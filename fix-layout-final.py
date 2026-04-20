#!/usr/bin/env python3
"""
最直接的方案：用 CSS 类标记现价和预测，然后用 grid-row 强制分行
"""

with open('middle-east-tracker-zh-TW.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

# ============================================
# 给所有卡片添加类标记
# ============================================
# 现价卡片添加 'current-price' 类
# 预测卡片添加 'prediction-price' 类

# 金价现价
html = re.sub(
    r'(<div class="market-card-wrapper">)\s*(<div class="market-card-title current">💰 現貨黃金</div>)',
    r'\1\n                        \2',
    html
)

# 金价预测
html = re.sub(
    r'(<div class="market-card-wrapper">)\s*(<div class="market-card-title prediction">📊 短期預測)',
    r'<div class="market-card-wrapper prediction-price">\n                        \2',
    html,
    count=1
)

html = re.sub(
    r'(<div class="market-card-wrapper">)\s*(<div class="market-card-title prediction">📊 悲觀情境（停火破裂）</div>)',
    r'<div class="market-card-wrapper prediction-price">\n                        \2',
    html,
    count=1
)

# 油价现价（两个）
html = re.sub(
    r'(<div class="market-card-wrapper">)\s*(<div class="market-card-title current oil">💰 當前)',
    r'<div class="market-card-wrapper current-price">\n                        \2',
    html
)

# 油价预测（三个）
html = re.sub(
    r'(<div class="market-card-wrapper">)\s*(<div class="market-card-title prediction">📊 樂觀情境)',
    r'<div class="market-card-wrapper prediction-price">\n                        \2',
    html,
    count=1
)

html = re.sub(
    r'(<div class="market-card-wrapper">)\s*(<div class="market-card-wrapper prediction-price">\n                        <div class="market-card-title prediction">📊 基準情境)',
    r'<div class="market-card-wrapper prediction-price">\n                        <div class="market-card-title prediction">📊 基準情境)',
    html,
    count=1
)

html = re.sub(
    r'(<div class="market-card-wrapper">)\s*(<div class="market-card-title prediction">📊 悲觀情境（停火破裂）</div>)',
    r'<div class="market-card-wrapper prediction-price">\n                        \2',
    html,
    count=2  # 油价的悲观情境（第二个）
)

print("✓ 添加类标记到卡片")

# ============================================
# 添加 CSS：现价和预测分两行
# ============================================
css_insert_pos = html.find('.market-grid {')
if css_insert_pos > 0:
    new_css = '''
        /* 金价/油价：现价和预测分两行 */
        .market-subsection .market-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            grid-auto-flow: dense;
        }
        
        /* 现价卡片：第一行 */
        .market-subsection .market-grid .market-card-wrapper:not(.prediction-price) {
            grid-row: 1;
        }
        
        /* 预测卡片：第二行 */
        .market-subsection .market-grid .market-card-wrapper.prediction-price {
            grid-row: 2;
        }
        
'''
    
    html = html[:css_insert_pos] + new_css + html[css_insert_pos:]
    print("✓ 添加分行 CSS")

with open('middle-east-tracker-zh-TW.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 验证
with open('middle-east-tracker-zh-TW.html', 'r', encoding='utf-8') as f:
    html = f.read()

current_count = html.count('current-price')
prediction_count = html.count('prediction-price')

print(f"\n验证：")
print(f"- current-price 类: {current_count} 个")
print(f"- prediction-price 类: {prediction_count} 个")
print(f"- grid-row CSS: {'✓ 已添加' if 'grid-row:' in html else '❌ 未添加'}")

print("\n✅ 修复完成！")
