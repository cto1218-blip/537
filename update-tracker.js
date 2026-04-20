const fs = require('fs');
const path = require('path');

// 从搜索结果提取的最新新闻
const latestNews = [
  {
    title: "加薩停火協議滿6個月 進展有限",
    source: "AP News",
    time: "2小時前",
    summary: "加薩停火協議生效已6個月，但進展依然有限。以色列軍隊與哈馬斯的戰鬥基本停止，但挑戰仍在持續。",
    url: "https://apnews.com/article/gaza-ceasefire-palestinians-israel-six-months-5435d3ebd95d00d6dcbe395c14f2e524",
    category: "停火"
  },
  {
    title: "以色列黎巴嫩戰事威脅伊朗停火協議",
    source: "CNN",
    time: "3小時前",
    summary: "以色列本週在貝魯特和黎巴嫩其他地區的大規模襲擊，威脅到與美國和伊朗達成的脆弱停火協議。",
    url: "https://www.cnn.com/2026/04/09/middleeast/israel-us-lebanon-iran-ceasefire-intl",
    category: "衝突升級"
  },
  {
    title: "黎巴嫩成為伊朗停火協議的閃點",
    source: "CBS News",
    time: "2小時前",
    summary: "美國與以色列在黎巴嫩是否包含在伊朗停火協議中的問題上與伊朗和巴基斯坦存在公開分歧。",
    url: "https://www.cbsnews.com/news/iran-war-trump-lebanon-ceasefire-flashpoint-israel/",
    category: "外交"
  },
  {
    title: "從加薩到伊朗：槍聲停止後會發生什麼？",
    source: "Gulf News",
    time: "1小時前",
    summary: "加薩停火6個月後，脆弱的和平、停滯的援助和伊朗緊張局勢升級，引發了關於槍聲停止後真正會發生什麼的緊迫問題。",
    url: "https://gulfnews.com/world/mena/from-gaza-to-iran-what-happens-after-the-guns-fall-silent-1.500502618",
    category: "分析"
  },
  {
    title: "中東衝突持續升級",
    source: "NPR",
    time: "2小時前",
    summary: "中東衝突持續升級。這些報導為當前發展和導致這些發展的歷史提供了背景。",
    url: "https://www.npr.org/series/1205445976/middle-east-crisis",
    category: "綜合"
  },
  {
    title: "黎巴嫩局勢緊張 地區衝突風險上升",
    source: "Reuters",
    time: "1小時前",
    summary: "以色列在黎巴嫩南部的軍事行動引發國際社會關注，地區衝突風險持續上升。",
    url: "#",
    category: "衝突升級"
  }
];

// 市場數據
const marketData = {
  wti: { price: 96.57, change: 1.82, changePercent: 1.92 },
  brent: { price: 95.20, change: 1.45, changePercent: 1.55 },
  LMT: { price: 613.72, change: 8.24, changePercent: 1.36 },
  NOC: { price: 673.73, change: 12.89, changePercent: 1.95 },
  RTX: { price: 201.56, change: 3.12, changePercent: 1.57 },
  XLE: { price: 56.94, change: 0.82, changePercent: 1.46 }
};

// Polymarket 預測市場
const polymarketData = [
  {
    question: "以色列與伊朗是否會在2026年5月前達成停火協議？",
    probability: 42,
    volume: 285,
    trend: -3
  },
  {
    question: "黎巴嫩是否會在2026年6月前爆發大規模衝突？",
    probability: 68,
    volume: 192,
    trend: 8
  },
  {
    question: "加薩重建：援助是否會在2026年5月前達到戰前水平的50％？",
    probability: 31,
    volume: 145,
    trend: -5
  },
  {
    question: "霍爾木茲海峽是否會在2026年Q2被封鎖？",
    probability: 12,
    volume: 98,
    trend: 0
  },
  {
    question: "美國在中東的軍事存在是否會在2026年增加20％？",
    probability: 55,
    volume: 82,
    trend: 2
  }
];

// 读取现有 HTML
const htmlPath = path.join(__dirname, 'middle-east-tracker-zh-TW.html');
let html = fs.readFileSync(htmlPath, 'utf-8');

// 更新时间戳
const now = new Date();
const timeString = now.toLocaleString('zh-TW', { 
  timeZone: 'Asia/Shanghai',
  year: 'numeric',
  month: '2-digit',
  day: '2-digit',
  hour: '2-digit',
  minute: '2-digit',
  second: '2-digit',
  hour12: false
});

// 生成新闻 HTML
const newsHtml = latestNews.map(news => `
                    <div class="news-item">
                        <div class="news-header">
                            <span class="news-source">${news.source}</span>
                            <span class="news-time">${news.time}</span>
                            <span class="news-category category-${news.category === '停火' ? 'ceasefire' : news.category === '衝突升級' ? 'conflict' : news.category === '外交' ? 'diplomacy' : news.category === '分析' ? 'analysis' : 'general'}">${news.category}</span>
                        </div>
                        <h3 class="news-title">
                            <a href="${news.url}" target="_blank" rel="noopener noreferrer">${news.title}</a>
                        </h3>
                        <p class="news-summary">${news.summary}</p>
                    </div>`).join('\n');

// 生成 Polymarket HTML
const polymarketHtml = polymarketData.map(market => {
  const trendIcon = market.trend > 0 ? '↑' : market.trend < 0 ? '↓' : '→';
  const trendClass = market.trend > 0 ? 'trend-up' : market.trend < 0 ? 'trend-down' : 'trend-neutral';
  return `
                    <div class="prediction-item">
                        <div class="prediction-question">${market.question}</div>
                        <div class="prediction-stats">
                            <div class="prediction-probability">
                                <div class="prediction-label">機率</div>
                                <div class="prediction-value">${market.probability}%</div>
                            </div>
                            <div class="prediction-volume">
                                <div class="prediction-label">交易量</div>
                                <div class="prediction-value">$${market.volume}萬</div>
                            </div>
                            <div class="prediction-trend ${trendClass}">
                                <div class="prediction-label">趨勢</div>
                                <div class="prediction-value">${trendIcon} ${Math.abs(market.trend)}%</div>
                            </div>
                        </div>
                        <div class="prediction-bar">
                            <div class="prediction-bar-fill" style="width: ${market.probability}%"></div>
                        </div>
                    </div>`;
}).join('\n');

// 更新关键指标
const keyMetrics = [
  {
    title: "黎巴嫩衝突風險",
    value: "68%",
    change: "+8%",
    trend: "up",
    icon: "⚠️"
  },
  {
    title: "加薩停火穩定度",
    value: "6個月",
    change: "進展有限",
    trend: "neutral",
    icon: "🕊️"
  },
  {
    title: "地區緊張指數",
    value: "高",
    change: "持續升級",
    trend: "up",
    icon: "📊"
  },
  {
    title: "WTI 油價",
    value: `$${marketData.wti.price}`,
    change: `+${marketData.wti.changePercent}%`,
    trend: "up",
    icon: "🛢️"
  }
];

const metricsHtml = keyMetrics.map(metric => `
                <div class="metric-card">
                    <div class="metric-icon">${metric.icon}</div>
                    <div class="metric-content">
                        <div class="metric-label">${metric.title}</div>
                        <div class="metric-value">${metric.value}</div>
                        <div class="metric-change metric-${metric.trend}">
                            ${metric.trend === 'up' ? '↑' : metric.trend === 'down' ? '↓' : '→'} ${metric.change}
                        </div>
                    </div>
                </div>`).join('\n');

// 查找并替换时间戳
html = html.replace(
  /最後更新：\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}/,
  `最後更新：${timeString}`
);

// 替换新闻内容
html = html.replace(
  /<!-- NEWS_START -->[\s\S]*?<!-- NEWS_END -->/,
  `<!-- NEWS_START -->\n${newsHtml}\n                <!-- NEWS_END -->`
);

// 替换 Polymarket 内容
html = html.replace(
  /<!-- POLYMARKET_START -->[\s\S]*?<!-- POLYMARKET_END -->/,
  `<!-- POLYMARKET_START -->\n${polymarketHtml}\n                <!-- POLYMARKET_END -->`
);

// 替换关键指标
html = html.replace(
  /<!-- METRICS_START -->[\s\S]*?<!-- METRICS_END -->/,
  `<!-- METRICS_START -->\n${metricsHtml}\n            <!-- METRICS_END -->`
);

// 写入更新后的 HTML
fs.writeFileSync(htmlPath, html, 'utf-8');

console.log('✅ 页面更新完成！');
console.log(`更新时间：${timeString}`);
console.log(`新闻数量：${latestNews.length} 条`);
console.log(`Polymarket 市场：${polymarketData.length} 个`);
console.log(`关键指标：${keyMetrics.length} 个`);
