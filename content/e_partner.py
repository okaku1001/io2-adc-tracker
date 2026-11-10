# -*- coding: utf-8 -*-
ENTRIES = []

ENTRIES.append({
    "slug": "summit-az",
    "title": "Summit 授权与阿斯利康入股",
    "subtitle": "依沃西的海外权益在 Summit。阿斯利康 20 亿美元入股不含依沃西的商业权益。",
    "kicker": "授权与股权",
    "group": "partner",
    "priority": 17,
    "companies": ["康方生物", "Summit", "阿斯利康"],
    "drugs": ["依沃西"],
    "indications": ["多瘤种"],
    "aliases": ["SMMT", "Akeso Collaboration"],
    "updated": "2026-11-04",
    "status": "2022 年 12 月完成授权。阿斯利康投资于 2026-10-05 交割。",
    "summary": "目前已知的跨国合作几乎都是各自供药、分担费用、各自保留权益的临床合作。没有任何一家获得依沃西的商业权益，阿斯利康入股 Summit 也不含依沃西权益。ADC 一方可以随时换伙伴。交易对价有两套口径，必须并列，以 10-K 为一手。",
    "timeline": [
        {
            "date": "2022-12-08",
            "title": "康方将美欧日等海外权益授给 Summit",
            "grades": ["一手"],
            "body": "常用口径：首付 5 亿美元，总额最高 50 亿美元，外加两位数提成。Summit 2025 财年 10-K（2026-02-23）写的是：首期对价合计 5.15 亿美元（2023 年第一季度支付 5.00 亿，其中现金 4.749 亿、1000 万股 Summit 股票抵 2510 万美元；2024 年第三季度因区域扩至拉美、中东、非洲再付 1500 万）；或有付款最高 45.6 亿美元（监管里程碑 10.5 亿、商业 35.1 亿）；提成为低两位数。权益区域：北美、南美、欧洲、中东、非洲和日本。中国等区域仍归康方。",
            "sources": [
                {"label": "Summit 2022-12 新闻稿", "url": "https://www.sec.gov/Archives/edgar/data/1599298/000159929822000136/a2022_prx1208xivonescimaba.htm", "grade": "一手"},
                {"label": "Summit 10-K FY2025 Item 1", "grade": "一手"}
            ]
        },
        {
            "date": "2026-09-28",
            "title": "阿斯利康签约认购 20 亿美元可转换优先股",
            "grades": ["一手"],
            "body": "2026-10-05 完成交割。折合每股 18.3561 美元，约 1.09 亿股（最多 108955369 股，见 424B7）。持股约 12.0%，完全稀释约 10.6%。不含依沃西的任何商业权益。阿斯利康获优先认购权，以及第三方收购时的特定权利。配套临床合作包括：Sone-Ve（消化道，阿斯利康主导，共担费用、各自保留权益，谅解备忘录拟扩大到更多抗肿瘤药或 ADC）；Datroway（与第一三共，首发一线三阴性乳腺癌 III 期）。到账是 10-05 的事件，不是 11 月第一周的新事件。",
            "sources": [
                {"label": "Summit：阿斯利康完成 20 亿美元股权投资", "url": "https://smmttx.com/news/press-releases/news-details/2026/AstraZeneca-Completes-2-Billion-Equity-Investment-in-Summit-Therapeutics/default.aspx", "grade": "一手"}
            ]
        },
        {
            "date": "2026-11-04",
            "title": "特别股东会通过法定普通股由 10 亿股增至 20 亿股",
            "grades": ["一手"],
            "body": "赞成 658142561 票，反对 1983511 票，弃权 3134826 票，用于阿斯利康优先股转换。同日的 424B7 是阿斯利康控股公司登记转售，不是新发行。",
            "sources": [
                {"label": "Summit 8-K 2026-11-04", "url": "https://www.sec.gov/Archives/edgar/data/1599298/000159929826000088/smmt-20261104.htm", "grade": "一手"}
            ]
        }
    ],
    "impact": {
        "text": "阿斯利康愿意出资，并把手上的 ADC 拿来和依沃西联用，是对依沃西作为公共骨架的加分；但它同时在推进自己的 rilvegostomig 联合 ADC，是两条骨架一起下注。海外经济利益主要归 Summit，康方拿里程碑和低两位数提成。",
        "attribution": "研究组判断"
    }
})

ENTRIES.append({
    "slug": "adc-hs20093",
    "title": "依沃西联合 HS-20093 / GSK'227",
    "subtitle": "翰森与 GSK 的 B7-H3 ADC。这是依沃西首个由公司申办的 B7-H3 ADC 肺癌联用，目前还在 I 期。",
    "kicker": "双抗 + ADC",
    "group": "partner",
    "priority": 12,
    "companies": ["康方生物", "翰森制药", "GSK"],
    "drugs": ["依沃西", "HS-20093"],
    "indications": ["NSCLC"],
    "aliases": ["NCT07899086", "GSK5764227", "risvutatug rezetecan", "GSK'227"],
    "updated": "2026-11-10",
    "status": "翰森申办的 NCT07899086 计划 2026-11-10 开始，截至 2026-11-10 仍尚未招募，最后更新 2026-10-27。I 期不计入依沃西 II 至 III 期清单。",
    "summary": "HS-20093 即 GSK'227（risvutatug rezetecan，GSK5764227），靶点是 B7-H3。存在两条联用路径：Summit 与 GSK 的非独家 I/II 期，以及翰森在中国申办的 I 期。翰森同时把 HS-20093 与恒瑞 SHR-4610 做跨公司联用申报（小细胞肺癌），两边都在押。",
    "timeline": [
        {
            "date": "2026-09-09",
            "title": "Summit 与 GSK 的非独家 I/II 期开始",
            "grades": ["一手"],
            "body": "登记号 NCT07602855。",
            "sources": [
                {"label": "NCT07602855", "url": "https://clinicaltrials.gov/study/NCT07602855", "grade": "一手"}
            ]
        },
        {
            "date": "2026-10-27",
            "title": "翰森申办 NCT07899086 首次登记",
            "grades": ["一手"],
            "body": "HS-20093 联合依沃西 20 mg/kg，可加或不加培美曲塞 / 白蛋白紫杉醇，用于晚期 NSCLC，I 期，非随机，计划 102 人。计划开始日期 2026-11-10。前几次日检曾漏记此项，第 4 期周报补报。GSK 自身的 III 期包括 EMBOLD（复发小细胞肺癌，NCT07099898）和转移性去势抵抗性前列腺癌（NCT07802704）等。",
            "sources": [
                {"label": "NCT07899086", "url": "https://clinicaltrials.gov/study/NCT07899086", "grade": "一手"}
            ]
        },
        {
            "date": "2026-11-10",
            "title": "计划开始日当天，登记状态仍为尚未招募",
            "grades": ["一手"],
            "body": "最后更新仍是 2026-10-27，估计开始日仍写 2026-11-10。",
            "sources": [
                {"label": "NCT07899086", "url": "https://clinicaltrials.gov/study/NCT07899086", "grade": "一手"}
            ]
        }
    ],
    "impact": {
        "text": "小幅加分：依沃西的 B7-H3 ADC 伙伴在扩容，但现在仍是 I 期，没有疗效数据。翰森同时把同一款 ADC 拿去和恒瑞的 PD-(L)1×VEGF 资产申报联用，说明供药方并未单押依沃西。",
        "attribution": "研究组判断（第 4 期周报）"
    }
})

ENTRIES.append({
    "slug": "adc-sys6043",
    "title": "依沃西联合 SYS6043",
    "subtitle": "与石药集团旗下巨石生物的临床合作。仅限中国大陆，瘤种未公开。",
    "kicker": "双抗 + ADC",
    "group": "partner",
    "priority": 12,
    "companies": ["康方生物", "石药集团"],
    "drugs": ["依沃西", "SYS6043"],
    "indications": ["未披露"],
    "aliases": ["巨石生物"],
    "updated": "2026-11-03",
    "status": "2026-11-02 宣布合作。未见联用登记，未披露金额和具体瘤种。",
    "summary": "SYS6043 是石药的 B7-H3 ADC。这是依沃西第二个与国内大型药企的 B7-H3 ADC 联用，前一个是翰森的 HS-20093。",
    "timeline": [
        {
            "date": "2026-11-02",
            "title": "康方官网宣布临床研究合作",
            "grades": ["一手"],
            "body": "合作区域为中国大陆，适应症为双方约定的肿瘤，具体瘤种未公开。研究成果双方共有；III 期如何安排，由联合指导委员会结合数据和监管沟通再评估。未披露金额。港交所当天无康方公告，按须披露交易的标准看，此事未单独公告。石药自身的 III 期包括铂耐药卵巢癌 NCT07708753（2026-07 开始，招募中）和一线某瘤种对照研究者选择化疗的 NCT07879911（计划 2026-11-30 开始）。",
            "sources": [
                {"label": "康方官网 2026-11-02", "url": "https://www.akesobio.com/cn/media/akeso-news/20261102/", "grade": "一手"}
            ]
        }
    ],
    "impact": {
        "text": "小幅加分：ADC 联用伙伴继续扩容，但仅限中国，也还没有登记和数据。",
        "attribution": "研究组判断（2026-11-03 日检）"
    }
})

ENTRIES.append({
    "slug": "sone-ve",
    "title": "Sone-Ve 与 CLARITY-Gastric 01",
    "subtitle": "阿斯利康的 CLDN18.2 ADC，是依沃西消化道联用的伙伴药。单药 III 期已有总生存获益。",
    "kicker": "伙伴药",
    "group": "partner",
    "priority": 19,
    "companies": ["阿斯利康", "Summit"],
    "drugs": ["Sone-Ve", "依沃西"],
    "indications": ["胃癌"],
    "aliases": ["sonesitatug vedotin", "LBA7", "CLARITY-Gastric"],
    "updated": "2026-10-26",
    "status": "与依沃西的临床合作「即将」启动，期别未披露；ClinicalTrials.gov 未见依沃西联用登记。",
    "summary": "Sone-Ve（sonesitatug vedotin）是阿斯利康的 CLDN18.2 ADC。公开合作范围是消化道，未见乳腺癌。伙伴药自己先有总生存获益，给以后的联用打下基础，但与依沃西没有直接数据。",
    "timeline": [
        {
            "date": "2026-10-25",
            "title": "ESMO LBA7：CLARITY-Gastric 01",
            "grades": ["二手"],
            "body": "二线及以后、CLDN18.2 阳性的胃或食管胃癌 III 期，532 人随机，中位随访 8.6 个月。三线及以后人群 OS 10.0 对 5.0 个月，HR 0.47（0.36–0.62）；意向性治疗人群 OS 10.6 对 6.4 个月，HR 0.58（0.47–0.73）。独立评审的 PFS 未达统计学显著。数字来自 Oncoletter 对主席论坛的转述，ESMO 幻灯原页当时未打开。曾有公众号把同场背靠背的研究误写成胰腺癌或胆道癌数据，已更正：与 HARMONi-GI1 同场的就是这项胃癌研究。",
            "sources": [
                {"label": "Oncoletter 转述", "url": "https://www.oncoletter.ch/de/Kongressbericht/2026/esmo-congress-2026/presidential-symposium-ii.html", "grade": "二手"}
            ]
        }
    ],
    "impact": {
        "text": "对依沃西消化道 ADC 联用是加分：伙伴药单药已经做出总生存获益。联用本身还没有登记，更没有数据。",
        "attribution": "研究组判断（2026-10-25 ESMO 跟进）"
    }
})

ENTRIES.append({
    "slug": "akeso-adc",
    "title": "康方自研 ADC",
    "subtitle": "AK146D1（TROP2/Nectin-4 双抗 ADC）和 AK138D1（HER3 ADC）已与依沃西联用进入早期临床。",
    "kicker": "自研管线",
    "group": "partner",
    "priority": 21,
    "companies": ["康方生物"],
    "drugs": ["AK146D1", "AK138D1", "依沃西"],
    "indications": ["NSCLC", "乳腺癌"],
    "aliases": ["AK157D1", "AK158D1"],
    "updated": "2026-10-08",
    "status": "已有首例患者入组的 II 期或 Ib/II 期，尚无随机疗效数据。",
    "summary": "康方把自研 ADC 接到依沃西上，是中国市场的闭环，也是对外授权的期权。它们目前都还没有可以拿来讨论疗效的随机数据。",
    "timeline": [
        {
            "date": "2026-06-15",
            "title": "AK138D1 联合或不联合依沃西的乳腺癌 Ib/II 期见诸新闻",
            "grades": ["一手", "未核实"],
            "body": "登记号 NCT07560124，尚未招募（以当时材料为准）。公司称在中国和澳大利亚的早期研究中未见间质性肺病。药物抗体比 8 这一说法来自二手，未核实。",
            "sources": [
                {"label": "NCT07560124", "url": "https://clinicaltrials.gov/study/NCT07560124", "grade": "一手"},
                {"label": "康方新闻 2026-06-15", "url": "https://akesobio.com/cn/media/akeso-news/20260615/", "grade": "一手"}
            ]
        },
        {
            "date": "2026-07-20",
            "title": "AK146D1 联合依沃西的 NSCLC II 期首例患者入组",
            "grades": ["一手"],
            "body": "AK146D1 是 TROP2/Nectin-4 双抗 ADC，连接子为 MC-AAA，载荷为 DXd。乳腺癌 II 期 NCT07591090 的首例患者新闻发于 2026-08-10，实际开始日期为 2026-07-17。",
            "sources": [
                {"label": "NCT07591090", "url": "https://clinicaltrials.gov/study/NCT07591090", "grade": "一手"},
                {"label": "康方新闻 2026-08-10", "url": "https://akesobio.com/cn/media/akeso-news/20260810/", "grade": "一手"}
            ]
        },
        {
            "date": "2026-08",
            "title": "更早的 ADC：AK157D1 与 AK158D1",
            "grades": ["一手"],
            "body": "AK157D1 是 B7-H3 ADC，2026 年 8 月获批 I 期。AK158D1 是 EGFR/TROP2 双抗 ADC，2026 年 7 月递交临床试验申请，9 月获批 I 期的标题已核对。",
            "sources": [{"label": "康方公开披露", "grade": "一手"}]
        }
    ]
})

ENTRIES.append({
    "slug": "adc-other",
    "title": "其他依沃西 ADC 联用",
    "subtitle": "百利 iza-bren、宜联 YL201、安领科 ALK201、荣昌维迪西妥单抗、吉利德戈沙妥珠单抗，以及 2025 年与辉瑞的 vedotin 合作。",
    "kicker": "双抗 + ADC",
    "group": "partner",
    "priority": 22,
    "companies": ["康方生物", "百利天恒", "宜联生物", "荣昌生物", "Gilead"],
    "drugs": ["依沃西", "iza-bren", "YL201", "维迪西妥单抗", "戈沙妥珠单抗"],
    "indications": ["NSCLC", "胃癌"],
    "aliases": ["BL-B01D1", "PANKU-Lung05", "PANKU-Lung06", "NCT07208773", "NCT07393555"],
    "updated": "2026-11-10",
    "status": "多数为早期或尚未招募。尚无依沃西联合 ADC 的公开随机或公司口径疗效数据。",
    "summary": "没有自家 PD-(L)1×VEGF 的 ADC 持有方，会不会把依沃西当成首选联用骨架，是总问题里的一条。下面这些合作说明名单在变长，但不等于数据已经出现。",
    "timeline": [
        {
            "date": "2025-02-24",
            "title": "Summit 与辉瑞宣布多款 vedotin ADC 合作",
            "grades": ["一手", "推论"],
            "body": "ClinicalTrials.gov 上未找到辉瑞申办的依沃西联合辉瑞 ADC 试验。研究组推断，此事已被 tivunatamig 替代或搁置。辉瑞的 sigvotatug vedotin 在 SigVie-002（二线 NSCLC）于 2026-06-22 宣布总生存未达终点。",
            "sources": [{"label": "Summit 2025-02-24 新闻稿", "grade": "一手"}]
        },
        {
            "date": "2026-07-29",
            "title": "安领科 ALK201 联合依沃西",
            "grades": ["一手"],
            "body": "NCT07742956，鳞状 NSCLC II 期，尚未招募。国家药监局已批准临床试验申请。ALK201 为 FGFR2b ADC。",
            "sources": [{"label": "康方新闻 2026-07-29", "grade": "一手"}]
        },
        {
            "date": "2026-09-22",
            "title": "西南肿瘤协作组 Lung-MAP 子研究实际开始",
            "grades": ["一手"],
            "body": "NCT07393555：依沃西可加或不加戈沙妥珠单抗（ Trodelvy），II 期。2026-02-06 首次登记，市场转载称「新登记」并不准确。吉利德同时与 BioNTech 合作 ROSETTA Breast-01（pumitamig 联合 Trodelvy），是在多种骨架之间对冲。",
            "sources": [
                {"label": "NCT07393555", "url": "https://clinicaltrials.gov/study/NCT07393555", "grade": "一手"}
            ]
        },
        {
            "date": "2026-11-10",
            "title": "宜联、百利、荣昌等联用的登记状态",
            "grades": ["一手"],
            "body": "宜联 YL201（B7-H3 ADC）联合依沃西：NCT07208773 / CTR20253697，I/II 期，260 人，招募中。百利天恒 iza-bren（BL-B01D1，EGFR×HER3 双抗 ADC）在中国的 PANKU-Lung05 / Lung06（NCT07739199 / NCT07739186，II/III 期，尚未招募）联合「PD-1/VEGF 双抗」，即依沃西（部分核实）。同一款 ADC 在海外由百时美施贵宝推进，与 pumitamig 联用（NCT06618287）。iza-bren 自身的 PANKU-Lung01 PFS HR 0.40，国内上市申请 10-26 受理。荣昌维迪西妥单抗（RC48）联合依沃西为研究者发起研究 NCT06957561；荣昌另有自家 PD-1×VEGF 双抗 RC148，已授权艾伯维，是直接竞品。",
            "sources": [
                {"label": "NCT07208773", "url": "https://clinicaltrials.gov/study/NCT07208773", "grade": "一手"}
            ]
        }
    ],
    "impact": {
        "text": "名单变长，是加分；但依沃西联合 ADC 至今没有公开的随机或公司口径疗效数据。首个公开的「PD-(L)1×VEGF 双抗联合 ADC」信号属于 pumitamig。有自家双抗的大药企，没有经济理由把骨架让给依沃西。",
        "attribution": "研究组判断"
    }
})
