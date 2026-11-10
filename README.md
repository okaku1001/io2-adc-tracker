# IO2.0+ADC 临床追踪

公开的静态站点，记录 IO2.0（以 PD-(L)1×VEGF 双抗为代表）和 ADC2.0 组合的核心临床变动。中心是康方生物的依沃西（AK112 / ivonescimab / SMT112，商品名依达方）与卡度尼利（AK104，商品名开坦尼），以及它们的授权伙伴、联用药和直接竞品。

站点地址：<https://okaku1001.github.io/io2-adc-tracker/>

同一条试验、同一个药、同一件监管事项只保留一个条目。新进展并进原条目的时间线。每日动态页只作索引。

本站为公开信息整理，不构成投资建议。

## 本地生成

```bash
python3 content/make_data.py   # 若改了 content/*.py
python3 build.py               # 读取 data/entries.json 与 data/daily/*.json，写出 HTML
```

更新办法见 [UPDATE.md](UPDATE.md)。
