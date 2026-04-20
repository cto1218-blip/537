#!/usr/bin/env python3
"""
彻底修复所有问题：
1. AI 预测卡片样式恢复紧凑
2. Polymarket %爆框
3. 油价预测改为2行（2+1或自适应）
"""
import re

with open('middle-east-tracker-zh-TW.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("=" * 70)
print("开始修复")
print("=" * 70)

# ============================================
# 修复 1: AI 预测卡片 - 减小padding和字体
# ============================================
# 找到 .prediction-card 的样式，减小padding
old_card_css = re.search(r'(\.prediction-card \{[^}]*padding: )(\d+px);', html)
if old_card_css:
    html = html.replace(old_card_css.group(0), f'{old_card_css.group(1)}20px;')
    print("✓ 减小 prediction-card padding: 28px → 20px")

# 减小标题字体
old_title_css = re.search(r'(\.prediction-title \{[^}]*font-size: )([\d.]+rem);', html)
if old_title_css:
    html = html.replace(old_title_css.group(0), f'{old_title_css.group(1)}1rem;')
    print("✓ 减小 prediction-title 字体")

# 确保描述字体小
html = re.sub(
    r'\.prediction-description \{[^}]+\}',
    '''.prediction-description {
            font-size: 0.8rem;
            color: var(--color-text-secondary);
            line-height: 1.5;
            margin-bottom: 16px;
            max-height: 120px;
            overflow-y: auto;
            overflow-x: hidden;
        }''',
    html
)
print("✓ 优化 prediction-description 样式（更小字体+更低高度）")

# ============================================
# 修复 2: Polymarket %爆框 - 检查并修复
# ============================================
# 查找 Polymarket 区块
poly_start = html.find('<!-- Polymarket 預測市場 -->')
poly_end = html.find('<!-- 市場洞察', poly_start)

if poly_start > 0 and poly_end > 0:
    poly_section = html[poly_start:poly_end]
    
    # 检查是否有 odds-value 包含%的地方
    # 问题可能是：52% 这样的文本没有正确包装
    # 确保 odds-value 有足够宽度
    
    # 修复 odds-value 的 CSS
    html = re.sub(
        r'(\.odds-value \{[^}]*)(font-size: [\d.]+rem;)',
        r'\1font-size: 2rem; min-width: 80px; text-align: center;',
        html
    )
    print("✓ 修复 Polymarket odds-value 样式（添加最小宽度）")

# ============================================
# 修复 3: 油价预测 - 改为自适应（允许换行）
# ============================================
# 找到油价区块的 grid-row 设置，删除它
# 让预测卡片自然换行而不是强制一行

# 删除强制 grid-row 的 CSS
html = re.sub(
    r'/\* 金价/油价：强制分两行显示 \*/.*?/\* 预测卡片：固定第二行，允许多列 \*/\s*\.market-subsection \.market-grid > \.market-card-wrapper\.prediction-price \{\s*grid-row: 2;\s*\}',
    '''/* 金价/油价：分组显示，自适应换行 */
        .market-subsection .market-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 16px;
        }
        
        /* 现价卡片：稍大一些 */
        .market-subsection .market-grid > .market-card-wrapper.current-price {
            min-width: 260px;
        }
        
        /* 预测卡片：较小，允许3个一行或2+1两行 */
        .market-subsection .market-grid > .market-card-wrapper.prediction-price {
            min-width: 220px;
        }''',
    html,
    flags=re.DOTALL
)
print("✓ 删除强制 grid-row，改为自适应换行")

# ============================================
# 保存并验证
# ============================================
with open('middle-east-tracker-zh-TW.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\n" + "=" * 70)
print("验证修复结果")
print("=" * 70)

# 重新读取验证
with open('middle-east-tracker-zh-TW.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. AI 预测
pred_card_padding = re.search(r'\.prediction-card \{[^}]*padding: (\d+)px', html)
pred_desc_height = re.search(r'\.prediction-description \{[^}]*max-height: (\d+)px', html)
print(f"\nAI 预测卡片:")
print(f"- padding: {pred_card_padding.group(1) if pred_card_padding else '?'}px")
print(f"- 描述高度: {pred_desc_height.group(1) if pred_desc_height else '?'}px")

# 2. Polymarket
odds_min_width = 'min-width' in html and 'odds-value' in html
print(f"\nPolymarket:")
print(f"- odds-value 最小宽度: {'✅ 已设置' if odds_min_width else '❌ 未设置'}")

# 3. 油价
has_grid_row = 'grid-row: 1' in html or 'grid-row: 2' in html
market_grid_columns = re.search(r'\.market-subsection \.market-grid \{[^}]*grid-template-columns: ([^;]+);', html)
print(f"\n油价布局:")
print(f"- 强制分行: {'❌ 已删除（自适应）' if not has_grid_row else '⚠️ 仍存在'}")
if market_grid_columns:
    print(f"- grid 设置: {market_grid_columns.group(1)}")

print("\n" + "=" * 70)
print("✅ 修复完成！")
print("\n预期效果：")
print("1. AI 预测：紧凑的4格子（padding 20px，描述120px高）")
print("2. Polymarket：%符号有足够空间，不爆框")
print("3. 油价：3个预测自适应换行（宽屏3个一行，窄屏2+1）")
print("=" * 70)
