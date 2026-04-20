#!/usr/bin/env python3
with open('middle-east-tracker-zh-TW.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 新的时间线内容（10个独立事件）
new_timeline = '''        <!-- 時間線 -->
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
        </section>
'''

# 替换第 1393-1471 行
new_lines = lines[:1392] + [new_timeline] + lines[1470:]

with open('middle-east-tracker-zh-TW.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("✅ 时间线已替换为10个独立事件！")
