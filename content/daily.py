# -*- coding: utf-8 -*-
from datetime import date, timedelta

START = date(2026, 10, 8)
END = date(2026, 11, 10)

ITEMS = {
    "2026-10-08": [
        {
            "entry": "ivonescimab-trials",
            "headline": "依沃西 II 至 III 期清单完成核实",
            "blurb": "按登记库逐条核对后，II 至 III 期为 136 项，严格口径 134 项；能对上的注册性或 III 期为 16 项，与当时公司口径吻合。此后的增减都并进同一条清单。",
            "grades": ["一手"],
        }
    ],
    "2026-10-09": [
        {
            "entry": "harmoni-10",
            "headline": "CDE 首次公示 HARMONi-10",
            "blurb": "不可切除 III 期 NSCLC 同步放化疗后巩固，依沃西对照度伐利尤单抗。目标入组国内 342 人、国际 830 人（国际为全球总数，含中国）。主要终点为独立评审的无进展生存。",
            "grades": ["一手"],
        },
        {
            "entry": "compassion-40",
            "headline": "康方宣布 COMPASSION-40 开始入组",
            "blurb": "MSI-H / dMMR 结肠癌围手术期 III 期。登记页实际启动日期为 2026-04-15，中报已写上半年启动，更像重新宣传。",
            "grades": ["一手"],
        },
    ],
    "2026-10-12": [
        {
            "entry": "summit-az",
            "headline": "阿斯利康 20 亿美元入股已于 10-05 交割",
            "blurb": "持股约 12.0%，完全稀释约 10.6%，不含依沃西商业权益。配套临床合作包括 Sone-Ve 和 Datroway。",
            "grades": ["一手"],
        },
        {
            "entry": "harmoni-bc1",
            "headline": "康方中文稿确认依沃西联合 Datroway 全球 III 期拟首发一线三阴性乳腺癌",
            "blurb": "合作本身由 Summit、阿斯利康和第一三共于 10-02 宣布。截至后来多次核验，ClinicalTrials.gov 上仍无对应 III 期登记。",
            "grades": ["一手"],
        },
    ],
    "2026-10-13": [
        {
            "entry": "harmoni-gi1",
            "headline": "一线胆道癌 II 期数据发表于《Journal of Hepatology》",
            "blurb": "依沃西联合吉西他滨/顺铂，30 例，ORR 66.7%，DCR 100%，中位 PFS 8.5 个月，中位 OS 16.8 个月。HARMONi-GI1 详细数据当时仍待 ESMO 主席论坛。",
            "grades": ["一手"],
        }
    ],
    "2026-10-16": [
        {
            "entry": "smt112-216",
            "headline": "SMT112-216 在 ClinicalTrials.gov 首次登记",
            "blurb": "NCT07877194，Summit 申办，一线 IMDC 中高危透明细胞肾癌，约 100 人，五组设计。CDE 公示其实早在 9-04，已在清单中。",
            "grades": ["一手"],
        },
        {
            "entry": "ivonescimab-trials",
            "headline": "补记两项中国研究者发起研究",
            "blurb": "ChiCTR2600134037（福建协和，单药新辅助可切除食管鳞癌）和 ChiCTR2600133939（上海东方医院，胸腺癌诱导）。西南肿瘤协作组 Lung-MAP 的 NCT07393555 实际于 9-22 开始，不是当月新登记。",
            "grades": ["一手"],
        },
    ],
    "2026-10-19": [
        {
            "entry": "smt112-216",
            "headline": "Summit 宣布 SMT112-216 全球开中心",
            "blurb": "美中两地。对照是纳武利尤单抗联合伊匹木单抗。康方同日发英文稿。",
            "grades": ["一手"],
        }
    ],
    "2026-10-21": [
        {
            "entry": "ea2251",
            "headline": "Summit 与 ECOG-ACRIN 宣布 EA2251 合作",
            "blurb": "美国一线晚期胆道癌 II/III 期，依沃西联合化疗对照 K药或 I药联合化疗，主要终点总生存，约 336 人。登记页 8-14 已出现，此次是合作宣布。Summit 称开中心预计第四季度，并称 registration-enabling。",
            "grades": ["一手"],
        }
    ],
    "2026-10-22": [
        {
            "entry": "rosetta-breast-01",
            "headline": "BioNTech 拟将 ROSETTA Breast-01 的化疗换成 Trodelvy",
            "blurb": "用于一线 PD-L1 低或阴性三阴性乳腺癌，尚待监管批准。原文是 pumitamig 自身首个全球 III 期 ADC 联合，不是全球首个 PD-(L)1 联合 ADC 的 III 期。",
            "grades": ["一手"],
        },
        {
            "entry": "ivonescimab-esmo-2026",
            "headline": "康方医学公众号预告 ESMO 消化道研究",
            "blurb": "数字当时来自公司稿，次日已对照官方摘要核对。HARMONi-GI1 仍无会上数字。",
            "grades": ["一手"],
        },
    ],
    "2026-10-23": [
        {
            "entry": "ivonescimab-esmo-2026",
            "headline": "ESMO 2026 官方摘要上线，依沃西与卡度尼利早期研究完成逐项核对",
            "blurb": "包括一线低危肾癌 3592O、胸腺癌 iTHYM、食管鳞癌 2908P、二线胃癌 2898P 等。LBA8 当时仍在禁发期。",
            "grades": ["一手"],
        },
        {
            "entry": "harmoni-gi1",
            "headline": "CDE 公示依沃西拟纳入优先审评，列表页未写适应症",
            "blurb": "申请人康方赛诺，申请日 10-20，公示截止 10-30。一线胆道癌的适应症当时只见于二手报道。",
            "grades": ["一手", "二手"],
        },
    ],
    "2026-10-25": [
        {
            "entry": "harmoni-gi1",
            "headline": "HARMONi-GI1 摘要解禁：期中总生存阳性",
            "blurb": "682 人，中位随访 14.3 个月。中位 OS 14.9 对 12.1 个月，HR 0.75（0.61–0.92）；中位 PFS 8.4 对 5.8 个月，HR 0.61。当时未见官方摘要原页，数字来自会议转述。",
            "grades": ["二手"],
        },
        {
            "entry": "sac-tmt",
            "headline": "OptiTROP-Lung06 达到无进展生存终点，同期发表于 NEJM",
            "blurb": "sac-TMT 联合 K药对照化疗联合 K药，一线 PD-L1<1% 非鳞 NSCLC，455 人。独立评审 PFS 15.0 对 5.7 个月，HR 0.49。",
            "grades": ["一手"],
        },
        {
            "entry": "pumitamig",
            "headline": "ROSETTA Lung-107：pumitamig 联合多西他赛的全球 II 期",
            "blurb": "免疫治疗后进展的 NSCLC，50 例，中位随访 12.2 周；30 例可评估，确认 ORR 36.7%，中位 PFS 6.9 个月。",
            "grades": ["一手"],
        },
        {
            "entry": "sone-ve",
            "headline": "CLARITY-Gastric 01：Sone-Ve 单药总生存阳性",
            "blurb": "二线及以后 CLDN18.2 阳性胃癌。意向性治疗人群 OS 10.6 对 6.4 个月，HR 0.58；独立评审 PFS 未达显著。数字来自会议转述。",
            "grades": ["二手"],
        },
        {
            "entry": "domestic-pd1vegf",
            "headline": "基石药业公布 CS2009 的 II 期更新",
            "blurb": "PD-1/VEGF/CTLA-4 三抗。一线 TPS≥50% 单药在更晚截止时整体 ORR 87.5%（21/24），30 mg/kg 组 11/11。早期单臂，无头对头。",
            "grades": ["一手"],
        },
    ],
    "2026-10-26": [
        {
            "entry": "harmoni-gi1",
            "headline": "HARMONi-GI1 会上全文与港交所自愿公告",
            "blurb": "公司稿确认疗效数字，并写明一线胆道癌已被拟纳入优先审评。出血等安全性见公司稿；部分 3/4 级不良事件总率仅见会议报道。",
            "grades": ["一手", "二手"],
        },
        {
            "entry": "ivonescimab-trials",
            "headline": "官网邀请函将口径写作 17 项注册性或 III 期、7 项国际多中心",
            "blurb": "与可核对清单的 17 项一致。同日港交所稿仍写「超过 18 项」。",
            "grades": ["一手"],
        },
        {
            "entry": "ivonescimab-esmo-2026",
            "headline": "iTHYM 胸腺癌会上报告，数字与摘要一致",
            "blurb": "24 例，ORR 83.3%，DCR 100%，已评估的 19 例在 6 个月时均无进展。",
            "grades": ["一手", "二手"],
        },
        {
            "entry": "tivunatamig",
            "headline": "tivunatamig 随机 II 期海报（2660P）",
            "blurb": "对照替雷利珠单抗联合化疗。非鳞确认 ORR 75.0% 对 44.7%；鳞癌 82.5% 对 67.7%。辉瑞已在做全球 III 期，并计划联合恩诺单抗。",
            "grades": ["一手"],
        },
        {
            "entry": "pumitamig",
            "headline": "pumitamig 联合 FOLFIRI 用于二线神经内分泌肿瘤",
            "blurb": "31 例，确认 ORR 40.0%，中位 PFS 5.5 个月，3 级及以上 TRAE 80.6%，治疗相关死亡 1 例。",
            "grades": ["二手"],
        },
    ],
    "2026-10-28": [
        {
            "entry": "pumitamig",
            "headline": "999O 会上更新：pumitamig 联合 Elfe-D",
            "blurb": "安全性 142 例、疗效 139 例，中位随访 6.3 个月，未确认 ORR 48.9%；铂耐药卵巢癌 80.6%（31 例）。3 级及以上 TRAE 38.7%，出现疑似间质性肺病信号。未见公司会后稿。",
            "grades": ["二手"],
        }
    ],
    "2026-11-02": [
        {
            "entry": "adc-hs20093",
            "headline": "补报翰森 NCT07899086：HS-20093 联合依沃西的肺癌 I 期",
            "blurb": "10-27 首次登记，计划 102 人，计划 11-10 开始。这是依沃西首个由公司申办的 B7-H3 ADC 肺癌联用，I 期不计入 II 至 III 期清单。",
            "grades": ["一手"],
        },
        {
            "entry": "adc-sys6043",
            "headline": "康方与石药宣布 SYS6043 联合依沃西的临床合作",
            "blurb": "仅限中国大陆，瘤种和金额未披露，成果共有，由联合指导委员会评估 III 期安排。港交所无单独公告。",
            "grades": ["一手"],
        },
    ],
    "2026-11-03": [
        {
            "entry": "rosetta-breast-01",
            "headline": "BioNTech 三季报再次确认 pumitamig 联合 Trodelvy 的 III 期计划",
            "blurb": "登记页干预当时仍是化疗加安慰剂。原文不能写成全球首个 PD-(L)1 联合 ADC 的 III 期。",
            "grades": ["一手"],
        },
        {
            "entry": "harmoni-gu1",
            "headline": "二手报道称 HARMONi-GU1 已在中国登记",
            "blurb": "称国内 202 人、国际 800 人。CTR 编号与原页未看到。",
            "grades": ["二手"],
        },
        {
            "entry": "domestic-pd1vegf",
            "headline": "二手转载：恒瑞 SHR-4610 新的临床试验申请承办",
            "blurb": "申报联用含多款 ADC，以及联合 HS-20093 用于小细胞肺癌。靶点口径不一。",
            "grades": ["二手"],
        },
    ],
    "2026-11-05": [
        {
            "entry": "harmoni-3",
            "headline": "Summit 三季报细化 HARMONi-3 时间表",
            "blurb": "两个队列均已入组完成。鳞癌主要 PFS 事件数预计 2026 年第四季度达到，同时做一次计划内早期总生存期中分析。事件数达到不等于读出。",
            "grades": ["一手"],
        },
        {
            "entry": "harmoni-fda",
            "headline": "三季报重申 FDA 要求统计学显著的总生存，PDUFA 仍为 11-14",
            "blurb": "6 月更新的 OS（HR 0.76，名义 p=0.0151）已提交 FDA。未提咨询会或延期。",
            "grades": ["一手"],
        },
        {
            "entry": "harmoni-gi1",
            "headline": "康方宣布一线胆道癌正式获纳入优先审评",
            "blurb": "此前 10-23 为拟纳入公示。未披露审评时限。CDE 原页当时未打开，以公司稿为准。港交所无对应自愿公告。",
            "grades": ["一手", "未核实"],
        },
        {
            "entry": "harmoni-gi3",
            "headline": "HARMONi-GI3 登记页入组目标改为 900 例",
            "blurb": "与 Summit 三季报「计划 900 例、预计 2027 年第三季度完成入组」一致。",
            "grades": ["一手"],
        },
        {
            "entry": "summit-az",
            "headline": "特别股东会通过法定普通股增至 20 亿股",
            "blurb": "用于阿斯利康优先股转换。424B7 是登记转售，不是新发行。交割本身发生在 10-05。",
            "grades": ["一手"],
        },
    ],
    "2026-11-06": [
        {
            "entry": "ivonescimab-perioperative",
            "headline": "康方发布围手术期 II 期《Nature Medicine》中文稿",
            "blurb": "期刊页标注 11-04 发表。完成手术人群与全分析集的病理缓解率不同，并排看 III 期时应用全分析集。属 II 期全文上刊，不是 III 期读出。",
            "grades": ["一手"],
        }
    ],
    "2026-11-09": [
        {
            "entry": "ivonescimab-trials",
            "headline": "试验清单增至 138 项",
            "blurb": "新增 MedSIR 申办的二线肝细胞癌 II 期 NCT07917481。HARMONi-GI3 计划例数由 600 调整为 900 已在 11-05 记入。",
            "grades": ["一手"],
        }
    ],
    "2026-11-10": [
        {
            "entry": "rc148",
            "headline": "补记荣昌 RC118 联合 RC148 的一线胃癌 II/III 期",
            "blurb": "CTR20264047，对照替雷利珠单抗联合化疗，用于 CLDN18.2 阳性、HER2 阴性的胃或胃食管结合部腺癌，国内计划 160 例，尚未招募。公示其实是 11-03，原页未核。翰森 NCT07899086 计划今日开始，查登记库仍尚未招募。",
            "grades": ["二手"],
        }
    ],
}

NOTES = {
    "2026-10-08": "追踪窗口的起点。此后同一条试验的进展都并进原条目，不再按日期另立门户。",
    "2026-10-10": "本日无新增重大临床动态。",
    "2026-10-11": "本日无新增重大临床动态。",
    "2026-10-14": "本日无新增重大临床动态。康方当日有配售公告，属融资事项，不写入本站。",
    "2026-10-15": "本日无新增重大临床动态。",
    "2026-10-17": "SMT112-216 的入选标准和对照写法在当天做了核对，详情已并进该条目。未出现新的监管决定或 III 期读出。",
    "2026-10-18": "本日无新增重大临床动态。",
    "2026-10-20": "本日无新增重大临床动态。SMT112-216 开中心已于昨日记录。",
    "2026-10-24": "ESMO 会期第一天，LBA 级数据当时尚未解禁。Summit 与 Lunit 的研究协议不含临床疗效数据，不单独成条。",
    "2026-10-27": "本日无新增重大临床动态。HARMONi-GI1 和竞品读出已在 10-25、10-26 记入对应条目。",
    "2026-10-29": "本日无新增重大临床动态。",
    "2026-10-30": "CDE 优先审评公示截止日。当时尚未见到正式纳入公告。",
    "2026-10-31": "本日无新增重大临床动态。正式纳入优先审评当时仍未见。",
    "2026-11-01": "本日无新增重大临床动态。",
    "2026-11-04": "Summit 于美东 11-04 发布第三季度报告，北京时间已记入 11-05。本日港交所无康方经营公告。",
    "2026-11-07": "本日无新增重大临床动态。围手术期 II 期全文已于昨日记入。FDA PDUFA 仍为 11-14，所查未见 CRL、延期或咨询会。",
    "2026-11-08": "本日无新增重大临床动态。PDUFA 仍为 11-14。",
}

TITLES = {
    "2026-10-08": "清单基线核实完成",
    "2026-10-09": "HARMONi-10 公示，COMPASSION-40 宣布入组",
    "2026-10-12": "阿斯利康入股交割与 Datroway 联用确认",
    "2026-10-13": "胆道癌 II 期见刊",
    "2026-10-16": "肾癌 II 期登记，补记研究者发起研究",
    "2026-10-19": "SMT112-216 宣布开中心",
    "2026-10-21": "EA2251 合作宣布",
    "2026-10-22": "ROSETTA Breast-01 拟换 Trodelvy",
    "2026-10-23": "ESMO 官方摘要核对，优先审评拟纳入公示",
    "2026-10-25": "HARMONi-GI1 与多项竞品在 ESMO 读出",
    "2026-10-26": "胆道癌会上全文、港交所公告与早期研究报告",
    "2026-10-28": "pumitamig 联合 B7-H3 ADC 的会上更新",
    "2026-11-02": "两个 B7-H3 ADC 联用：翰森补报，石药新合作",
    "2026-11-03": "pumitamig 联合 ADC 的 III 期计划再获确认",
    "2026-11-05": "Summit 三季报与胆道癌优先审评正式纳入",
    "2026-11-06": "围手术期 II 期全文的中文稿",
    "2026-11-09": "试验清单增至 138 项",
    "2026-11-10": "荣昌双抗联合 ADC 进入一线胃癌（补记）",
}


def all_days():
    days = []
    d = START
    while d <= END:
        iso = d.isoformat()
        items = ITEMS.get(iso, [])
        title = TITLES.get(iso)
        if not title:
            title = "无新增重大临床动态" if not items else "临床动态"
        note = NOTES.get(iso, "")
        if not items and not note:
            note = "本日无新增重大临床动态。所查未见新的监管决定、III 期读出或新的大型 ADC 合作。"
        days.append({"date": iso, "title": title, "items": items, "note": note})
        d += timedelta(days=1)
    return days
