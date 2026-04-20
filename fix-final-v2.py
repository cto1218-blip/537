#!/usr/bin/env python3
"""
最终修复：
1. 删除第一个 Polymarket 区块（第990行那个简单版）
2. 保留第二个 Polymarket 区块（第1135行旧版，有蓝色框框）
3. 删除重复的金价卡片（只保留一个）
4. 将市场分析拆分成两个独立板块：油价分析 + 金价分析
"""

with open('middle-east-tracker-zh-TW.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ============================================
# 1. 删除第一个 Polymarket 区块（简单版）
# ============================================
# 找到并删除第一个 Polymarket 区块（从 "<!-- Polymarket 預測市場 -->" 到下一个 </section>）
import re

# 删除第一个出现的 Polymarket 区块（简单版）
pattern1 = r'<!-- Polymarket 預測市場 -->\s*<section class="section">\s*<h2 class="section-title">\s*<span class="section-title-icon">📊</span>\s*Polymarket 預測市場\s*</h2>.*?</section>\s*\n'
html = re.sub(pattern1, '', html, count=1, flags=re.DOTALL)
print("✓ 删除了第一个 Polymarket 区块（简单版）")

# ============================================
# 2. 删除重复的金价卡片（只保留第一个）
# ============================================
# 金价卡片的完整HTML
gold_card_pattern = r'<!-- 金价指标 -->\s*<div class="market-card gold-card">.*?</div>\s*</div>\s*'

# 找到所有金价卡片
gold_cards = re.findall(gold_card_pattern, html, re.DOTALL)
if len(gold_cards) > 1:
    # 删除第二个及以后的金价卡片
    for i in range(1, len(gold_cards)):
        html = html.replace(gold_cards[i], '', 1)
    print(f"✓ 删除了 {len(gold_cards)-1} 个重复的金价卡片")

# ============================================
# 3. 重组市场分析：拆分成油价分析 + 金价分析两个独立板块
# ============================================
# 找到 "市場波動分析" 区块的开始位置
market_section_start = html.find('<!-- 市場波動分析 -->')
if market_section_start > 0:
    # 找到这个 section 的结束位置（找到包含 oil-analysis 的那个 </div>）
    market_section_end = html.find('<!-- 市場洞察 -->', market_section_start)
    
    if market_section_end > 0:
        # 提取当前市场分析区块的内容
        old_market_section = html[market_section_start:market_section_end]
        
        # 构建新的两个独立板块
        new_market_sections = '''<!-- 黃金市場分析 -->
        <section class="section">
            <h2 class="section-title" style="--section-accent: #f59e0b;">
                <span class="section-title-icon">✨</span>
                黃金市場分析
            </h2>
            
            <div class="market-subsection">
                <div class="market-grid">
                    <!-- 金价指标 -->
                    <div class="market-card gold-card">
                        <div class="market-card-header">
                            <div class="market-label">現貨黃金</div>
                            <div class="market-value">$4,787<span class="market-unit">/盎司</span></div>
                        </div>
                        <div class="market-change positive">▲ +2.8%</div>
                        <div class="market-meta">
                            <span>4月14日 00:40</span>
                            <span class="market-peak">避險需求升溫</span>
                        </div>
                    </div>
                    
                    <div class="market-card gold-card">
                        <div class="market-card-header">
                            <div class="market-label">短期預測（7日）</div>
                            <div class="market-value">$4,850-4,950</div>
                        </div>
                        <div class="market-change positive">▲ 預測上漲 +2-4%</div>
                        <div class="market-meta">
                            <span>7日內</span>
                            <span class="market-peak">避險情緒主導</span>
                        </div>
                    </div>
                    
                    <div class="market-card gold-card">
                        <div class="market-card-header">
                            <div class="market-label">悲觀情境（停火破裂）</div>
                            <div class="market-value">$5,100-5,300</div>
                        </div>
                        <div class="market-change positive">▲ 暴漲 +7-11%</div>
                        <div class="market-meta">
                            <span>數日內</span>
                            <span class="market-recovery">機率：52%</span>
                        </div>
                    </div>
                    
                    <div class="market-card stock-analysis">
                        <div class="analysis-title">📊 金價驅動因素</div>
                        <ul class="analysis-list">
                            <li><strong>地緣風險溢價</strong>：停火協議面臨崩潰風險（52%機率破裂），黎巴嫩衝突升級，避險需求升溫</li>
                            <li><strong>美元走弱預期</strong>：若停火破裂，Fed可能延遲加息，利好黃金</li>
                            <li><strong>央行購金持續</strong>：新興市場央行持續增持黃金儲備，支撐長期需求</li>
                            <li><strong>技術面強勢</strong>：突破$4,750阻力位，下一目標$5,000</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>
        
        <!-- 油價市場分析 -->
        <section class="section">
            <h2 class="section-title" style="--section-accent: #10b981;">
                <span class="section-title-icon">🛢️</span>
                國際油價分析（7日預測）
            </h2>
            
            <div class="market-subsection">
                <div class="market-grid">
                    <div class="market-card oil-card">
                        <div class="market-card-header">
                            <div class="market-label">當前 WTI 原油</div>
                            <div class="market-value">$96-104<span class="market-unit">/桶</span></div>
                        </div>
                        <div class="market-change positive">▲ 近期高點$104.4</div>
                        <div class="market-meta">
                            <span>4月13日 09:33</span>
                            <span class="market-peak">地緣風險溢價</span>
                        </div>
                    </div>
                    
                    <div class="market-card oil-card">
                        <div class="market-card-header">
                            <div class="market-label">當前 Brent 原油</div>
                            <div class="market-value">$95-103<span class="market-unit">/桶</span></div>
                        </div>
                        <div class="market-change positive">▲ 近期高點$102.3</div>
                        <div class="market-meta">
                            <span>4月13日 09:33</span>
                            <span class="market-peak">停火脆弱擔憂</span>
                        </div>
                    </div>
                    
                    <div class="market-card oil-card">
                        <div class="market-card-header">
                            <div class="market-label">樂觀情境（停火成功）</div>
                            <div class="market-value">$92-98</div>
                        </div>
                        <div class="market-change negative">▼ 預測回落 -4%</div>
                        <div class="market-meta">
                            <span>7日內</span>
                            <span class="market-trend">機率：15%</span>
                        </div>
                    </div>
                    
                    <div class="market-card oil-card">
                        <div class="market-card-header">
                            <div class="market-label">基準情境（僵局持續）</div>
                            <div class="market-value">$98-107</div>
                        </div>
                        <div class="market-change positive">▲ 預測震盪 ±3%</div>
                        <div class="market-meta">
                            <span>7日內</span>
                            <span class="market-note">機率：33%</span>
                        </div>
                    </div>
                    
                    <div class="market-card oil-card">
                        <div class="market-card-header">
                            <div class="market-label">悲觀情境（停火破裂）</div>
                            <div class="market-value">$115-125</div>
                        </div>
                        <div class="market-change negative">▲ 預測暴漲 +15%</div>
                        <div class="market-meta">
                            <span>數日內</span>
                            <span class="market-recovery">機率：52%</span>
                        </div>
                    </div>
                    
                    <div class="market-card oil-analysis">
                        <div class="analysis-title">📊 油價預測分析</div>
                        <ul class="analysis-list">
                            <li><strong>地緣風險溢價顯著</strong>：WTI原油徘徊在<strong>$96-104區間</strong>（近期高點$104.4），Polymarket預測<strong>100%機率</strong>4月內突破$105，<strong>82%機率</strong>突破$110。黎巴嫩問題成為最大威脅：以色列本週在黎巴嫩發動<strong>戰爭以來最大規模空襲</strong>（數百架次），內塔尼亞胡明確表示「黎巴嫩沒有停火」。CNN警告停火協議「瀕臨崩潰」。市場預期<strong>52%機率</strong>停火可能在4月21日前破裂，油價可能飆升至$115-125</li>
                            <li><strong>霍爾木茲海峽仍未完全開放</strong>：油輪/貨船繼續觀望，只有俄羅斯油輪通過。<strong>可能存在水雷威脅</strong>，需清理作業。馬士基集團表示運營恢復可能需要<strong>數週甚至數月</strong>。Polymarket預測<strong>僅14%機率</strong>霍爾木茲海峽4月底前恢復正常。JP Morgan警告若霍爾木茲僵局持續至7月，油價可能衝破<strong>$120</strong>。Goldman警告：再關閉一個月，2026年全年Brent將維持<strong>$100+</strong>。油價維持高位反映市場對霍爾木茲風險的擔憂</li>
                            <li><strong>三大情境預測</strong>：<strong>悲觀情境（52%）</strong>：停火數日內破裂，油價飆升至$115-125。<strong>基準情境（33%）</strong>：僵局持續但隨時可能破裂，油價震盪$98-107。<strong>樂觀情境（15%）</strong>：停火奇蹟成功，油價回落至$92-98。市場傾向悲觀情境，油價維持高位</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>
        
'''
        
        # 替换旧的市场分析区块
        html = html[:market_section_start] + new_market_sections + html[market_section_end:]
        print("✓ 拆分市场分析为两个独立板块：黃金市場分析 + 國際油價分析")

# 保存文件
with open('middle-east-tracker-zh-TW.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\n✅ 所有修复完成！")
print("- 删除了重复的 Polymarket 区块（只保留旧版蓝色框框版本）")
print("- 删除了重复的金价卡片")
print("- 拆分市场分析为两个独立板块")
