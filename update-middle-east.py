#!/usr/bin/env python3
import sys
import json
import re
from opencc import OpenCC

# 初始化 OpenCC（简体转繁体）
cc = OpenCC('s2tw')

def s2tw(text):
    """简体转繁体"""
    return cc.convert(text)

# 读取命令行参数的 JSON
data = json.loads(sys.argv[1])

# 读取 HTML 模板
with open('middle-east-tracker-zh-TW.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. 更新时间戳
html = re.sub(
    r'<div class="last-update">最後更新：.*?</div>',
    f'<div class="last-update">最後更新：{data["timestamp"]}</div>',
    html
)

# 2. 更新市场数据（金价）
if 'market' in data and 'gold' in data['market']:
    gold_value = s2tw(data['market']['gold'])
    html = re.sub(
        r'(gold-card">\s*<div class="market-value">)[^<]+',
        r'\1' + gold_value,
        html,
        flags=re.DOTALL
    )

# 3. 更新市场数据（油价 WTI）
if 'market' in data and 'oil_wti' in data['market']:
    wti_value = s2tw(data['market']['oil_wti'])
    html = re.sub(
        r'(wti-card">\s*<div class="market-value">)[^<]+',
        r'\1' + wti_value,
        html,
        flags=re.DOTALL
    )

# 4. 更新市场数据（油价 Brent）
if 'market' in data and 'oil_brent' in data['market']:
    brent_value = s2tw(data['market']['oil_brent'])
    html = re.sub(
        r'(brent-card">\s*<div class="market-value">)[^<]+',
        r'\1' + brent_value,
        html,
        flags=re.DOTALL
    )

# 5. 更新新闻内容（直接替换，简单方法）
if 'news' in data:
    news_cards = re.findall(
        r'<div class="news-card">.*?</div>\s*</div>\s*</div>',
        html,
        flags=re.DOTALL
    )
    
    for i, news_item in enumerate(data['news'][:3]):
        if i < len(news_cards):
            title = s2tw(news_item.get('title', ''))
            desc = s2tw(news_item.get('desc', ''))
            
            # 替换第 i 个新闻卡片
            old_card = news_cards[i]
            new_card = re.sub(
                r'(<div class="news-title">).*?(</div>)',
                r'\1' + title + r'\2',
                old_card,
                flags=re.DOTALL
            )
            new_card = re.sub(
                r'(<div class="news-description">).*?(</div>)',
                r'\1' + desc + r'\2',
                new_card,
                flags=re.DOTALL
            )
            
            html = html.replace(old_card, new_card, 1)

# 写回文件
with open('middle-east-tracker-zh-TW.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"✅ HTML 已更新：{data['timestamp']}")
print("✅ 已转换为繁体中文")
