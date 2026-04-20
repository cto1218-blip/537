# Cron 任务更新模板（最终版）

## 关键要求

### 1. 新闻必须是过去24小时内
**搜索关键词必须包含**：
- `latest news today yesterday`
- `April 16 2026` （当天日期）
- `breaking news past 24 hours`

### 2. 完整指令模板

```
中东局势更新任务：

1. **搜索最新24小时新闻**：
   web_search('Israel Gaza war latest news today April HH 2026 past 24 hours')
   
2. **搜索市场数据**：
   - 金价：web_search('gold spot price today USD per ounce real-time April HH 2026')
   - 油价：web_search('WTI Brent crude oil price today April HH 2026')

3. **构建JSON**：
   - timestamp: "2026年4月HH日 HH:00" （**必须中文格式**）
   - news数组：**日期必须是2026-04-HH或2026-04-(HH-1)**（今天或昨天）
   - 每条新闻必须有 title + desc（150-250字完整描述）+ date + source
   - market.gold, market.oil_wti, market.oil_brent: 真实价格

4. **写入并执行**：
   - echo '<JSON>' > /tmp/middle-east-data.json
   - cd ~/.openclaw/workspace && /usr/bin/python3 update-middle-east.py "$(cat /tmp/middle-east-data.json | tr -d '\n')"
   - git add middle-east-tracker-zh-TW.html && git commit -m "中东局势更新 2026-04-HH HH:00" && git push -f origin main

直接执行，简短报告即可。
```

## 关键改进点

### ❌ 旧版问题
- 搜索关键词太泛化：`Israel Gaza war latest news`
- 没有指定日期，可能搜到几天前的新闻
- JSON 中的 date 字段没有验证要求

### ✅ 新版改进
- 搜索关键词包含具体日期：`April 16 2026 past 24 hours`
- 明确要求新闻日期必须是今天或昨天
- 增加 `breaking news` 关键词提高时效性

---
更新时间：2026-04-16 17:35 UTC+8
