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
    "updated": "2026-11-05",
    "status": "FDA 已于 2026-01-29 受理 BLA，PDUFA 2026-11-14。截至 2026-11-10，所查未见 CRL、延期或咨询会披露。",
    "summary": "依沃西（AK112 / ivonescimab / SMT112，商品名依达方）递交美国上市的依据，是 Summit 申办的全球 III 期 HARMONi，不是中国的 HARMONi-A，也不是一线头对头 K药的适应症。PFS 显著；主分析 OS 未达显著。FDA 书面指出，该适应症获批需要统计学显著的 OS，本研究的 PFS 可能不足以支持上市。之后几次 OS 更新给出的是名义 p 值，不能替代预设检验。",
    "timeline": [
        {
            "date": "2025-04",
            "title": "主分析：PFS 显著，OS 未达显著",
            "grades": ["一手"],
            "body": "HARMONi（NCT06396065）与中国 HARMONi-A 共用方案号 AK112-301，但是独立研究。入组人数有两套并列口径：深挖材料记 n=438，试验清单按登记页记 n=420，引用时以最新登记页或论文为准。\n\nPFS：中位随访 22.3 个月，中位 PFS 6.8 对 4.4 个月，HR 0.52（0.41–0.66），p<0.0001。主分析 OS（数据截止 2025-04）：中位 OS 16.8 对 14.0 个月，HR 0.79（0.62–1.01），p=0.057，未达显著。严重 TRAE 28%（61/218）对 15%（33/218）；TRAE 导致死亡 4 例对 5 例。",
            "sources": [
                {"label": "Lancet Oncology（PFS）", "grade": "一手"},
                {"label": "主分析 OS（2025-04 截止）", "grade": "一手"}
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
            "body": "Summit 8-K 附件给出三次 OS 分析。亚洲患者数据仍锁定在 2025-04 截点。更新分析已提交 FDA。后续更新的 p 值均为名义 p 值。",
            "table": {
                "headers": ["数据截止", "ITT HR（95%CI）", "西方亚组 HR（95%CI）", "西方中位随访"],
                "rows": [
                    ["2025-04（主分析）", "0.79（0.62–1.01），p=0.057", "0.98（0.55–1.73）", "9.2 个月"],
                    ["2025-09", "0.78（0.62–0.98），名义 p=0.0332", "0.84（0.53–1.32）", "13.7 个月"],
                    ["2026-06", "0.76（0.61–0.95），名义 p=0.0151", "0.76（0.52–1.10）", "23.2 个月"]
                ]
            },
            "sources": [
                {"label": "Summit 8-K EX-99.1（2026-09-15，WCLC）", "grade": "一手"}
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
        "text": "这是本季度最大的二元事件。说明书是否以及如何写 OS，决定依沃西以什么身份进入美国。它拿的是 EGFR 突变、TKI 之后的位置，不是一线、也不是对 K药的头对头。\n\n研究组根据 FDA「需要显著 OS」的原话和主分析 p=0.057 判断：出现 CRL、要求补充数据，或因审评新数据而延期的可能性都不低。这是推论，不是已经发生的监管决定。",
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
                {"label": "JAMA 2026;336(4):306-314，PMID 42307937", "grade": "一手"},
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
    "aliases": ["NCT05499390", "CTR20222137", "AK112-302"],
    "updated": "2026-09-14",
    "status": "PFS 期中和预设 OS 期中均为阳性。最终 OS 仍待公布。中国已于 2025-04-25 获批该适应症。",
    "summary": "HARMONi-2（NCT05499390 / CTR20222137）入组 398 人，是依沃西第一条对 K药单药的注册性头对头。PFS 期中：中位 PFS 11.14 对 5.82 个月，HR 0.51（P<0.0001）。预设 OS 期中（数据截止 2026-08-20，中位随访 36 个月，OS 事件 234 例，单侧 α=0.0141）：中位 OS 30.75 对 22.57 个月，HR 0.73（0.57–0.95），P=0.009。一手只称「预设期中分析」，不是「第二次期中」。",
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
            "body": "中位 PFS 11.14 对 5.82 个月，HR 0.51（P<0.0001）。严重 TRAE 29.9% 对 21.6%。见刊年份为 2025，具体月份以 Lancet 论文为准。",
            "sources": [
                {"label": "Lancet 2025;405:839-849，PMID 40057343", "grade": "一手"}
            ]
        },
        {
            "date": "2026-09-14",
            "title": "WCLC / JTO：预设 OS 期中阳性",
            "grades": ["一手"],
            "body": "数据截止 2026-08-20，中位随访 36 个月，OS 事件 234 例，单侧 α=0.0141。中位 OS 30.75 对 22.57 个月（有的基线报告四舍五入写成 30.8 对 22.6，引用推荐带一位小数的原文）。HR 0.73（0.57–0.95），P=0.009。2 年 OS 率 57.9% 对 48.0%，3 年 45.0% 对 33.1%。鳞癌亚组 HR 0.65（0.45–0.95），非鳞 HR 0.79（0.55–1.14）；PD-L1 1–49% 亚组 OS HR 0.85（0.61–1.18）。最终 OS 仍待公布。",
            "sources": [
                {"label": "JTO 摘要 doi:10.1016/j.jtho.2026.104254", "grade": "一手"},
                {"label": "Summit 8-K 2026-09-14", "grade": "一手"}
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
    "updated": "2026-08-12",
    "status": "PFS 与首次计划内 OS 均为阳性。中国已于 2026-08-12 获批该适应症。",
    "summary": "HARMONi-6（NCT05840016 / CTR20231272）入组 532 人。PFS 期中：11.1 对 6.9 个月，HR 0.60（0.46–0.78）。路演披露的最终 PFS：12.48 对 8.31 个月，HR 0.72（P=0.003），中位随访 17.02 个月；说明书原文有条目记为未看到，数字来自路演。首次计划内 OS（数据截止 2026-02-27，中位随访 21.4 个月）：中位 OS 27.9 对 23.7 个月，HR 0.66（0.50–0.87），单侧 P=0.0017。",
    "timeline": [
        {
            "date": "2025",
            "title": "PFS 期中见刊",
            "grades": ["一手"],
            "body": "11.1 对 6.9 个月，HR 0.60（0.46–0.78）。",
            "sources": [
                {"label": "Lancet 2025;406:2078-2088，PMID 41125109", "grade": "一手"}
            ]
        },
        {
            "date": "2026-06",
            "title": "ASCO 全体大会：首次计划内 OS 阳性",
            "grades": ["一手"],
            "body": "数据截止 2026-02-27，中位随访 21.4 个月；有效性边界为单侧 P<0.0049。中位 OS 27.9 对 23.7 个月，HR 0.66（0.50–0.87），单侧 P=0.0017。PD-L1<1% 的 HR 0.64（0.43–0.96），PD-L1≥1% 的 HR 0.68（0.46–0.99）。3 级及以上 TRAE 69% 对 59%，3 级及以上出血 3% 对 1%。\n\n路演还披露了最终 PFS：12.48 对 8.31 个月，HR 0.72（P=0.003），中位随访 17.02 个月。说明书原文未看到，数字来自康方 2026 年中期路演第 14 页。",
            "sources": [
                {"label": "Lancet 2026;407:2620-2629，PMID 42218899", "grade": "一手"},
                {"label": "康方 2026H1 路演 p.14（最终 PFS）", "grade": "一手"}
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
    "updated": "2026-11-05",
    "status": "两个队列均已入组完成。鳞癌队列主要 PFS 分析所需事件数预计 2026 年第四季度达到，同时做一次计划内早期 OS 期中分析。这是事件数预计达到，不是数据公布日。",
    "summary": "HARMONi-3（NCT05899608 / CTR20232457，方案号 SMT112-3003 / AK112-3003）计划入组约 1600 例（鳞癌约 600，非鳞约 1000）。两个组织学队列分别进行主要终点 PFS 与 OS 的分析，「如同同一方案下的两项独立研究」。对照是帕博利珠单抗联合化疗，对应 KEYNOTE-189（非鳞）和 KEYNOTE-407（鳞癌）的领地。目前唯一读出是 2026-04-30 鳞癌队列期中 PFS 未达显著。",
    "timeline": [
        {
            "date": "2026-04-30",
            "title": "鳞癌队列期中 PFS 未达显著",
            "grades": ["一手", "二手"],
            "body": "Summit 在 HARMONi-2（PFS HR 0.51）和 HARMONi-6（PFS HR 0.60）都在计划内期中 PFS 获益之后，为鳞癌队列增加了一次期中 PFS 分析，以便更早与监管沟通，并称最初把 PFS 作为主要终点是基于 HARMONi-2。公司称该期中分析分配了「minimal alpha」（第一季度财报原话）。实际读出未达显著。当时 OS 尚不成熟，公司称可能无法沟通 OS。股价当日跌幅见二手报道，本站不记录行情。",
            "sources": [
                {"label": "Summit 第一季度财报（minimal alpha）", "grade": "一手"},
                {"label": "Fierce 2026-05-01（期中结果的市场报道）", "grade": "二手"}
            ]
        },
        {
            "date": "2026-07-23",
            "title": "第二季度：按鳞/非鳞分别分析，并给出事件驱动时间表",
            "grades": ["一手"],
            "body": "上季度宣布按鳞癌、非鳞分别分析 PFS 与 OS。入组口径在同一天的文件里不完全一致，需要并列：10-Q / 8-K 写鳞癌「2026 年一季度完成入组」、非鳞「2026 年二季度完成入组」；同日电话会则说「已完成鳞状队列筛查，末例受试者将在未来几周内随机入组」，非鳞「仍预计今年下半年完成入组」。公司未在后续文件里解释这一字面差别。\n\n事件驱动流程的正确读法是：入组完成之后，等待该队列预设的 PFS 事件数；事件数达到，才做该队列的主要 PFS 分析。鳞癌队列在同一时点还安排一次计划内早期 OS 期中分析。第二季度指引：鳞癌主要 PFS 事件数预计 2026 年下半年达到；独立于 PFS 的鳞癌 OS 期中计划在 2027 年上半年；非鳞 PFS 事件数预计 2027 年上半年达到。ClinicalTrials.gov（2026-10-08 更新）状态为 ACTIVE_NOT_RECRUITING，主要完成估计 2028-12-31。",
            "sources": [
                {"label": "Summit Q2 10-Q / 8-K（2026-07-23）", "grade": "一手"},
                {"label": "Summit Q2 电话会", "grade": "一手"}
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
