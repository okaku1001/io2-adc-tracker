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
    "tagline": "以康方生物为中心，记录依沃西、卡度尼利及其战略竞品与伙伴的核心临床变动。",
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


def nav_html(prefix: str, current: str, site: dict) -> str:
    links = [
        ("index.html", "首页", "home"),
        ("entries/index.html", "条目", "entries"),
        ("daily/index.html", "每日动态", "daily"),
        ("about.html", "关于", "about"),
    ]
    items = []
    for href, label, key in links:
        cur = ' aria-current="page"' if key == current else ""
        items.append(f'<a href="{rel_to(prefix, href)}"{cur}>{label}</a>')
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
      <button class="icon-btn nav-toggle" type="button" aria-expanded="false" aria-label="打开菜单">☰</button>
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


def page(title: str, prefix: str, current: str, site: dict, body: str, extra_head: str = "") -> str:
    full = title if title == site["title"] else f"{title} · {site['title']}"
    css = rel_to(prefix, "css/style.css")
    js = rel_to(prefix, "js/app.js")
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
<body>
<a class="skip" href="#main">跳到正文</a>
{nav_html(prefix, current, site)}
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


def render_entry(entry: dict, site: dict) -> str:
    companies = chips(entry.get("companies", []))
    drugs = chips(entry.get("drugs", []))
    inds = chips(entry.get("indications", []))
    labels = []
    for g in entry.get("grades_present", []):
        labels.append(badge(g))

    def date_key(s):
        parts = (str(s) + "-01-01").split("-")[:3]
        return tuple(int(x) for x in parts)

    timeline_html = []
    for ev in sorted(entry.get("timeline", []), key=lambda item: date_key(item["date"])):
        grades = "".join(badge(g) for g in ev.get("grades", []))
        timeline_html.append(f"""<li>
  <div class="t-date">{html.escape(fmt_date(ev['date']))} {grades}</div>
  <h2>{html.escape(ev['title'])}</h2>
  {md_blocks(ev.get('body', ''))}
  {render_table(ev.get('table'))}
  {render_sources(ev.get('sources', []))}
</li>""")
    impact = entry.get("impact") or {}
    impact_html = ""
    if impact.get("text"):
        impact_html = f"""<aside class="impact">
  <h2>对康方的影响</h2>
  {md_blocks(impact['text'])}
  <p class="attr">{html.escape(impact.get('attribution', '研究组判断'))}</p>
</aside>"""
    body = f"""<article class="read entry-header">
  <p class="kicker">{html.escape(entry.get('kicker', '临床条目'))}</p>
  <h1>{html.escape(entry['title'])}</h1>
  <p class="lede muted">{md_inline(entry.get('subtitle', ''))}</p>
  <div class="card-foot">{companies}{drugs}{inds}{''.join(labels)}</div>
  <p class="status-line"><span>当前状态　</span>{md_inline(entry.get('status', ''))}</p>
</article>
<section class="read summary">{md_blocks(entry.get('summary', ''))}</section>
<ol class="read timeline">
{''.join(timeline_html)}
</ol>
<div class="read">{impact_html}</div>
<p class="read muted" style="margin-top:1.6rem">最后写入本条目的资料日期：{html.escape(fmt_date(entry.get('updated', site.get('source_as_of', '2026-11-10'))))}。</p>
"""
    return page(entry["title"], "../", "entries", site, body)


def unique(seq):
    out, seen = [], set()
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def entries_index(entries, site):
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
        cards.append(
            f"""<a class="card" data-entry-card href="{html.escape(e['slug'])}.html"
              data-companies="{'|'.join(e.get('companies', []))}"
              data-drugs="{'|'.join(e.get('drugs', []))}"
              data-indications="{'|'.join(e.get('indications', []))}"
              data-search="{html.escape(search)}">
  <p class="card-kicker">{html.escape(e.get('kicker', ''))}</p>
  <h3>{html.escape(e['title'])}</h3>
  <p>{html.escape(e.get('subtitle', ''))}</p>
  <div class="card-foot">{chips(e.get('drugs', [])[:3])}{chips(e.get('indications', [])[:2])}</div>
</a>"""
        )
    body = f"""<header class="hero read">
  <h1>条目</h1>
  <p class="lede">按药、试验或事件线组织。同一条线的新旧进展写在同一页，按时间往下读。</p>
</header>
<div class="filters">
  <div class="search-box"><input id="entry-search" type="search" placeholder="搜索药名、试验名、适应症或公司" aria-label="搜索条目"></div>
  <div><p class="muted" style="margin:0 0 .35rem">公司</p><div class="filter-row">{btns('company', companies)}</div></div>
  <div><p class="muted" style="margin:0 0 .35rem">药物</p><div class="filter-row">{btns('drug', drugs)}</div></div>
  <div><p class="muted" style="margin:0 0 .35rem">适应症</p><div class="filter-row">{btns('indication', inds)}</div></div>
</div>
<div class="grid">{''.join(cards)}</div>
<p id="filter-empty" class="empty-note hidden">没有符合筛选的条目。</p>
"""
    return page("条目", "../", "entries", site, body)


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
  <p class="t-date">{grades}</p>
  <h2>{link}</h2>
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
    body = f"""<header class="hero read">
  <p class="kicker">每日动态</p>
  <h1>{fmt_date(day['date'])}</h1>
  <p class="lede">{html.escape(day.get('title', ''))}</p>
</header>
<div class="read">{content}</div>
<p class="read muted"><a href="index.html">全部日期</a></p>
"""
    return page(fmt_date(day["date"]), "../", "daily", site, body)


def daily_index(dailies, site):
    cards = []
    for d in dailies:
        n = len(d.get("items", []))
        cls = "has" if n else ""
        label = f"{n} 条" if n else "无重大新增"
        cards.append(
            f'<a class="{cls}" href="{d["date"]}.html"><strong>{d["date"]}</strong><span class="n">{html.escape(label)}</span></a>'
        )
    body = f"""<header class="hero read">
  <h1>每日动态</h1>
  <p class="lede">每天只作索引，详情在对应条目里按时间线更新。安静的日子也会记下：查过、没有新的监管决定或 III 期读出。</p>
</header>
<div class="cal">{''.join(cards)}</div>
"""
    return page("每日动态", "../", "daily", site, body)


def home(entries, dailies, site):
    upcoming = site.get("upcoming", [])
    up_html = []
    for u in upcoming:
        up_html.append(
            f"""<article class="card">
  <p class="card-kicker">{html.escape(u.get('when', ''))}</p>
  <h3>{html.escape(u.get('title', ''))}</h3>
  <p>{html.escape(u.get('detail', ''))}</p>
</article>"""
        )
    recent = []
    count = 0
    for d in dailies:
        for it in d.get("items", []):
            slug = it.get("entry")
            href = f"entries/{slug}.html" if slug else f"daily/{d['date']}.html"
            recent.append(
                f"""<a class="card" href="{href}">
  <p class="card-kicker">{d['date']}</p>
  <h3>{html.escape(it.get('headline', ''))}</h3>
  <p>{html.escape(it.get('blurb', '')[:140])}{'…' if len(it.get('blurb', '')) > 140 else ''}</p>
</a>"""
            )
            count += 1
            if count >= 8:
                break
        if count >= 8:
            break

    groups = [
        ("依沃西主线", [e for e in entries if e.get("group") == "ivo"]),
        ("卡度尼利", [e for e in entries if e.get("group") == "cado"]),
        ("联用与伙伴", [e for e in entries if e.get("group") == "partner"]),
        ("竞品与对照", [e for e in entries if e.get("group") == "competitor"]),
    ]
    group_html = []
    for title, ents in groups:
        if not ents:
            continue
        cards = []
        for e in ents:
            cards.append(
                f"""<a class="card" href="entries/{e['slug']}.html">
  <p class="card-kicker">{html.escape(e.get('kicker', ''))}</p>
  <h3>{html.escape(e['title'])}</h3>
  <p>{html.escape(e.get('subtitle', ''))}</p>
</a>"""
            )
        group_html.append(
            f'<section><div class="section-h"><h2>{html.escape(title)}</h2></div><div class="grid">{"".join(cards)}</div></section>'
        )

    banner = site.get("banner") or {}
    banner_html = ""
    if banner.get("title"):
        banner_html = f"""<aside class="banner">
  <strong>{html.escape(banner['title'])}</strong>
  <p>{html.escape(banner.get('text', ''))}</p>
</aside>"""

    body = f"""<header class="hero">
  <h1>{html.escape(site['title'])}</h1>
  <p class="lede">{html.escape(site['tagline'])}</p>
  <p class="meta-row"><span>资料截至 {html.escape(site.get('source_as_of', '2026-11-10'))}（北京时间）</span><span>生成于 {html.escape(site['generated'])}（北京时间）</span></p>
</header>
{banner_html}
<section>
  <div class="section-h"><h2>即将到来</h2></div>
  <div class="grid">{''.join(up_html)}</div>
</section>
<section>
  <div class="section-h"><h2>最近动态</h2><a href="daily/index.html">全部日期</a></div>
  <div class="grid">{''.join(recent)}</div>
</section>
{''.join(group_html)}
"""
    return page(site["title"], "", "home", site, body)


def about_page(site):
    body = f"""<header class="hero read">
  <h1>关于本站</h1>
  <p class="lede">这是一份公开的临床动态整理，关注 IO2.0（以 PD-(L)1×VEGF 双抗为代表）和 ADC2.0 组合，中心是康方生物的依沃西与卡度尼利，以及它们的授权伙伴、联用药和直接竞品。</p>
</header>
<div class="read">
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
  <p>{html.escape(site['disclaimer'])}</p>
  <p class="muted">资料截至 {html.escape(site.get('source_as_of', '2026-11-10'))}（北京时间）。页面生成：{html.escape(site['generated'])}（北京时间，UTC+8）。</p>
</div>
"""
    return page("关于", "", "about", site, body)


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
    by_slug = {e["slug"]: e for e in entries}

    write(OUT / "index.html", home(entries, dailies, site))
    write(OUT / "about.html", about_page(site))
    write(OUT / "entries" / "index.html", entries_index(entries, site))
    for e in entries:
        write(OUT / "entries" / f"{e['slug']}.html", render_entry(e, site))
    write(OUT / "daily" / "index.html", daily_index(dailies, site))
    for d in dailies:
        write(OUT / "daily" / f"{d['date']}.html", daily_page(d, by_slug, site))
    write(OUT / "feed.xml", rss(dailies, by_slug, site))
    write(OUT / "favicon.svg", favicon())
    write(
        OUT / "robots.txt",
        f"User-agent: *\nAllow: /\nSitemap: {site['base_url']}/sitemap.xml\n",
    )
    urls = ["/", "/about.html", "/entries/", "/daily/", "/feed.xml"]
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
