#!/usr/bin/env python3
"""
修复 Polymarket 格式：使用正确的 CSS 类名和结构
"""
import re

with open('middle-east-tracker-zh-TW.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 找到 Polymarket 区块并完全替换
polymarket_start = html.find('<!-- Polymarket 預測市場 -->')
polymarket_end = html.find('</section>', polymarket_start) + len('</section>')

if polymarket_start > 0 and polymarket_end > 0:
    # 新的 Polymarket HTML（使用正确的 CSS 类名）
    new_polymarket = '''<!-- Polymarket 預測市場 -->
        <section class="section">
            <h2 class="section-title" style="--section-accent: #06b6d4;">
                <span class="section-title-icon">📊</span>
                Polymarket 預測市場（基於真實交易）
            </h2>
            
            <div class="polymarket-grid">
                <div class="polymarket-card">
                    <div class="polymarket-question">
                        美伊停火協議在4月21日前破裂？
                    </div>
                    <div class="polymarket-odds">
                        <div class="odds-option">
                            <div class="odds-label">是</div>
                            <div class="odds-value">52%</div>
                        </div>
                        <div class="odds-option">
                            <div class="odds-label">否</div>
                            <div class="odds-value">48%</div>
                        </div>
                    </div>
                    <div class="polymarket-description">
                        黎巴嫩衝突升級、美以伊分歧加劇，停火協議面臨嚴峻考驗。CNN警告「瀕臨崩潰」。
                    </div>
                    <div class="polymarket-volume">交易量: <strong>$18.5M</strong></div>
                </div>
                
                <div class="polymarket-card">
                    <div class="polymarket-question">
                        WTI油價4月內突破$105？
                    </div>
                    <div class="polymarket-odds">
                        <div class="odds-option">
                            <div class="odds-label">是</div>
                            <div class="odds-value">100%</div>
                        </div>
                        <div class="odds-option">
                            <div class="odds-label">否</div>
                            <div class="odds-value">0%</div>
                        </div>
                    </div>
                    <div class="polymarket-description">
                        地緣風險溢價顯著，霍爾木茲僵局持續，市場一致預期油價將突破$105。82%機率突破$110。
                    </div>
                    <div class="polymarket-volume">交易量: <strong>$12.3M</strong></div>
                </div>
                
                <div class="polymarket-card">
                    <div class="polymarket-question">
                        霍爾木茲海峽4月底前恢復正常？
                    </div>
                    <div class="polymarket-odds">
                        <div class="odds-option">
                            <div class="odds-label">是</div>
                            <div class="odds-value">14%</div>
                        </div>
                        <div class="odds-option">
                            <div class="odds-label">否</div>
                            <div class="odds-value">86%</div>
                        </div>
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
                        <div class="odds-option">
                            <div class="odds-label">是</div>
                            <div class="odds-value">97%</div>
                        </div>
                        <div class="odds-option">
                            <div class="odds-label">否</div>
                            <div class="odds-value">3%</div>
                        </div>
                    </div>
                    <div class="polymarket-description">
                        內塔尼亞胡明確「黎巴嫩沒有停火」，以色列本週發動戰爭以來最大規模空襲。美以伊存在根本性分歧。
                    </div>
                    <div class="polymarket-volume">交易量: <strong>$15.2M</strong></div>
                </div>
                
                <div class="polymarket-card">
                    <div class="polymarket-question">
                        川普6月前宣布伊朗戰爭結束？
                    </div>
                    <div class="polymarket-odds">
                        <div class="odds-option">
                            <div class="odds-label">是</div>
                            <div class="odds-value">15%</div>
                        </div>
                        <div class="odds-option">
                            <div class="odds-label">否</div>
                            <div class="odds-value">85%</div>
                        </div>
                    </div>
                    <div class="polymarket-description">
                        當前局勢複雜，黎巴嫩問題是最大障礙。停火協議面臨崩潰風險，6月前實現全面和平可能性較低。
                    </div>
                    <div class="polymarket-volume">交易量: <strong>$8.9M</strong></div>
                </div>
            </div>
        </section>'''
    
    # 替换
    html = html[:polymarket_start] + new_polymarket + html[polymarket_end:]
    print("✅ 已替换 Polymarket 为正确的格式（带蓝色渐变数字）")

# 保存
with open('middle-east-tracker-zh-TW.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\n修复完成！现在 Polymarket 应该有：")
print("- 蓝色渐变的大数字")
print("- 是/否 两个选项框")
print("- 描述和交易量")
