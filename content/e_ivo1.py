# -*- coding: utf-8 -*-
ENTRIES = []

ENTRIES.append({
    "slug": "harmoni-fda",
    "title": "依沃西美国 BLA（HARMONi）",
    "subtitle": "EGFR 突变非鳞 NSCLC、三代 TKI 之后，依沃西联合化疗。PDUFA 日为 2026-11-14。",
    "kicker": "监管 · 全球 HARMONi",
    "group": "ivo",
    "priority": 1,
    "companies": ["康方生物", "Summit"],
    "drugs": ["依沃西"],
    "indications": ["NSCLC"],
    "aliases": ["SMT112", "AK112", "ivonescimab", "依达方", "PDUFA", "HARMONi"],
    "updated": "2026-11-11",
    "status": "FDA 已于 2026-01-29 受理 BLA，PDUFA 2026-11-14。截至 2026-11-10，所查未见 CRL、延期或咨询会披露。",
    "summary": "依沃西（AK112 / ivonescimab / SMT112，商品名依达方）递交美国上市的依据，是 Summit 申办的全球 III 期 HARMONi，不是中国的 HARMONi-A，也不是一线头对头 K药的适应症。PFS 显著；主分析 OS 未达显著。FDA 书面指出，该适应症获批需要统计学显著的 OS，本研究的 PFS 可能不足以支持上市。之后几次 OS 更新给出的是名义 p 值，不能替代预设检验。",
    "timeline": [
        {
            "date": "2025-04",
            "title": "主分析：PFS 显著，OS 未达显著",
            "grades": ["一手"],
            "body": "HARMONi（NCT06396065）与中国 HARMONi-A 共用方案号 AK112-301，但是独立研究。见刊论文入组 438 例（每组 219）。ClinicalTrials.gov 截至 2026-07-28 更新仍登记实际入组 420 例，以论文为准。（更正日期 2026-11-11：此前两套口径并列；本次打开 Lancet Oncol 2026;27(9):1094-1109，PMID 42636833，确认随机入组 438 例。）\n\nPFS：中位随访 22.3 个月，中位 PFS 6.8 对 4.4 个月，HR 0.52（0.41–0.66），p<0.0001。主分析 OS：中位 OS 16.8 对 14.0 个月，HR 0.79（0.62–1.01），p=0.057，未达显著。Summit 自 2025-05-30 起多次在公司新闻稿中写出该 p 值；2025-09-07 公司稿并写明统计计划要求主分析显著界值为 p=0.0448。Lancet Oncol 论文摘要未写 p 值。Summit 2026-11-04 三季报仍称 a positive trend without achieving a statistically significant result。（更正日期 2026-11-11：此前因未打开 8-K 而撤下 p=0.057；2026-11-11 续核打开 Summit 2025-09-07、2026-07-22 公司稿及 2026-09-15 8-K EX-99.1，均重申主分析 p=0.057，现按公司来源和日期恢复。）\n\n严重 TRAE 28%（61/218）对 15%（33/218）；TRAE 导致死亡 4 例对 5 例。",
            "sources": [
                {"label": "Lancet Oncology（PFS）", "grade": "一手"},
                {"label": "主分析 OS（2025-04 截止）", "grade": "一手"},
                {"label": "Lancet Oncol 2026;27(9):1094-1109，PMID 42636833", "url": "https://pubmed.ncbi.nlm.nih.gov/42636833/", "grade": "一手"},
                {"label": "Summit 公司新闻 2025-09-07（重申主分析 OS p=0.057，并写明界值 p=0.0448）", "url": "https://www.smmttx.com/news/press-releases/news-details/2025/Longer-Term-Follow-Up-of-Western-Patients-Showed-Improving-Favorable-Trend-in-Overall-Survival-in-Global-Phase-III-HARMONi-Clinical-Trial-for-Ivonescimab-Plus-Chemotherapy-in-2L-EGFRm-NSCLC/default.aspx", "grade": "一手"}
            ]
        },
        {
            "date": "2026-01-29",
            "title": "FDA 受理 BLA，PDUFA 定为 2026-11-14",
            "grades": ["一手"],
            "body": "2025 年第四季度递交 BLA，2026-01-29 受理，此前已获 Fast Track。适应症：依沃西联合化疗，用于 EGFR 突变非鳞 NSCLC、三代 TKI 治疗之后。Summit 自称美国每年符合条件的患者在 1.4 万人以上。",
            "sources": [
                {"label": "Summit BLA 受理新闻稿", "url": "https://smmttx.com/news/press-releases/news-details/2026/Summit-Therapeutics-Announces-U-S--FDA-Acceptance-of-Biologics-License-Application-BLA-Seeking-Approval-for-Ivonescimab-in-Combination-with-Chemotherapy-in-Treatment-of-Patients-with-EGFRm-NSCLC-Post-TKI-Therapy/default.aspx", "grade": "一手"}
            ]
        },
        {
            "date": "2026-02-23",
            "title": "10-K 写明 FDA 要求统计学显著的 OS",
            "grades": ["一手"],
            "body": "Summit 2025 财年 10-K 的大意是：FDA 指出该适应症获批需要统计学显著的 OS，本研究的 PFS 可能不足以支持上市。这一约束在 2026 年第三季度新闻稿里再次被重申。",
            "sources": [
                {"label": "Summit 10-K FY2025（2026-02-23）", "grade": "一手"}
            ]
        },
        {
            "date": "2026-09-15",
            "title": "WCLC 更新：ITT 名义显著，西方亚组置信区间仍跨 1",
            "grades": ["一手"],
            "body": "Summit 2026-09-15 的 8-K EX-99.1（与公司官网同日新闻稿为同一份业务更新）给出三次 OS 分析。亚洲患者数据锁定在 2025-04 截点。更新分析已提交 FDA。后续更新的 p 值均为名义 p 值。\n\n全球 ITT（每组 219 例）：2025-04 主分析 HR 0.79（0.62–1.01，p=0.057）；2025-09 HR 0.78（0.62–0.98，名义 p=0.0332）；2026-06 HR 0.76（0.61–0.95，名义 p=0.0151）。三次分析的 ITT 中位 OS 均为 16.8 对 14.0 个月。\n\n西方亚组（83 对 82 例）：HR 分别为 0.98（0.55–1.73）、0.84（0.53–1.32）、0.76（0.52–1.10）；中位随访 9.2、13.7、23.2 个月。公司稿写 2025-04 西方中位 OS 为尚未达到对 14.0 个月，2025-09 为 17.0 对 14.0，2026-06 为 17.5 对 14.0。\n\n（更正日期 2026-11-11：续核打开 Summit 2026-09-15 8-K EX-99.1 与公司官网稿，上表 ITT 与西方亚组数字及主分析 p=0.057 已核对。论文摘要仍未写该 p 值。）",
            "table": {
                "headers": ["数据截止", "ITT HR（95%CI）", "西方亚组 HR（95%CI）", "西方中位随访"],
                "rows": [
                    ["2025-04（主分析）", "0.79（0.62–1.01），p=0.057", "0.98（0.55–1.73）", "9.2 个月"],
                    ["2025-09", "0.78（0.62–0.98），名义 p=0.0332", "0.84（0.53–1.32）", "13.7 个月"],
                    ["2026-06", "0.76（0.61–0.95），名义 p=0.0151", "0.76（0.52–1.10）", "23.2 个月"]
                ]
            },
            "sources": [
                {"label": "Summit 8-K EX-99.1（2026-09-15，WCLC）", "url": "https://www.sec.gov/Archives/edgar/data/1599298/000159929826000081/a2026_prx0915xharmoniltf.htm", "grade": "一手"},
                {"label": "Summit 公司官网同日新闻稿", "url": "https://smmttx.com/news/press-releases/news-details/2026/Updated-HARMONi-Data-Presented-at-WCLC-2026-Demonstrate-Consistent-Overall-Survival-Results-with-Ivonescimab-Plus-Chemotherapy-in-Western-and-Asian-Patients/default.aspx", "grade": "一手"},
                {"label": "Summit 三季报（公司官网，2026-11-04）", "url": "https://smmttx.com/news/press-releases/news-details/2026/Summit-Therapeutics-Reports-Financial-Results-and-Operational-Progress-for-the-Third-Quarter-and-Nine-Months-Ended-September-30-2026/default.aspx", "grade": "一手"}
            ]
        },
        {
            "date": "2026-11-04",
            "title": "三季报再次重申 FDA 的 OS 要求，未提咨询会或延期",
            "grades": ["一手"],
            "body": "Summit 2026 年第三季度新闻稿重申「FDA 指出该适应症获批需要统计学显著的 OS 获益」，并写明 6 月更新的 OS（HR 0.76，名义 p=0.0151）已提交 FDA。稿件未提及咨询委员会或审评延期。截至 2026-11-10，所查 EDGAR 未见 CRL、延期或咨询会披露。",
            "sources": [
                {"label": "Summit 8-K（2026-11-04）", "url": "https://www.sec.gov/Archives/edgar/data/1599298/000159929826000088/smmt-20261104.htm", "grade": "一手"},
                {"label": "Q3 新闻稿", "url": "https://www.sec.gov/Archives/edgar/data/1599298/000159929826000088/a2026_prx1105xq32026earn.htm", "grade": "一手"}
            ]
        }
    ],
    "impact": {
        "text": "这是本季度最大的二元事件。说明书是否以及如何写 OS，决定依沃西以什么身份进入美国。它拿的是 EGFR 突变、TKI 之后的位置，不是一线、也不是对 K药的头对头。\n\n研究组根据 FDA「需要显著 OS」的原话和主分析 OS 未达显著（HR 0.79，0.62–1.01，公司稿 p=0.057，显著界值 p=0.0448）判断：出现 CRL、要求补充数据，或因审评新数据而延期的可能性都不低。这是推论，不是已经发生的监管决定。",
        "attribution": "研究组判断（知识库截至 2026-11-10；其中关于 CRL/延期可能性的表述标为推论，依据为深挖材料对 FDA 原话的解读）"
    }
})

ENTRIES.append({
    "slug": "harmoni-a",
    "title": "HARMONi-A",
    "subtitle": "中国 III 期。EGFR-TKI 治疗进展的 EGFR 突变非鳞 NSCLC，依沃西联合化疗对照安慰剂联合化疗。",
    "kicker": "已获批 · 中国",
    "group": "ivo",
    "priority": 5,
    "companies": ["康方生物"],
    "drugs": ["依沃西"],
    "indications": ["NSCLC"],
    "aliases": ["AK112-301", "NCT05184712", "CTR20213079"],
    "updated": "2026-06-18",
    "status": "已读出最终 OS，并作为 2024-05-24 中国首个获批适应症的依据。",
    "summary": "HARMONi-A（NCT05184712 / CTR20213079）入组 322 人。最终 OS：中位随访 32.5 个月，中位 OS 16.8 对 14.1 个月，分层 HR 0.74（95%CI 0.58–0.95），P=0.02；30 个月 OS 率 29.1% 对 18.4%；3 级及以上 TEAE 67.1% 对 54.7%。全球 HARMONi 研究同一适应症，但是独立试验，OS 结果不能互相替代。",
    "timeline": [
        {
            "date": "2024-05-24",
            "title": "中国获批：EGFR-TKI 后非鳞 NSCLC，联合化疗",
            "grades": ["一手"],
            "body": "这是依沃西在中国的第一个适应症，依据即为 HARMONi-A。2024 年 12 月，该适应症进入国家医保目录。",
            "sources": [
                {"label": "康方新闻 / 港交所自愿公告", "grade": "一手"}
            ]
        },
        {
            "date": "2026-06-18",
            "title": "最终 OS 见刊",
            "grades": ["一手"],
            "body": "中位随访 32.5 个月，中位 OS 16.8 对 14.1 个月，分层 HR 0.74（0.58–0.95），P=0.02；30 个月 OS 率 29.1% 对 18.4%；3 级及以上 TEAE 67.1% 对 54.7%。",
            "sources": [
                {"label": "JAMA 2026;336(4):306-314，PMID 42307937", "url": "https://pubmed.ncbi.nlm.nih.gov/42307937/", "grade": "一手"},
                {"label": "康方新闻 2026-06-18", "grade": "一手"}
            ]
        }
    ],
    "impact": {
        "text": "这是依沃西在中国落地的起点，也是全球 HARMONi 的中国对照镜像。全球申报走的是独立的 HARMONi，不能把这边已经显著的最终 OS 直接说成美国申请的依据。",
        "attribution": "研究组判断"
    }
})

ENTRIES.append({
    "slug": "harmoni-2",
    "title": "HARMONi-2",
    "subtitle": "中国 III 期。一线 PD-L1 阳性（TPS≥1%）NSCLC，依沃西单药对照帕博利珠单抗（K药）单药。",
    "kicker": "头对头 K药 · 已获批",
    "group": "ivo",
    "priority": 3,
    "companies": ["康方生物"],
    "drugs": ["依沃西"],
    "indications": ["NSCLC"],
    "aliases": ["NCT05499390", "CTR20222137", "AK112-303"],
    "updated": "2026-11-11",
    "status": "PFS 期中和预设 OS 期中均为阳性。最终 OS 仍待公布。中国已于 2025-04-25 获批该适应症。",
    "summary": "HARMONi-2（NCT05499390 / CTR20222137）入组 398 人，是依沃西第一条对 K药单药的注册性头对头。PFS 期中：中位 PFS 11.1 对 5.8 个月，HR 0.51（0.38–0.69），单侧 P<0.0001。预设 OS 期中（数据截止 2026-08-20，中位随访 36 个月，OS 事件 234 例，单侧 α=0.0141）：中位 OS 30.8 对 22.6 个月，HR 0.73（0.57–0.95），P=0.009。一手只称「预设期中分析」，不是「第二次期中」。",
    "timeline": [
        {
            "date": "2025-04-25",
            "title": "中国获批一线 PD-L1 阳性 NSCLC 单药",
            "grades": ["一手"],
            "body": "依据 HARMONi-2 对帕博利珠单抗的头对头。2025 年 12 月，该适应症进入医保。",
            "sources": [{"label": "康方新闻 / 港交所自愿公告", "grade": "一手"}]
        },
        {
            "date": "2025",
            "title": "PFS 期中见刊",
            "grades": ["一手"],
            "body": "中位 PFS 11.1 对 5.8 个月，分层 HR 0.51（95%CI 0.38–0.69），单侧 P<0.0001。3 级及以上 TRAE 29%（58 例）对 16%（31 例）。见刊为 Lancet 2025;405:839-849（2025-03-08）。（更正日期 2026-11-11：原文摘要为 11.1 对 5.8 个月，不是 11.14 对 5.82；安全性原文是 grade 3 or higher treatment-related adverse events 58 (29%) vs 31 (16%)，不是「严重 TRAE 29.9% 对 21.6%」。方案号以 ClinicalTrials.gov 的 AK112-303 为准，此前别名误写 AK112-302。）",
            "sources": [
                {"label": "Lancet 2025;405:839-849，PMID 40057343", "url": "https://pubmed.ncbi.nlm.nih.gov/40057343/", "grade": "一手"}
            ]
        },
        {
            "date": "2026-09-14",
            "title": "WCLC / JTO：预设 OS 期中阳性",
            "grades": ["一手"],
            "body": "数据截止 2026-08-20，中位随访 36 个月，OS 事件 234 例；康方 2026-09-13 新闻写明本次按预设 O’Brien-Fleming 消耗函数，单侧 α=0.0141。康方 2026-09-13 与 Summit 2026-09-15 公司稿均写 ITT 中位 OS 30.8 对 22.6 个月；Summit 2026-09-15 还给出 95%CI：25.4–37.8 对 17.8–26.5。HR 0.73（0.57–0.95），P=0.009。2 年 OS 率 57.9% 对 48.0%，3 年 45.0% 对 33.1%（Summit 2026-09-15）。鳞癌亚组 HR 0.65（0.45–0.95），非鳞 HR 0.79（0.55–1.14）；PD-L1 1–49% 亚组 OS HR 0.85（0.61–1.18），PD-L1≥50% HR 0.58（0.38–0.89）。一手只称「预设期中分析」或「protocol-specified interim」，不是「第二次期中」。最终 OS 仍待公布。\n\n（更正日期 2026-11-11：续核打开康方 2026-09-13 新闻与 Summit 2026-09-15 8-K EX-99.1。公司稿用一位小数 30.8 对 22.6 个月；所引 JTO 摘要有报道作 30.75 对 22.57，本次仍未打开 JTO 原文，不以未见原文的两位小数覆盖公司稿。234 例事件与单侧 α=0.0141 已用康方新闻核对；2 年/3 年 OS 率及亚组已用 Summit 2026-09-15 核对。）",
            "sources": [
                {"label": "康方新闻 2026-09-13（HARMONi-2 OS：234 例事件、单侧 α=0.0141、中位 OS 30.8 对 22.6）", "url": "https://www.akesobio.com/cn/media/akeso-news/20260913-1/", "grade": "一手"},
                {"label": "Summit 8-K EX-99.1（2026-09-15）", "url": "https://www.sec.gov/Archives/edgar/data/1599298/000159929826000081/a2026_prx0915xharmoniltf.htm", "grade": "一手"},
                {"label": "Summit 公司官网同日新闻稿（含 2 年/3 年 OS 率与 95%CI）", "url": "https://smmttx.com/news/press-releases/news-details/2026/Updated-HARMONi-Data-Presented-at-WCLC-2026-Demonstrate-Consistent-Overall-Survival-Results-with-Ivonescimab-Plus-Chemotherapy-in-Western-and-Asian-Patients/default.aspx", "grade": "一手"},
                {"label": "JTO 摘要 doi:10.1016/j.jtho.2026.104254（本次仍未打开摘要正文，未看到原文）", "grade": "一手"},
                {"label": "Summit 三季报（公司官网，核对 OS HR 0.73、p=0.009 及「protocol-specified interim」表述）", "url": "https://smmttx.com/news/press-releases/news-details/2026/Summit-Therapeutics-Reports-Financial-Results-and-Operational-Progress-for-the-Third-Quarter-and-Nine-Months-Ended-September-30-2026/default.aspx", "grade": "一手"}
            ]
        }
    ],
    "impact": {
        "text": "这是依沃西已经读出的、对 K药单药的头对头 OS 阳性。优势在鳞癌和高表达人群里更清楚；PD-L1 1–49% 亚组的置信区间跨 1。全球能否坐实对 Keytruda 体系的优势，仍要看 HARMONi-3，不能把中国单药头对头直接外推到全球联合化疗人群。",
        "attribution": "研究组判断"
    }
})

ENTRIES.append({
    "slug": "harmoni-6",
    "title": "HARMONi-6",
    "subtitle": "中国 III 期。一线鳞状 NSCLC，依沃西联合化疗对照替雷利珠单抗联合化疗。",
    "kicker": "头对头替雷利珠 · 已获批",
    "group": "ivo",
    "priority": 4,
    "companies": ["康方生物"],
    "drugs": ["依沃西"],
    "indications": ["NSCLC"],
    "aliases": ["NCT05840016", "CTR20231272"],
    "updated": "2026-11-11",
    "status": "PFS 与首次计划内 OS 均为阳性。中国已于 2026-08-12 获批该适应症。",
    "summary": "HARMONi-6（NCT05840016 / CTR20231272）入组 532 人。PFS 期中：11.1 对 6.9 个月，HR 0.60（0.46–0.78）。路演披露的最终 PFS：12.48 对 8.31 个月，HR 0.72（P=0.003），中位随访 17.02 个月；说明书原文有条目记为未看到，数字来自路演。首次计划内 OS（数据截止 2026-02-27，中位随访 21.4 个月）：中位 OS 27.9 对 23.7 个月，HR 0.66（0.50–0.87），单侧 P=0.0017。",
    "timeline": [
        {
            "date": "2025",
            "title": "PFS 期中见刊",
            "grades": ["一手"],
            "body": "11.1 对 6.9 个月，HR 0.60（0.46–0.78）。",
            "sources": [
                {"label": "Lancet 2025;406:2078-2088，PMID 41125109", "url": "https://pubmed.ncbi.nlm.nih.gov/41125109/", "grade": "一手"}
            ]
        },
        {
            "date": "2026-06",
            "title": "ASCO 全体大会：首次计划内 OS 阳性",
            "grades": ["一手"],
            "body": "数据截止 2026-02-27，中位随访 21.4 个月；有效性边界为单侧 P<0.0049。中位 OS 27.9 对 23.7 个月，HR 0.66（0.50–0.87），单侧 P=0.0017。论文摘要写总生存获益在关键亚组中总体一致，但未给出 PD-L1 分层 HR。康方 2026 年中期路演（2026-08）给出该次 OS 分析的 PD-L1 分层点估计：PD-L1<1% HR 0.64，PD-L1≥1% HR 0.68，以及 TPS 1–49% 0.67、TPS≥50% 0.64；路演未给置信区间。\n\n3 级及以上 TRAE 69% 对 59%，3 级及以上出血 3% 对 1%。\n\n路演还披露了最终 PFS：12.48 对 8.31 个月，HR 0.72（P=0.003），中位随访 17.02 个月。路演注明「2026.8月获批说明书披露」；本次仍未打开国家药监局说明书原文。\n\n（更正日期 2026-11-11：续核打开康方 2026 年中期路演 PDF。论文摘要仍无分层 HR，故把路演点估计按公司来源和日期写入，并与摘要「总体一致」并列。最终 PFS 数字已用该路演核对。）",
            "sources": [
                {"label": "Lancet 2026;407:2620-2629，PMID 42218899", "url": "https://pubmed.ncbi.nlm.nih.gov/42218899/", "grade": "一手"},
                {"label": "康方 2026 年中期路演（2026-08）", "url": "https://akesobio.com/media/7931/akeso%E8%B7%AF%E6%BC%94%E6%9D%90%E6%96%99-2026%E5%B9%B4%E5%8D%8A%E5%B9%B4%E6%8A%A5%E7%BD%91%E7%BB%9C%E7%89%88.pdf", "grade": "一手"}
            ]
        },
        {
            "date": "2026-08-12",
            "title": "中国获批一线鳞状 NSCLC，联合化疗",
            "grades": ["一手", "推论"],
            "body": "依据 HARMONi-6。研究组推断：该适应症获批晚于「2026-06-10 前批准」的医保目录调整窗口，大概率不在 2026 年目录内，最早 2027 年。依沃西和卡度尼利现有协议 2026 年底到期，续约有降价风险。依据是国家医保局 2026-07-14 形式审查名单，依沃西通过条件为「目录内条件 1」（协议到期且不申请调整支付范围）。",
            "sources": [
                {"label": "康方新闻 / 港交所自愿公告", "grade": "一手"}
            ]
        }
    ],
    "impact": {
        "text": "这是依沃西在鳞状 NSCLC 里对另一种已上市 PD-1 联合化疗的头对头 OS 阳性，也是 2026 年 8 月刚拿到的新适应症。它不能代替 HARMONi-3 对 K药联合化疗的全球检验，但给鳞癌队列提供了中国人群的参照。",
        "attribution": "研究组判断；医保时间表部分为推论"
    }
})

ENTRIES.append({
    "slug": "harmoni-3",
    "title": "HARMONi-3",
    "subtitle": "全球一线转移性 NSCLC，依沃西联合化疗对照帕博利珠单抗联合化疗。两个组织学队列分别分析。",
    "kicker": "全球注册主线",
    "group": "ivo",
    "priority": 2,
    "companies": ["康方生物", "Summit"],
    "drugs": ["依沃西"],
    "indications": ["NSCLC"],
    "aliases": ["NCT05899608", "CTR20232457", "SMT112-3003", "AK112-3003"],
    "updated": "2026-11-11",
    "status": "两个队列均已入组完成。鳞癌队列主要 PFS 分析所需事件数预计 2026 年第四季度达到，同时做一次计划内早期 OS 期中分析。这是事件数预计达到，不是数据公布日。",
    "summary": "HARMONi-3（NCT05899608 / CTR20232457，方案号 SMT112-3003 / AK112-3003）计划入组约 1600 例（鳞癌约 600，非鳞约 1000）。两个组织学队列分别进行主要终点 PFS 与 OS 的分析，「如同同一方案下的两项独立研究」。对照是帕博利珠单抗联合化疗，对应 KEYNOTE-189（非鳞）和 KEYNOTE-407（鳞癌）的领地。目前唯一读出是 2026-04-30 鳞癌队列期中 PFS 未达显著。",
    "timeline": [
        {
            "date": "2026-04-30",
            "title": "鳞癌队列期中 PFS 未达显著",
            "grades": ["一手", "二手"],
            "body": "Summit 在 HARMONi-2（PFS HR 0.51）和 HARMONi-6（PFS HR 0.60）都在计划内期中 PFS 获益之后，为鳞癌队列增加了一次期中 PFS 分析，以便更早与监管沟通，并称最初把 PFS 作为主要终点是基于 HARMONi-2。Summit 2026-04-30 一季报原话是：该期中分析「based on the minimal alpha spent」，达到统计学显著的门槛高于计划中的最终 PFS 分析；由独立数据监查委员会（iDMC）审阅后，iDMC 建议研究按原计划继续，未见安全性问题，研究保持双盲。公司未公布该次期中的 HR 或 p 值，也未使用「未达显著」这几个字。研究组根据「更高显著门槛」和 iDMC 建议继续、且公司未宣布阳性的表述，判断该次期中未越过优效界值。这是对原文的解读，不是公司写出的检验结论。股价当日跌幅见二手报道，本站不记录行情。\n\n（更正日期 2026-11-11：续核打开 Summit 2026-04-30 公司一季报。原稿「实际读出未达显著」「当时 OS 尚不成熟，公司称可能无法沟通 OS」中，后一句未在该新闻稿中出现，已删去；前一句改为紧贴公司原话并标为研究组解读。）",
            "sources": [
                {"label": "Summit 第一季度财报新闻稿（2026-04-30）", "url": "https://smmttx.com/news/press-releases/news-details/2026/Summit-Therapeutics-Reports-Financial-Results-and-Operational-Progress-for-the-First-Quarter-Ended-March-31-2026/default.aspx", "grade": "一手"},
                {"label": "Fierce 2026-05-01（期中结果的市场报道）（本次复核未打开该原文，未看到原文）", "grade": "二手"}
            ]
        },
        {
            "date": "2026-07-23",
            "title": "第二季度：按鳞/非鳞分别分析，并给出事件驱动时间表",
            "grades": ["一手"],
            "body": "上季度宣布按鳞癌、非鳞分别分析 PFS 与 OS。已打开的 Summit 2026-07-23 二季报新闻稿（亦即 8-K EX-99.1）写明：「Enrollment in both the squamous and non-squamous NSCLC cohorts of the global HARMONi-3 study is now complete。」鳞癌主要 PFS 事件数预计 2026 年下半年达到，同时做一次计划内早期 OS 期中；独立于 PFS 的鳞癌 OS 期中计划 2027 年上半年；非鳞 PFS 事件数预计 2027 年上半年达到。\n\n原条目还并列过另一组同日口径：10-Q 写鳞癌「2026 年一季度完成入组」、非鳞「2026 年二季度完成入组」；同日电话会则说「已完成鳞状队列筛查，末例受试者将在未来几周内随机入组」，非鳞「仍预计今年下半年完成入组」。这两份 10-Q 和电话会逐字稿本次仍未打开，上述差别予以保留并标注未看到原文；已打开的新闻稿本身写的是两个队列均已入组完成。\n\n事件驱动流程的正确读法是：入组完成之后，等待该队列预设的 PFS 事件数；事件数达到，才做该队列的主要 PFS 分析。ClinicalTrials.gov（2026-10-08 更新）状态为 ACTIVE_NOT_RECRUITING，主要完成估计 2028-12-31。",
            "sources": [
                {"label": "Summit 第二季度财报新闻稿（2026-07-23）", "url": "https://smmttx.com/news/press-releases/news-details/2026/Summit-Therapeutics-Reports-Financial-Results-and-Operational-Progress-for-the-Second-Quarter-and-Six-Months-Ended-June-30-2026/default.aspx", "grade": "一手"},
                {"label": "Summit Q2 10-Q（smmt-20260630.htm）（本次未打开 10-Q 全文，未看到原文）", "url": "https://www.sec.gov/Archives/edgar/data/1599298/000159929826000068/smmt-20260630.htm", "grade": "一手"},
                {"label": "Summit Q2 电话会逐字稿（本次未打开，未看到原文）", "grade": "一手"}
            ]
        },
        {
            "date": "2026-11-04",
            "title": "第三季度：两个队列均已入组完成，鳞癌 PFS 事件数细化到第四季度",
            "grades": ["一手", "未核实"],
            "body": "Q3 8-K 写明两个队列均已入组完成。时间表在第二季度指引上进一步细化：鳞癌主要 PFS 事件数预计 2026 年第四季度达到，同时做一次计划内早期 OS 期中分析；鳞癌独立 OS 期中仍计划 2027 年上半年；非鳞 PFS 事件数预计 2027 年上半年达到。\n\n不可把「事件数达到」写成「读出」，也不可把第三季度更新写成「首次给出时间表」——第二季度已经给出，第三季度是细化到季度。自媒体曾称鳞癌最终 PFS 将在 12 月读出，这一点未核实。BioSpace 11-02 引 Summit「年底前读出」、阿斯利康发言人「海外获批需全球人群 OS 显著改善」，属评论。",
            "sources": [
                {"label": "Summit Q3 8-K / 新闻稿（2026-11-04）", "url": "https://www.sec.gov/Archives/edgar/data/1599298/000159929826000088/a2026_prx1105xq32026earn.htm", "grade": "一手"}
            ]
        }
    ],
    "impact": {
        "text": "HARMONi-3 比 11-14 的 PDUFA 更能决定依沃西的海外天花板。PDUFA 对应的是 EGFR 突变、TKI 之后；HARMONi-3 对应的是 Keytruda 最大的单一适应症。鳞癌期中 PFS 未显著，已经说明全球数据不是单行线。下一步要看的是主要 PFS 分析，以及同期那次早期 OS 期中——OS 当时仍可能不成熟。",
        "attribution": "研究组判断（第 5 期周报，2026-11-09）"
    }
})
