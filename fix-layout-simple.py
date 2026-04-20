#!/usr/bin/env python3
"""
最终修复方案（简化版）：
1. AI 预测保持 4 格子布局（已OK）
2. 金价/油价：在现价和预测之间插入视觉分隔，并添加 CSS 让它们分两行显示
"""

with open('middle-east-tracker-zh-TW.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# ============================================
# 金价：在现价和第一个预测之间插入分隔标记
# ============================================
for i, line in enumerate(lines):
    # 找到金价的第一个预测（📊 短期預測）
    if '📊 短期預測（7日）' in line:
        # 往回找 wrapper
        for j in range(i, max(0, i-5), -1):
            if '<div class="market-card-wrapper">' in lines[j]:
                # 在这之前插入分隔行标记
                lines.insert(j, '                    <!-- 金价预测开始 -->\n')
                print(f"✓ 在金价现价和预测之间插入分隔（行 {j}）")
                break
        break

# ============================================
# 油价：在现价和第一个预测之间插入分隔标记
# ============================================
for i, line in enumerate(lines):
    # 找到油价的第一个预测（📊 樂觀情境）
    if '📊 樂觀情境（停火成功）' in line:
        # 往回找 wrapper
        for j in range(i, max(0, i-5), -1):
            if '<div class="market-card-wrapper">' in lines[j]:
                # 在这之前插入分隔行标记
                lines.insert(j, '                    <!-- 油价预测开始 -->\n')
                print(f"✓ 在油价现价和预测之间插入分隔（行 {j}）")
                break
        break

# 保存
with open('middle-east-tracker-zh-TW.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

# ============================================
# 添加 CSS：让金价/油价的 market-grid 分两行显示
# ============================================
with open('middle-east-tracker-zh-TW.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 找到 market-grid 的 CSS
css_insert_pos = html.find('.market-grid {')
if css_insert_pos > 0:
    # 往前插入新的 CSS
    new_css = '''
        /* 金价/油价板块：强制分两行显示 */
        .market-subsection .market-grid {
            display: flex;
            flex-direction: column;
            gap: 32px;
        }
        
        .market-subsection .market-grid > .market-card-wrapper,
        .market-subsection .market-grid > * {
            width: 100%;
        }
        
        /* 当遇到注释"预测开始"时，前面的卡片为一组 */
        .market-subsection .market-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
        }
        
'''
    
    html = html[:css_insert_pos] + new_css + html[css_insert_pos:]
    print("✓ 添加分行显示 CSS")

with open('middle-east-tracker-zh-TW.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\n✅ 修复完成！")
print("\n预期效果：")
print("【金价】")
print("  第一行：💰 現貨黃金")
print("  ---分隔---")
print("  第二行：📊 短期預測 | 📊 悲觀情境")
print("\n【油价】")
print("  第一行：💰 WTI | 💰 Brent")
print("  ---分隔---")
print("  第二行：📊 樂觀 | 📊 基準 | 📊 悲觀")
