#!/usr/bin/env python3
import sys
import json
import re
from opencc import OpenCC

# 初始化 OpenCC
cc = OpenCC('s2tw')

def s2tw(text):
    """简体转繁体"""
    return cc.convert(text)

data = json.loads(sys.argv[1])

with open('middle-east-tracker-zh-TW.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 更新时间戳
ts = data.get('timestamp', '')
content = re.sub(
    r'最後更新：[^<]+',
    f'最後更新：{ts}',
    content
)

# 2. 更新新闻 (前3条)
if 'news' in data and data['news']:
    news_items = data['news'][:3]
    new_news = '\n'.join([
        f'''                <div class="news-card">
                    <span class="news-source">{s2tw(n['source'])}</span>
                    <span class="news-date">{n['date']}</span>
                    <div class="news-title">{s2tw(n['title'])}</div>
                    <div class="news-description">{s2tw(n.get('desc',''))}</div>
                </div>'''
        for n in news_items
    ])
    content = re.sub(
        r'(<div class="news-grid">)(.*?)(</div>\s*</section>)',
        f'\\1\n{new_news}\n            \\3',
        content, flags=re.DOTALL, count=1
    )

# 3. 更新市场数据
if 'market' in data:
    m = data['market']
    if 'gold' in m:
        content = re.sub(
            r'(gold-card">\s*<div class="market-value">)[^<]+',
            f'\\1{s2tw(m["gold"])}',
            content, count=1, flags=re.DOTALL
        )
    if 'oil_wti' in m:
        content = re.sub(
            r'(wti-card">\s*<div class="market-value">)[^<]+',
            f'\\1{s2tw(m["oil_wti"])}',
            content, count=1, flags=re.DOTALL
        )
    if 'oil_brent' in m:
        content = re.sub(
            r'(brent-card">\s*<div class="market-value">)[^<]+',
            f'\\1{s2tw(m["oil_brent"])}',
            content, count=1, flags=re.DOTALL
        )

with open('middle-east-tracker-zh-TW.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✅ HTML 已更新：{ts}")
print("✅ 已转换为繁体中文")
