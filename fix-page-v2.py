#!/usr/bin/env python3
"""
修复中东局势页面 - 精确版本
"""
import re

# 读取文件
with open('middle-east-tracker-zh-TW.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

html = ''.join(lines)

# ============================================
# Step 1: 添加 CSS 样式用于 gold-card
# ============================================
# 查找 .oil-card 的 CSS 定义，在其后添加 .gold-card
oil_card_css_pos = html.find('.oil-card {')
if oil_card_css_pos > 0:
    # 找到这个 CSS 块的结束位置
    next_brace = html.find('}', oil_card_css_pos)
    gold_card_css = '''
        
        .gold-card {
            background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
            border-left: 4px solid #f59e0b;
        }
        
        .gold-card .market-value {
            color: #92400e;
        }
        
        .gold-card .market-peak {
            color: #b45309;
        }'''
    
    html = html[:next_brace+1] + gold_card_css + html[next_brace+1:]

# ============================================
# Step 2: 在第一个 oil-card 前添加金价卡片
# ============================================
gold_html = '''                    <!-- 金价指标 -->
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
                    
'''

first_oil_card = html.find('<div class="market-card oil-card">')
if first_oil_card > 0:
    html = html[:first_oil_card] + gold_html + html[first_oil_card:]
    print("✓ 添加了金价卡片")
else:
    print("❌ 未找到油价卡片位置")

# ============================================
# Step 3: 在 AI 预测区块前添加 Polymarket 区块
# ============================================
polymarket_html = '''
        <!-- Polymarket 預測市場 -->
        <section class="section">
            <h2 class="section-title">
                <span class="section-title-icon">📊</span>
                Polymarket 預測市場
            </h2>
            
            <div class="polymarket-grid">
                <div class="polymarket-card">
                    <div class="polymarket-question">
                        停火協議4月21日前破裂？
                    </div>
                    <div class="polymarket-odds">
                        <span class="odds-yes">是 52%</span>
                        <span class="odds-divider">|</span>
                        <span class="odds-no">否 48%</span>
                    </div>
                    <div class="polymarket-description">
                        黎巴嫩衝突升級、美以伊分歧加劇，市場預期停火協議面臨嚴峻考驗。CNN警告「瀕臨崩潰」。
                    </div>
                    <div class="polymarket-volume">交易量: <strong>$18.5M</strong></div>
                </div>
                
                <div class="polymarket-card">
                    <div class="polymarket-question">
                        WTI油價4月內突破$105？
                    </div>
                    <div class="polymarket-odds">
                        <span class="odds-yes">是 100%</span>
                        <span class="odds-divider">|</span>
                        <span class="odds-no">否 0%</span>
                    </div>
                    <div class="polymarket-description">
                        地緣風險溢價顯著，霍爾木茲僵局持續，市場一致預期油價將突破$105。82%機率突破$110。
                    </div>
                    <div class="polymarket-volume">交易量: <strong>$12.3M</strong></div>
                </div>
                
                <div class="polymarket-card">
                    <div class="polymarket-question">
                        霍爾木茲4月底前恢復正常？
                    </div>
                    <div class="polymarket-odds">
                        <span class="odds-yes">是 14%</span>
                        <span class="odds-divider">|</span>
                        <span class="odds-no">否 86%</span>
                    </div>
                    <div class="polymarket-description">
                        油輪/貨船觀望，可能存在水雷威脅需清理。馬士基警告恢復需「數週甚至數月」。
                    </div>
                    <div class="polymarket-volume">交易量: <strong>$9.7M</strong></div>
                </div>
                
                <div class="polymarket-card">
                    <div class="polymarket-question">
                        黎巴嫩衝突持續至4月底？
                    </div>
                    <div class="polymarket-odds">
                        <span class="odds-yes">是 97%</span>
                        <span class="odds-divider">|</span>
                        <span class="odds-no">否 3%</span>
                    </div>
                    <div class="polymarket-description">
                        內塔尼亞胡明確「黎巴嫩沒有停火」，以色列本週發動戰爭以來最大規模空襲。美以伊存在根本性分歧。
                    </div>
                    <div class="polymarket-volume">交易量: <strong>$15.2M</strong></div>
                </div>
            </div>
        </section>

'''

# 找到 AI 预测区块的开始位置
ai_section_start = html.find('<!-- AI 預測分析 -->')
if ai_section_start > 0:
    html = html[:ai_section_start] + polymarket_html + html[ai_section_start:]
    print("✓ 添加了 Polymarket 区块")
else:
    print("❌ 未找到 AI 预测区块")

# ============================================
# Step 4: 修复 AI 预测描述（替换短描述为详细分析）
# ============================================
# 逐个替换每个预测卡片的描述
replacements = [
    (
        '<div class="prediction-title">停火持續至4/21</div>\n                    <div class="prediction-description">基於當前局勢和市場數據的綜合分析。</div>',
        '''<div class="prediction-title">停火持續至4/21</div>
                    <div class="prediction-description">
                        <strong>分析：</strong>當前停火協議面臨嚴峻考驗。黎巴嫩問題是最大變數——美以伊三方對「黎巴嫩是否包含在停火範圍內」存在公開分歧。以色列本週在黎巴嫩發動戰爭以來最大規模空襲，內塔尼亞胡明確「黎巴嫩沒有停火」；伊朗堅持黎巴嫩必須涵蓋。CNN警告協議「瀕臨崩潰」。內塔尼亞胡在國內遭遇史無前例的政治風暴，需要通過強硬立場平息批評。Polymarket顯示52%機率停火破裂。綜合評估：<strong>黎巴嫩衝突升級風險極高，協議持續至4/21的可能性較低</strong>。
                    </div>'''
    ),
    (
        '<div class="prediction-title">霍爾木茲4月恢復</div>\n                    <div class="prediction-description">基於當前局勢和市場數據的綜合分析。</div>',
        '''<div class="prediction-title">霍爾木茲4月恢復</div>
                    <div class="prediction-description">
                        <strong>分析：</strong>霍爾木茲海峽重新開放進展緩慢。儘管川普宣布「非伊朗船隻可通過」，但油輪/貨船繼續觀望，只有俄羅斯油輪通過。<strong>可能存在水雷威脅</strong>需要清理作業。馬士基集團警告運營恢復可能需要「數週甚至數月」。Polymarket顯示僅14%機率4月底前恢復正常。JP Morgan警告：若僵局持續至7月，油價可能衝破$120。Goldman警告：再關閉一個月，2026年全年Brent將維持$100+。綜合評估：<strong>安全擔憂和地緣不確定性將延緩恢復進程</strong>。
                    </div>'''
    ),
    (
        '<div class="prediction-title">黎巴嫩衝突持續</div>\n                    <div class="prediction-description">基於當前局勢和市場數據的綜合分析。</div>',
        '''<div class="prediction-title">黎巴嫩衝突持續</div>
                    <div class="prediction-description">
                        <strong>分析：</strong>黎巴嫩衝突幾乎確定持續。內塔尼亞胡明確表示「黎巴嫩沒有停火」，授權與黎巴嫩談判但攻擊未停止。以色列本週在黎巴嫩發動戰爭以來最大規模空襲（數百架次），超160人死亡。美以伊三方對黎巴嫩問題存在<strong>根本性分歧</strong>：以色列認為不在停火範圍內，伊朗堅持必須涵蓋。內塔尼亞胡在國內遭遇政治風暴，需要通過對黎巴嫩的強硬立場證明「並非完全投降」。Polymarket顯示97%機率黎巴嫩衝突持續。綜合評估：<strong>黎巴嫩衝突是當前中東局勢最大的不穩定因素</strong>。
                    </div>'''
    ),
    (
        '<div class="prediction-title">川普6月宣布結束</div>\n                    <div class="prediction-description">基於當前局勢和市場數據的綜合分析。</div>',
        '''<div class="prediction-title">川普6月宣布結束</div>
                    <div class="prediction-description">
                        <strong>分析：</strong>川普在4月8日宣布兩週停火協議（至4月21日），但當前局勢複雜。黎巴嫩問題是最大障礙——美以伊三方存在根本性分歧，停火協議面臨崩潰風險（52%機率破裂）。霍爾木茲僵局持續，油價維持高位。加薩停火經驗顯示「明確範圍、執行機制、監督」是關鍵，但伊朗停火協議在這方面存在缺陷。若停火破裂，戰爭可能重新升級。若停火奇蹟成功，川普可能在5-6月宣布「任務完成」。但考慮到當前複雜局勢，綜合評估：<strong>6月前實現全面和平的可能性較低</strong>。
                    </div>'''
    )
]

for old, new in replacements:
    if old in html:
        html = html.replace(old, new, 1)
        print(f"✓ 替换了预测描述")
    else:
        print(f"❌ 未找到预测描述: {old[:30]}...")

# ============================================
# Step 5: 重组时间线
# ============================================
# 找到时间线区块并完全替换
timeline_start = html.find('<!-- 時間線 -->')
timeline_end = html.find('</section>\n        </div>', timeline_start)

if timeline_start > 0 and timeline_end > 0:
    new_timeline = '''<!-- 時間線 -->
        <section class="section">
            <h2 class="section-title">
                <span class="section-title-icon">📅</span>
                完整時間線
            </h2>
            
            <div class="timeline">
                <div class="timeline-item">
                    <div class="timeline-marker"></div>
                    <div class="timeline-date">2026年2月28日</div>
                    <div class="timeline-content">
                        <h3>衝突爆發 - "史詩怒火"行動</h3>
                        <ul>
                            <li>德黑蘭多地遭空襲，伊朗最高領袖<span class="alert">哈梅內伊遇襲身亡</span></li>
                            <li>以色列宣佈對伊朗發動<span class="highlight">先發制人打擊</span></li>
                            <li>美國將行動命名為"史詩怒火"（Operation Epic Fury）</li>
                            <li>伊朗啟動<span class="highlight">"真實承諾-4"</span>反擊行動</li>
                        </ul>
                    </div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-marker"></div>
                    <div class="timeline-date">3月1-7日</div>
                    <div class="timeline-content">
                        <h3>全面戰爭 - 能力摧毀階段</h3>
                        <ul>
                            <li>美以<span class="highlight">摧毀75%伊朗導彈發射器</span>，打擊3000+目標</li>
                            <li>伊朗導彈/無人機攻擊減少<span class="alert">90%/83%</span></li>
                            <li>美軍擊沉伊朗<span class="highlight">58艘軍艦</span>（含1艘潛艇）</li>
                            <li>伊朗摧毀<span class="highlight">7部美軍薩德雷達</span>，擊落82架無人機</li>
                        </ul>
                    </div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-marker"></div>
                    <div class="timeline-date">4月8日</div>
                    <div class="timeline-content">
                        <h3>🔥 兩週停火協議達成</h3>
                        <ul>
                            <li>川普宣佈<span class="highlight">兩週停火協議</span>（至4月21日），由巴基斯坦調解</li>
                            <li>川普派遣<span class="highlight">副總統萬斯</span>於本週末前往伊斯蘭堡會談</li>
                            <li>Polymarket平台交易員通過<span class="alert">精準押注</span>獲利近百萬美元，CFTC啟動初步調查</li>
                        </ul>
                    </div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-marker"></div>
                    <div class="timeline-date">4月8日（停火宣佈後）</div>
                    <div class="timeline-content">
                        <h3>🚨 以色列在黎巴嫩發動最大規模空襲</h3>
                        <ul>
                            <li>停火宣佈後，以色列在黎巴嫩發動<span class="alert">戰爭以來最大規模空襲</span>（數百架次）</li>
                            <li>內塔尼亞胡明確表示「<span class="alert">黎巴嫩沒有停火</span>」，將繼續打擊真主黨</li>
                            <li>美以伊三方對<span class="highlight">黎巴嫩是否包含在停火範圍內</span>存在公開分歧</li>
                        </ul>
                    </div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-marker"></div>
                    <div class="timeline-date">4月9日（週三）</div>
                    <div class="timeline-content">
                        <h3>黎巴嫩衝突升級</h3>
                        <ul>
                            <li>以色列持續在黎巴嫩發動大規模空襲</li>
                            <li>伊朗批評美國提出的停火協議條款「不合理」，堅持黎巴嫩必須涵蓋在停火範圍內</li>
                        </ul>
                    </div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-marker"></div>
                    <div class="timeline-date">4月10日（週四）</div>
                    <div class="timeline-content">
                        <h3>內塔尼亞胡政治風暴</h3>
                        <ul>
                            <li>內塔尼亞胡在以色列國內遭遇<span class="alert">史無前例的政治風暴</span>，被指犯下「史上最嚴重政治災難」</li>
                            <li>反對派指控他被川普「強迫接受停火」，未能實現戰爭目標</li>
                        </ul>
                    </div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-marker"></div>
                    <div class="timeline-date">4月11日（週五）</div>
                    <div class="timeline-content">
                        <h3>📊 加薩停火協議滿6個月</h3>
                        <ul>
                            <li>加薩停火協議滿<span class="highlight">6個月</span>（自2025年10月11日起生效）</li>
                            <li>儘管停火協議持續，6個月內仍有<span class="alert">738人在以色列攻擊中死亡</span>（加薩衛生部數據）</li>
                            <li>整個加以衝突已造成<strong>超過4.9萬人死亡</strong></li>
                            <li>加薩停火為伊朗停火提供經驗借鑒：<strong>明確範圍、執行機制、監督方可持續</strong></li>
                        </ul>
                    </div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-marker"></div>
                    <div class="timeline-date">4月12日（週六）</div>
                    <div class="timeline-content">
                        <h3>🤝 副總統萬斯會談巴基斯坦總理</h3>
                        <ul>
                            <li>美國副總統萬斯與巴基斯坦總理會談，討論停火協議執行細節</li>
                            <li>重點包括黎巴嫩衝突問題</li>
                            <li>內塔尼亞胡授權與黎巴嫩談判，但以色列在黎巴嫩的攻擊未停止</li>
                            <li>國會調查Polymarket精準押注獲利事件：超過<strong>$185M+</strong>流入伊朗停火相關市場</li>
                        </ul>
                    </div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-marker"></div>
                    <div class="timeline-date">4月13日（週日）</div>
                    <div class="timeline-content">
                        <h3>📈 油價徘徊高位 + 市場擔憂加劇</h3>
                        <ul>
                            <li>油價徘徊在<span class="alert">$96-104區間</span>（近期高點$104.4）</li>
                            <li>Polymarket預測<strong>100%機率</strong>4月內突破$105，<strong>82%機率</strong>突破$110</li>
                            <li>市場預測<strong>52%機率</strong>停火可能在4月21日前破裂</li>
                            <li>CNN警告伊朗戰爭的停火協議「<span class="alert">瀕臨崩潰</span>」</li>
                            <li>馬士基集團表示運營恢復可能需要<strong>數週甚至數月</strong></li>
                            <li>霍爾木茲海峽<span class="highlight">仍未完全重新開放</span>：油輪/貨船繼續觀望，只有俄羅斯油輪通過</li>
                        </ul>
                    </div>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-marker"></div>
                    <div class="timeline-date">4月14日（週一）🆕</div>
                    <div class="timeline-content">
                        <h3>⚡️ 當前局勢</h3>
                        <ul>
                            <li>黃金價格飆升至<strong>$4,787/盎司</strong>（+2.8%），避險需求升溫</li>
                            <li><strong>停火協議僅剩7天</strong>（4月21日到期），破裂風險極高</li>
                            <li>黎巴嫩衝突持續，<strong>97%機率</strong>衝突將持續至4月底</li>
                            <li>霍爾木茲僵局持續，<strong>僅14%機率</strong>4月底前恢復正常</li>
                            <li>市場情緒謹慎：<strong>僅15%機率</strong>停火成功</li>
                            <li>沙特SATORP煉油廠和東西石油管道遭攻擊關閉，加劇能源供應擔憂</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>'''
    
    html = html[:timeline_start] + new_timeline + html[timeline_end:]
    print("✓ 替换了时间线区块")
else:
    print("❌ 未找到时间线区块")

# 保存文件
with open('middle-east-tracker-zh-TW.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\n✅ 所有修复完成！")
