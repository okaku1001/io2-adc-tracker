#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the public static site from data/entries.json and data/daily/*.json."""

from __future__ import annotations

import html
import json
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
OUT = ROOT

SITE_DEFAULT = {
    "title": "IO2.0+ADC 临床追踪",
    "tagline": "以康方生物已公布的成药、管线和平台技术为底盘，记录已核临床与监管变动，并延伸到与之构成竞争或合作的具体品种。同一条试验只保留一个条目，每日动态是索引。",
    "base_url": "https://okaku1001.github.io/io2-adc-tracker",
    "disclaimer": "本站为公开信息整理，不构成投资建议。数字均来自已核对的一手或已标注来源，不代表康方、Summit 或其他公司立场。",
}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def site_meta():
    meta = dict(SITE_DEFAULT)
    p = DATA / "site.json"
    if p.exists():
        meta.update(load_json(p))
    if not meta.get("generated"):
        meta["generated"] = datetime.now(ZoneInfo("Asia/Shanghai")).strftime("%Y-%m-%d %H:%M")
    return meta


def load_entries():
    raw = load_json(DATA / "entries.json")
    entries = raw if isinstance(raw, list) else raw.get("entries", [])
    entries.sort(key=lambda e: (e.get("priority", 99), e.get("title", "")))
    return entries


def load_dailies():
    days = []
    folder = DATA / "daily"
    if not folder.exists():
        return days
    for p in sorted(folder.glob("*.json")):
        days.append(load_json(p))
    days.sort(key=lambda d: d["date"], reverse=True)
    return days


def load_layout():
    path = DATA / "layout.json"
    if not path.exists():
        return {}
    return load_json(path)


def md_inline(text: str) -> str:
    if not text:
        return ""
    s = html.escape(text)

    def repl_link(m):
        return f'<a href="{m.group(2)}" rel="noopener noreferrer">{m.group(1)}</a>'

    s = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", repl_link, s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = s.replace("\n", "<br>")
    return s


def md_blocks(text: str) -> str:
    if not text:
        return ""
    parts = [p.strip() for p in text.split("\n\n") if p.strip()]
    return "".join(f"<p>{md_inline(p)}</p>" for p in parts)


def date_key(s):
    parts = (str(s) + "-01-01").split("-")[:3]
    return tuple(int(x) for x in parts)


def entry_recency_key(entry: dict):
    keys = []
    updated = entry.get("updated")
    if updated:
        keys.append(date_key(updated))
    for ev in entry.get("timeline") or []:
        if ev.get("date"):
            keys.append(date_key(ev["date"]))
    return max(keys) if keys else (0, 0, 0)


def sort_by_recency(items):
    return sorted(items, key=entry_recency_key, reverse=True)


def _matching_fw_paren_end(text: str, start: int):
    depth = 0
    for j in range(start, len(text)):
        if text[j] == "（":
            depth += 1
        elif text[j] == "）":
            depth -= 1
            if depth == 0:
                return j + 1
    return None


def _tidy_extracted_body(text: str) -> str:
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" +\n", "\n", text)
    text = re.sub(r"\n +", "\n", text)
    text = re.sub(r" +([。；，、])", r"\1", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _note_from_paren(raw: str) -> dict:
    inner = raw[1:-1] if raw.startswith("（") and raw.endswith("）") else raw
    m = re.match(r"更正日期\s*(\d{4}-\d{2}-\d{2})\s*[：:]\s*(.*)$", inner, re.S)
    if m:
        return {"date": m.group(1), "label": "更正", "text": m.group(2).strip()}
    return {"date": "", "label": "更正", "text": inner.strip()}


def _infer_note_date(text: str, year_hint: str = "") -> str:
    m = re.search(r"(20\d{2}-\d{2}-\d{2})", text)
    if m:
        return m.group(1)
    m = re.search(r"(\d{1,2})-(\d{1,2})\s*更正", text)
    if m and year_hint:
        return f"{year_hint}-{int(m.group(1)):02d}-{int(m.group(2)):02d}"
    return ""


_EXTRA_NOTE_RE = re.compile(
    r"(?:"
    r"[^。\n]*曾误写[^。\n]*。"
    r"|[^。\n]*已更正：[^\n。]*。"
    r"|[^。\n]*，已更正。"
    r"|[^。\n]*更正为已经纳入。"
    r")"
)


def split_corrections(text: str, year_hint: str = "") -> tuple:
    """Split body into fact text and correction notes. Does not alter source data."""
    if not text:
        return "", []
    notes = []
    pieces = []
    i = 0
    while i < len(text):
        m = re.search(r"（更正日期", text[i:])
        if not m:
            pieces.append(text[i:])
            break
        start = i + m.start()
        end = _matching_fw_paren_end(text, start)
        if end is None:
            pieces.append(text[i:])
            break
        pieces.append(text[i:start])
        notes.append(_note_from_paren(text[start:end]))
        i = end
    body = "".join(pieces)
    extras = []

    def take_extra(match: re.Match) -> str:
        raw = match.group(0).strip()
        extras.append(
            {
                "date": _infer_note_date(raw, year_hint),
                "label": "更正",
                "text": raw,
            }
        )
        return ""

    body = _EXTRA_NOTE_RE.sub(take_extra, body)
    notes.extend(extras)
    return _tidy_extracted_body(body), notes


def render_corrections(notes) -> str:
    bits = []
    for n in notes:
        label = n.get("label") or "更正"
        if n.get("date"):
            label = f"{label} {n['date']}"
        bits.append(
            '<aside class="correction">'
            f'<p class="correction-label">{html.escape(label)}</p>'
            f'<p>{md_inline(n.get("text") or "")}</p>'
            "</aside>"
        )
    return "".join(bits)



def fmt_date(iso: str, with_year: bool = True) -> str:
    parts = iso.split("-")
    if len(parts) == 1:
        return f"{parts[0]}年"
    if len(parts) == 2:
        y, m = parts
        return f"{y}年{int(m)}月" if with_year else f"{int(m)}月"
    y, m, d = parts
    if with_year:
        return f"{y}年{int(m)}月{int(d)}日"
    return f"{int(m)}月{int(d)}日"


def badge(label: str) -> str:
    safe = html.escape(label)
    cls = label if label in ("一手", "二手", "未核实", "推论", "推断") else "chip"
    return f'<span class="badge badge-{html.escape(cls)}">{safe}</span>'


def chips(items):
    return "".join(f'<span class="chip">{html.escape(x)}</span>' for x in items)


def rel_to(prefix: str, target: str) -> str:
    if target.startswith("http"):
        return target
    return prefix + target


def nav_html(prefix: str, current: str, site: dict, toc_launch: bool = False) -> str:
    layout = load_layout()
    guide_label = layout.get("nav_label") or "管线与竞争"
    links = [
        ("index.html", "首页", "home", ""),
        ("pipeline.html", guide_label, "pipeline", "nav-guide"),
        ("entries/index.html", "条目", "entries", ""),
        ("daily/index.html", "每日动态", "daily", ""),
        ("about.html", "关于", "about", ""),
    ]
    items = []
    for href, label, key, cls in links:
        cur = ' aria-current="page"' if key == current else ""
        class_attr = f' class="{cls}"' if cls else ""
        items.append(f'<a href="{rel_to(prefix, href)}"{class_attr}{cur}>{html.escape(label)}</a>')
    toc_btn = ""
    if toc_launch:
        toc_btn = (
            '<button class="toc-launch" type="button" aria-expanded="false" '
            'aria-controls="entry-toc">时间线</button>'
        )
    return f"""<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="{rel_to(prefix, 'index.html')}">
      <svg class="brand-mark" viewBox="0 0 40 40" aria-hidden="true">
        <circle cx="16" cy="20" r="11" fill="none" stroke="currentColor" stroke-width="2.2"/>
        <circle cx="24" cy="20" r="11" fill="none" stroke="currentColor" stroke-width="2.2"/>
      </svg>
      <span class="brand-text">
        <span class="brand-title">{html.escape(site['title'])}</span>
        <span class="brand-sub">公开临床动态 · 不构成投资建议</span>
      </span>
    </a>
    <nav class="nav" aria-label="主导航">
      {toc_btn}<button class="icon-btn nav-toggle" type="button" aria-expanded="false" aria-label="打开菜单">☰</button>
      <div class="nav-links">{''.join(items)}</div>
      <button class="icon-btn" id="theme-toggle" type="button" aria-label="切换深浅色">◐</button>
    </nav>
  </div>
</header>"""


def footer_html(prefix: str, site: dict) -> str:
    return f"""<footer class="site-footer">
  <div class="footer-inner">
    <p>{html.escape(site['disclaimer'])}</p>
    <p>资料截至 {html.escape(site.get('source_as_of', '2026-11-10'))}（北京时间）。页面生成：{html.escape(site['generated'])}（北京时间，UTC+8）。</p>
    <p class="footer-links">
      <a href="{rel_to(prefix, 'feed.xml')}">RSS</a>
      <a href="{rel_to(prefix, 'about.html')}">方法与来源说明</a>
      <a href="{site.get('repo_url', 'https://github.com/okaku1001/io2-adc-tracker')}">GitHub</a>
    </p>
  </div>
</footer>"""


def page(title: str, prefix: str, current: str, site: dict, body: str, extra_head: str = "", body_class: str = "", skips=None) -> str:
    full = title if title == site["title"] else f"{title} · {site['title']}"
    css = rel_to(prefix, "css/style.css")
    js = rel_to(prefix, "js/app.js")
    skip_links = ['<a class="skip" href="#main">跳到正文</a>']
    if skips:
        for href, label in skips:
            skip_links.append(f'<a class="skip" href="{html.escape(href)}">{html.escape(label)}</a>')
    progress = ""
    if body_class == "page-entry":
        progress = '<div class="read-progress" aria-hidden="true"><span></span></div>'
    body_attr = f' class="{html.escape(body_class)}"' if body_class else ""
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(full)}</title>
<meta name="description" content="{html.escape(site['tagline'])}">
<meta name="color-scheme" content="light dark">
<link rel="stylesheet" href="{css}">
<link rel="alternate" type="application/rss+xml" title="{html.escape(site['title'])}" href="{rel_to(prefix, 'feed.xml')}">
<link rel="icon" href="{rel_to(prefix, 'favicon.svg')}" type="image/svg+xml">
{extra_head}
</head>
<body{body_attr}>
{progress}
{"".join(skip_links)}
{nav_html(prefix, current, site, toc_launch=(body_class == 'page-entry'))}
<main id="main" class="wrap">
{body}
</main>
{footer_html(prefix, site)}
<script src="{js}" defer></script>
</body>
</html>
"""


def render_table(table: dict) -> str:
    if not table:
        return ""
    heads = "".join(f"<th>{html.escape(h)}</th>" for h in table.get("headers", []))
    rows = []
    for row in table.get("rows", []):
        rows.append("<tr>" + "".join(f"<td>{md_inline(c)}</td>" for c in row) + "</tr>")
    return f'<div class="table-wrap"><table class="data"><thead><tr>{heads}</tr></thead><tbody>{"".join(rows)}</tbody></table></div>'


def render_sources(sources) -> str:
    if not sources:
        return ""
    bits = []
    for s in sources:
        label = s.get("label") or s.get("url") or "来源"
        url = s.get("url")
        grade = s.get("grade")
        if url:
            bits.append(f'<a href="{html.escape(url)}" rel="noopener noreferrer">{html.escape(label)}</a>')
        else:
            bits.append(html.escape(label))
        if grade:
            bits.append(badge(grade))
    return f'<p class="sources">来源：{" ".join(bits)}</p>'


def entry_url(slug: str, prefix: str = "") -> str:
    return rel_to(prefix, f"entries/{slug}.html")


def layout_item_map(layout: dict) -> dict:
    found = {}
    for section in layout.get("sections", []):
        for item in section.get("items", []):
            slug = item.get("slug")
            if slug:
                found[slug] = item
    return found


def collect_layout_slugs(layout: dict):
    slugs = []
    seen = set()

    def add(slug):
        if slug and slug not in seen:
            seen.add(slug)
            slugs.append(slug)

    for section in layout.get("sections", []):
        for item in section.get("items", []):
            add(item.get("slug"))
            for cluster in item.get("clusters", []):
                for slug in cluster.get("slugs", []):
                    add(slug)
            extra = item.get("related_extra") or {}
            for kind_slugs in extra.values():
                for slug in kind_slugs:
                    add(slug)
    return slugs


def warn_layout(layout: dict, entries):
    by_slug = {e["slug"]: e for e in entries}
    listed = collect_layout_slugs(layout)
    missing = [s for s in listed if s not in by_slug]
    uncovered = [e["slug"] for e in entries if e["slug"] not in set(listed)]
    if missing:
        print("layout missing entries:", ", ".join(missing))
    if uncovered:
        print("entries not in layout:", ", ".join(uncovered))


def related_groups_for(item: dict, layout: dict, hub_slug: str = ""):
    kinds = layout.get("cluster_kinds") or {}
    grouped = {}
    order = []

    def add(kind, slug):
        if not kind or not slug or slug == hub_slug:
            return
        if kind not in grouped:
            grouped[kind] = []
            order.append(kind)
        if slug not in grouped[kind]:
            grouped[kind].append(slug)

    for cluster in item.get("clusters", []):
        kind = kinds.get(cluster.get("title", ""), "试验")
        for slug in cluster.get("slugs", []):
            add(kind, slug)
    extra = item.get("related_extra") or {}
    for kind, slugs in extra.items():
        for slug in slugs:
            add(kind, slug)
    return [(kind, grouped[kind]) for kind in order]


def entry_status_line(entry: dict) -> str:
    return (entry.get("subtitle") or entry.get("status") or entry.get("title") or "").strip()


def render_guide_row(entry: dict, prefix: str, compact: bool, extra_class: str = "") -> str:
    sub = "" if compact else entry_status_line(entry)
    sub_html = f'<p class="catalog-sub">{html.escape(sub)}</p>' if sub else ""
    cls = f"catalog-row{(' ' + extra_class) if extra_class else ''}"
    return f"""<a class="{cls}" href="{html.escape(entry_url(entry['slug'], prefix))}">
    <p class="kicker">{html.escape(entry.get('kicker', ''))}</p>
    <h4 class="catalog-title">{html.escape(entry['title'])}</h4>
    {sub_html}
  </a>"""


def render_guide(layout: dict, entries, prefix: str, compact: bool = False) -> str:
    by_slug = {e["slug"]: e for e in entries}
    sections_html = []
    for section in layout.get("sections", []):
        hubs = []
        for item in section.get("items", []):
            slug = item.get("slug")
            entry = by_slug.get(slug)
            if not entry:
                continue
            clusters_html = []
            for cluster in item.get("clusters", []):
                rows = []
                children = []
                for child_slug in cluster.get("slugs", []):
                    if child_slug == slug:
                        continue
                    child = by_slug.get(child_slug)
                    if not child:
                        continue
                    children.append(child)
                for child in sort_by_recency(children):
                    rows.append(f"<li>{render_guide_row(child, prefix, compact)}</li>")
                if not rows:
                    continue
                clusters_html.append(
                    f'<div class="guide-cluster">'
                    f'<h4>{html.escape(cluster.get("title", ""))}</h4>'
                    f'<ul class="catalog-list">{"".join(rows)}</ul>'
                    f"</div>"
                )
            status = entry_status_line(entry)
            status_html = f'<p class="guide-status">{html.escape(status)}</p>' if status else ""
            hub_id = html.escape(slug)
            hubs.append(
                f'''<article class="guide-hub" id="{hub_id}">
  <a class="guide-hub-head catalog-row" href="{html.escape(entry_url(slug, prefix))}">
    <p class="kicker">{html.escape(entry.get("kicker", ""))}</p>
    <h4 class="catalog-title">{html.escape(entry["title"])}</h4>
    {status_html}
  </a>
  {"".join(clusters_html)}
</article>'''
            )
        if not hubs:
            continue
        sid = html.escape(section.get("id") or "")
        sections_html.append(
            f'<section class="guide-section" id="{sid}">'
            f'<h3>{html.escape(section.get("title", ""))}</h3>'
            f'{"".join(hubs)}'
            f"</section>"
        )
    if not sections_html:
        return ""
    compact_cls = " is-compact" if compact else ""
    return f'<div class="guide{compact_cls}">{"".join(sections_html)}</div>'


def render_related(entry: dict, layout: dict, entries, prefix: str) -> str:
    item = layout_item_map(layout).get(entry["slug"])
    if not item:
        return ""
    groups = related_groups_for(item, layout, hub_slug=entry["slug"])
    if not groups:
        return ""
    by_slug = {e["slug"]: e for e in entries}
    blocks = []
    for kind, slugs in groups:
        lis = []
        children = [by_slug[s] for s in slugs if s in by_slug]
        for child in sort_by_recency(children):
            slug = child["slug"]
            kicker = html.escape(child.get("kicker", ""))
            kicker_html = f'<span class="kicker">{kicker}</span>' if kicker else ""
            lis.append(
                f'<li><a href="{html.escape(entry_url(slug, prefix))}">{kicker_html}'
                f'<span class="related-title">{html.escape(child["title"])}</span></a></li>'
            )
        if lis:
            blocks.append(
                f"<h3>{html.escape(kind)}</h3><ul class=\"related-list\">{''.join(lis)}</ul>"
            )
    if not blocks:
        return ""
    guide_href = rel_to(prefix, f"pipeline.html#{entry['slug']}")
    more = '<p class="related-more"><a href="' + html.escape(guide_href) + '">在「管线与竞争」中查看</a></p>'
    return (
        '<section class="related" aria-labelledby="related-h">'
        '<h2 id="related-h">相关条目</h2>'
        + "".join(blocks)
        + more
        + "</section>"
    )



def event_anchor(date: str, index: int) -> str:
    safe = re.sub(r"[^0-9A-Za-z-]+", "-", str(date)).strip("-")
    return f"ev-{safe}-{index}"


def render_entry(entry: dict, site: dict, layout: dict, entries) -> str:
    companies = chips(entry.get("companies", []))
    drugs = chips(entry.get("drugs", []))
    inds = chips(entry.get("indications", []))
    labels = []
    for g in entry.get("grades_present", []):
        labels.append(badge(g))

    events = sorted(entry.get("timeline", []), key=lambda item: date_key(item["date"]), reverse=True)
    timeline_html = []
    toc_items = []
    for i, ev in enumerate(events):
        eid = event_anchor(ev["date"], i)
        grades = "".join(badge(g) for g in ev.get("grades", []))
        ev_body, ev_notes = split_corrections(ev.get("body", ""), str(ev.get("date", ""))[:4])
        timeline_html.append(f"""<li id="{html.escape(eid)}">
  <div class="t-date">{html.escape(fmt_date(ev['date']))} {grades}</div>
  <h2>{html.escape(ev['title'])}</h2>
  {md_blocks(ev_body)}
  {render_corrections(ev_notes)}
  {render_table(ev.get('table'))}
  {render_sources(ev.get('sources', []))}
</li>""")
        toc_items.append(
            f'<li><a href="#{html.escape(eid)}"><span class="toc-date">{html.escape(fmt_date(ev["date"]))}</span><span class="toc-title">{html.escape(ev["title"])}</span></a></li>'
        )
    toc_html = ""
    if toc_items:
        toc_html = f"""<div class="toc-slot">
<nav class="toc" id="entry-toc" aria-labelledby="toc-label">
  <div class="toc-panel-head">
    <p class="toc-label" id="toc-label">本页时间线</p>
    <button class="toc-close" type="button" aria-label="关闭时间线目录">关闭</button>
  </div>
  <p class="toc-resume hidden"></p>
  <ol>{''.join(toc_items)}</ol>
</nav>
</div>"""
    impact = entry.get("impact") or {}
    impact_html = ""
    if impact.get("text"):
        impact_html = f"""<aside class="impact">
  <h2>对康方的影响</h2>
  {md_blocks(impact['text'])}
  <p class="attr">{html.escape(impact.get('attribution', '研究组判断'))}</p>
</aside>"""
    status = entry.get("status", "")
    status_html = ""
    if status:
        year_hint = str(entry.get("updated") or entry.get("date") or "")[:4]
        status_body, status_notes = split_corrections(status, year_hint)
        status_html = f"""<section class="status-box" aria-labelledby="status-heading">
  <h2 id="status-heading" class="status-label">当前状态</h2>
  <p class="status-text">{md_inline(status_body)}</p>
  {render_corrections(status_notes)}
</section>"""
    skips = [("#timeline", "跳到时间线")] if events else None
    if toc_items:
        skips = (skips or []) + [("#entry-toc", "本页时间线目录")]
    related_html = render_related(entry, layout or {}, entries or [], "../")
    summary_body, summary_notes = split_corrections(
        entry.get("summary", ""), str(entry.get("updated") or "")[:4]
    )
    body = f"""<article class="entry-layout">
  <header class="entry-header">
    <p class="kicker">{html.escape(entry.get('kicker', '临床条目'))}</p>
    <h1>{html.escape(entry['title'])}</h1>
    <p class="lede muted">{md_inline(entry.get('subtitle', ''))}</p>
    <div class="card-foot">{companies}{drugs}{inds}{''.join(labels)}</div>
  </header>
  {status_html}
  <section class="summary">{md_blocks(summary_body)}{render_corrections(summary_notes)}</section>
  {toc_html}
  <ol class="timeline" id="timeline">
{''.join(timeline_html)}
  </ol>
  {impact_html}
  {related_html}
  <p class="entry-updated muted">最后写入本条目的资料日期：{html.escape(fmt_date(entry.get('updated', site.get('source_as_of', '2026-11-10'))))}。</p>
</article>
"""
    return page(entry["title"], "../", "entries", site, body, body_class="page-entry", skips=skips)


def unique(seq):
    out, seen = [], set()
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def entries_index(entries, site, layout=None):
    layout = layout or {}
    group_labels = layout.get("group_labels") or {
        "ivo": "依沃西",
        "cado": "卡度尼利",
        "akeso-other": "康方其他品种与平台",
        "partner": "合作与联用",
        "competitor": "竞争与对照",
        "policy": "政策与规则",
    }
    group_order = unique(
        [g for g in group_labels if any(e.get("group") == g for e in entries)]
        + [e.get("group") for e in entries if e.get("group")]
    )
    companies = unique(c for e in entries for c in e.get("companies", []))
    drugs = unique(d for e in entries for d in e.get("drugs", []))
    inds = unique(i for e in entries for i in e.get("indications", []))

    def btns(key, vals):
        first = f'<button class="filter-btn" type="button" data-key="{key}" data-val="全部" aria-pressed="true">全部</button>'
        rest = "".join(
            f'<button class="filter-btn" type="button" data-key="{key}" data-val="{html.escape(v)}" aria-pressed="false">{html.escape(v)}</button>'
            for v in vals
        )
        return first + rest

    cards = []
    for e in entries:
        search = " ".join(
            [
                e.get("title", ""),
                e.get("subtitle", ""),
                e.get("summary", ""),
                e.get("status", ""),
                " ".join(e.get("companies", [])),
                " ".join(e.get("drugs", [])),
                " ".join(e.get("indications", [])),
                " ".join(e.get("aliases", [])),
            ]
        )
        updated = e.get("updated") or site.get("source_as_of", "2026-11-10")
        sub = e.get("subtitle") or ""
        sub_html = f'<p class="entry-sub">{html.escape(sub)}</p>' if sub else ""
        cards.append(
            f"""<a class="entry-row" data-entry-card href="{html.escape(e['slug'])}.html"
              data-group="{html.escape(e.get('group', ''))}"
              data-companies="{'|'.join(e.get('companies', []))}"
              data-drugs="{'|'.join(e.get('drugs', []))}"
              data-indications="{'|'.join(e.get('indications', []))}"
              data-search="{html.escape(search)}">
  <p class="kicker">{html.escape(e.get('kicker', ''))}</p>
  <h3 class="entry-title">{html.escape(e['title'])}</h3>
  {sub_html}
  <p class="entry-meta"><time datetime="{html.escape(updated)}">{html.escape(fmt_date(updated))}</time></p>
  <div class="card-foot">{chips(e.get('drugs', [])[:3])}{chips(e.get('indications', [])[:2])}</div>
</a>"""
        )
    group_btns = '<button class="filter-btn" type="button" data-key="group" data-val="全部" aria-pressed="true">全部</button>'
    group_btns += "".join(
        f'<button class="filter-btn" type="button" data-key="group" data-val="{html.escape(g)}" aria-pressed="false">{html.escape(group_labels.get(g, g))}</button>'
        for g in group_order
    )
    body = f"""<header class="hero">
  <h1>条目</h1>
  <p class="lede">按药、试验或事件线组织。同一条线的新旧进展写在同一页，按时间往下读。按品种看竞争关系，请走「管线与竞争」。</p>
</header>
<div class="filters">
  <div class="search-box"><input id="entry-search" type="search" placeholder="搜索药名、试验名、适应症或公司" aria-label="搜索条目"></div>
  <details class="filter-panel">
    <summary>筛选分类、公司、药物、适应症</summary>
    <div class="filter-groups">
      <div><p class="filter-label">分类</p><div class="filter-row">{group_btns}</div></div>
      <div><p class="filter-label">公司</p><div class="filter-row">{btns('company', companies)}</div></div>
      <div><p class="filter-label">药物</p><div class="filter-row">{btns('drug', drugs)}</div></div>
      <div><p class="filter-label">适应症</p><div class="filter-row">{btns('indication', inds)}</div></div>
    </div>
  </details>
</div>
<div class="entry-list">{''.join(cards)}</div>
<p id="filter-empty" class="empty-note hidden">没有符合筛选的条目。</p>
"""
    return page("条目", "../", "entries", site, body, body_class="page-entries")


def daily_page(day, entries_by_slug, site):
    items = []
    for it in day.get("items", []):
        slug = it.get("entry")
        href = f"../entries/{slug}.html" if slug else ""
        title = it.get("headline") or (entries_by_slug.get(slug, {}) or {}).get("title", "")
        grades = "".join(badge(g) for g in it.get("grades", []))
        link = f'<a href="{href}">{html.escape(title)}</a>' if href else html.escape(title)
        items.append(
            f"""<article class="day-item">
  <h2>{link}</h2>
  <p class="day-grades">{grades}</p>
  {md_blocks(it.get('blurb', ''))}
</article>"""
        )
    note = md_blocks(day.get("note", ""))
    extra = f'<div class="empty-note">{note}</div>' if day.get("note") else ""
    if not items and extra:
        content = extra
    elif not items:
        content = '<div class="empty-note"><p>本日无新增重大临床动态。</p></div>'
    else:
        content = extra + "".join(items)
    body = f"""<article class="brief">
  <header class="brief-header">
    <p class="kicker">每日动态</p>
    <h1>{fmt_date(day['date'])}</h1>
    <p class="lede">{html.escape(day.get('title', ''))}</p>
  </header>
  {content}
  <p class="brief-back muted"><a href="index.html">全部日期</a></p>
</article>
"""
    return page(fmt_date(day["date"]), "../", "daily", site, body, body_class="page-daily")


def daily_index(dailies, site):
    cards = []
    for d in dailies:
        n = len(d.get("items", []))
        cls = "has" if n else ""
        label = f"{n} 条" if n else "无重大新增"
        cards.append(
            f'<a class="{cls}" href="{d["date"]}.html"><strong>{d["date"]}</strong><span class="n">{html.escape(label)}</span></a>'
        )
    body = f"""<header class="hero">
  <h1>每日动态</h1>
  <p class="lede">每天只作索引，详情在对应条目里按时间线更新。安静的日子也会记下：查过、没有新的监管决定或 III 期读出。</p>
</header>
<div class="cal">{''.join(cards)}</div>
"""
    return page("每日动态", "../", "daily", site, body, body_class="page-daily-index")


def home(entries, dailies, site, layout=None):
    upcoming = site.get("upcoming", [])

    def rail_lis(items, passed: bool) -> str:
        bits = []
        for u in items:
            detail = u.get("detail") or ""
            detail_html = f'<p class="rail-detail">{html.escape(detail)}</p>' if detail else ""
            cls = ' class="is-passed"' if passed else ""
            tag = '<p class="passed-tag">已过计划日</p>' if passed else ""
            bits.append(
                f"""<li{cls}>
  <p class="when">{html.escape(u.get('when', ''))}</p>
  <div>
    {tag}
    <p class="rail-title">{html.escape(u.get('title', ''))}</p>
    {detail_html}
  </div>
</li>"""
            )
        return "".join(bits)

    future = [u for u in upcoming if not u.get("passed")]
    past = [u for u in upcoming if u.get("passed")]

    recent_items = []
    for d in dailies:
        for it in d.get("items", []):
            slug = it.get("entry")
            href = f"entries/{slug}.html" if slug else f"daily/{d['date']}.html"
            recent_items.append(
                {
                    "date": d["date"],
                    "href": href,
                    "headline": it.get("headline", ""),
                    "blurb": it.get("blurb", ""),
                }
            )
            if len(recent_items) >= 8:
                break
        if len(recent_items) >= 8:
            break

    lead_html = ""
    list_html = ""
    if recent_items:
        lead = recent_items[0]
        blurb = lead.get("blurb") or ""
        blurb_html = f'<p class="lead-blurb">{html.escape(blurb)}</p>' if blurb else ""
        lead_html = f"""<a class="lead" href="{html.escape(lead['href'])}">
  <p class="lead-date">{html.escape(lead['date'])}</p>
  <h3 class="lead-title">{html.escape(lead['headline'])}</h3>
  {blurb_html}
</a>"""
        rest = []
        for it in recent_items[1:]:
            extra = f'<p class="story-blurb">{html.escape(it["blurb"])}</p>' if it.get("blurb") else ""
            rest.append(
                f"""<li>
  <a class="story-item" href="{html.escape(it['href'])}">
    <time datetime="{html.escape(it['date'])}">{html.escape(it['date'])}</time>
    <span class="story-title">{html.escape(it['headline'])}</span>
    {extra}
  </a>
</li>"""
            )
        if rest:
            list_html = f'<ul class="story-list">{"".join(rest)}</ul>'

    news_block = ""
    if lead_html or list_html:
        news_block = f"""<section class="briefing-news" aria-labelledby="recent-h">
  <div class="section-h"><h2 id="recent-h">最近动态</h2><a href="daily/index.html">全部日期</a></div>
  {lead_html}
  {list_html}
</section>"""

    rails = []
    if future:
        rails.append(
            f"""<aside class="briefing-rail" aria-labelledby="upcoming-h">
  <div class="section-h"><h2 id="upcoming-h">即将到来</h2></div>
  <ul class="date-rail">{rail_lis(future, False)}</ul>
</aside>"""
        )
    if past:
        rails.append(
            f"""<aside class="briefing-rail is-passed" aria-labelledby="passed-h">
  <div class="section-h"><h2 id="passed-h">已过计划日</h2></div>
  <ul class="date-rail">{rail_lis(past, True)}</ul>
</aside>"""
        )
    up_block = f'<div class="briefing-rails">{"".join(rails)}</div>' if rails else ""

    layout = layout or {}
    guide_html = render_guide(layout, entries, "", compact=True)
    catalog_block = ""
    if guide_html:
        section_title = html.escape(layout.get("home_section_title") or "管线与竞争")
        home_intro = layout.get("home_intro") or ""
        intro_html = f'<p class="guide-intro">{html.escape(home_intro)}</p>' if home_intro else ""
        catalog_block = f"""<section class="catalog guide-home" aria-labelledby="catalog-h">
  <div class="section-h">
    <h2 id="catalog-h">{section_title}</h2>
    <a class="guide-jump" href="pipeline.html">完整导览</a>
  </div>
  {intro_html}
  {guide_html}
  <p class="guide-foot"><a href="pipeline.html">打开完整「管线与竞争」导览</a> · <a href="entries/index.html">筛选全部条目</a></p>
</section>"""

    banner = site.get("banner") or {}
    banner_html = ""
    if banner.get("title"):
        banner_html = f"""<aside class="banner">
  <strong>{html.escape(banner['title'])}</strong>
  <p>{html.escape(banner.get('text', ''))}</p>
</aside>"""

    body = f"""<header class="masthead">
  <h1>{html.escape(site['title'])}</h1>
  <p class="lede">{html.escape(site['tagline'])}</p>
  <p class="lede read-path">先看最近动态和即将到来的日期，再按「<a href="pipeline.html">管线与竞争</a>」查阅品种与已挂上的相关条目。</p>
  <p class="meta-row"><span>资料截至 {html.escape(site.get('source_as_of', '2026-11-10'))}（北京时间）</span><span>生成于 {html.escape(site['generated'])}（北京时间）</span></p>
</header>
<div class="home-board">
{news_block}
{up_block}
{banner_html}
{catalog_block}
</div>
"""
    return page(site["title"], "", "home", site, body, body_class="page-home")


def pipeline_page(entries, site, layout=None):
    layout = layout or {}
    title = layout.get("page_title") or "管线与竞争"
    intro = layout.get("intro") or ""
    toc = []
    for section in layout.get("sections", []):
        sid = section.get("id")
        stitle = section.get("title")
        if sid and stitle:
            toc.append(f'<a href="#{html.escape(sid)}">{html.escape(stitle)}</a>')
    toc_html = f'<nav class="guide-toc" aria-label="本页分节">{"".join(toc)}</nav>' if toc else ""
    intro_html = f'<p class="lede">{html.escape(intro)}</p>' if intro else ""
    body = f"""<header class="hero">
  <h1>{html.escape(title)}</h1>
  {intro_html}
</header>
{toc_html}
{render_guide(layout, entries, "", compact=False)}
<p class="guide-foot"><a href="entries/index.html">筛选全部条目</a> · <a href="index.html">返回首页最近动态</a></p>
"""
    return page(title, "", "pipeline", site, body, body_class="page-pipeline")


def about_page(site):
    body = f"""<header class="hero read">
  <h1>关于本站</h1>
  <p class="lede">这是一份公开的临床动态整理。覆盖范围以康方生物已公布的全部成药、管线和平台技术为底盘，再延伸到全球能与之形成竞争或合作的具体管线与药物。不再只聚焦依沃西与卡度尼利。影响相关合作或商务发展的政策、交易规则，核实后也会单独成条收入。不把再鼎、亚盛、金斯瑞、百济、信达、恒瑞、君实、荣昌等公司的整条管线无差别并入，也不把与康方不构成竞争或合作的全球公司整线搬进来，只收与康方已公布成药、管线或平台相关的具体品种。本站覆盖仍在按已核材料补全，不表示已经穷尽。</p>
</header>
<div class="read">
  <p>阅读时可先看首页的「最近动态」和「即将到来」，再进入「管线与竞争」按康方品种查看已挂上的试验、竞争与合作。条目时间线仍是完整正文。</p>
  <p>同一条试验、同一个药、同一件监管事项只保留一个条目。新进展并进原条目的时间线，不按日期拆成互不相干的短讯。每日动态页只作索引，指回这些条目。</p>
  <p>数字都带来源和日期。公司或会议上不同时点给出的口径，写成轨迹：哪一天怎么说、后来改成了什么、现在以哪一版为准。没有头对头比较时，不写「优于」或「低于」。跨试验数字只并置，并说明不可比。</p>
  <p>来源分成四类，条目里会看得见：</p>
  <ul>
    <li><strong>一手</strong>：交易所或公司公告、监管机构、登记库、会议官方摘要、原始论文；</li>
    <li><strong>二手</strong>：媒体、会议转述、第三方数据库；</li>
    <li><strong>未核实</strong>：尚未看到原文或未能回到原页；</li>
    <li><strong>推论</strong>：写明依据，以及判断来自研究组而非公司原文。</li>
  </ul>
  <p>本站不收录股价、融资细节、持仓或买卖建议，也不把计划中的日期写成已经读出或已经获批。</p>
  <p>公开站每天约 8:30（北京时间）更新一次，周末也更新。已上线内容若发现错误，会尽快在原条目改正并注明日期和依据。2026-11-16 起曾改为严格每周一更新；11-26 先补上 11-23 未更的一轮，随后恢复日更，并把覆盖基准调整为康方已公布的成药、管线和平台技术，以及与之构成竞争或合作的具体品种。覆盖仍在按已核材料补全，不表示整站已经穷尽。</p>
  <p>{html.escape(site['disclaimer'])}</p>
  <p class="muted">资料截至 {html.escape(site.get('source_as_of', '2026-11-10'))}（北京时间）。页面生成：{html.escape(site['generated'])}（北京时间，UTC+8）。</p>
</div>
"""
    return page("关于", "", "about", site, body, body_class="page-about")


def write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def rss(dailies, entries_by_slug, site):
    items = []
    for d in dailies:
        for it in d.get("items", []):
            slug = it.get("entry")
            link = f"{site['base_url']}/entries/{slug}.html" if slug else f"{site['base_url']}/daily/{d['date']}.html"
            title = it.get("headline") or ""
            desc = html.escape(it.get("blurb") or "")
            items.append(
                f"""<item>
  <title>{html.escape(title)}</title>
  <link>{html.escape(link)}</link>
  <guid>{html.escape(link + '#' + d['date'])}</guid>
  <pubDate>{d['date']}</pubDate>
  <description>{desc}</description>
</item>"""
            )
        if len(items) >= 40:
            break
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
  <title>{html.escape(site['title'])}</title>
  <link>{html.escape(site['base_url'])}/</link>
  <description>{html.escape(site['tagline'])}</description>
  <language>zh-cn</language>
  <lastBuildDate>{html.escape(site['generated'])} +0800</lastBuildDate>
  {''.join(items)}
</channel>
</rss>
"""


def favicon():
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40">
  <rect width="40" height="40" rx="8" fill="#0c5849"/>
  <circle cx="16" cy="20" r="9" fill="none" stroke="#f4efe6" stroke-width="2.2"/>
  <circle cx="24" cy="20" r="9" fill="none" stroke="#f4efe6" stroke-width="2.2"/>
</svg>
"""


def main():
    site = site_meta()
    entries = load_entries()
    dailies = load_dailies()
    layout = load_layout()
    warn_layout(layout, entries)
    by_slug = {e["slug"]: e for e in entries}

    write(OUT / "index.html", home(entries, dailies, site, layout))
    write(OUT / "pipeline.html", pipeline_page(entries, site, layout))
    write(OUT / "about.html", about_page(site))
    write(OUT / "entries" / "index.html", entries_index(entries, site, layout))
    for e in entries:
        write(OUT / "entries" / f"{e['slug']}.html", render_entry(e, site, layout, entries))
    write(OUT / "daily" / "index.html", daily_index(dailies, site))
    for d in dailies:
        write(OUT / "daily" / f"{d['date']}.html", daily_page(d, by_slug, site))
    write(OUT / "feed.xml", rss(dailies, by_slug, site))
    write(OUT / "favicon.svg", favicon())
    write(
        OUT / "robots.txt",
        f"User-agent: *\nAllow: /\nSitemap: {site['base_url']}/sitemap.xml\n",
    )
    urls = ["/", "/pipeline.html", "/about.html", "/entries/", "/daily/", "/feed.xml"]
    urls += [f"/entries/{e['slug']}.html" for e in entries]
    urls += [f"/daily/{d['date']}.html" for d in dailies]
    sm = ["<?xml version='1.0' encoding='UTF-8'?>", '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f"<url><loc>{html.escape(site['base_url'] + u)}</loc></url>")
    sm.append("</urlset>")
    write(OUT / "sitemap.xml", "\n".join(sm) + "\n")

    print(f"built {len(entries)} entries, {len(dailies)} daily pages")


if __name__ == "__main__":
    main()
