#!/usr/bin/env node
/**
 * 中东局势仪表板 - 数据自动更新脚本
 * 数据源：
 * - 新闻：BBC/CNN/新华社 RSS feeds
 * - 市场：Yahoo Finance API (油价/军工股)
 * - 预测市场：Polymarket API
 */

const https = require('https');
const http = require('http');
const fs = require('fs');
const { parseString } = require('xml2js');

// ==================== 配置 ====================
const CONFIG = {
  RSS_FEEDS: [
    'https://feeds.bbci.co.uk/news/world/middle_east/rss.xml',
    'http://rss.cnn.com/rss/cnn_latest.rss',
    'https://news.google.com/rss/search?q=middle+east+OR+israel+OR+iran&hl=en-US&gl=US&ceid=US:en'
  ],
  POLYMARKET_API: 'https://gamma-api.polymarket.com/events',
  YAHOO_FINANCE_SYMBOLS: ['XLE', 'LMT', 'NOC', 'RTX', 'CL=F'], // 能源ETF, 军工股, 原油期货
  OUTPUT_FILE: './middle-east-data.json',
  HTML_FILE: './middle-east-tracker-zh-TW.html',
  MAX_NEWS_ITEMS: 20
};

// ==================== 工具函数 ====================
function httpGet(url) {
  return new Promise((resolve, reject) => {
    const client = url.startsWith('https') ? https : http;
    client.get(url, {
      headers: { 'User-Agent': 'Mozilla/5.0 (compatible; MiddleEastTracker/1.0)' }
    }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => resolve(data));
    }).on('error', reject);
  });
}

function parseRSS(xml) {
  return new Promise((resolve, reject) => {
    parseString(xml, (err, result) => {
      if (err) reject(err);
      else resolve(result);
    });
  });
}

// ==================== 数据获取 ====================
async function fetchNews() {
  console.log('📰 获取新闻数据...');
  const allNews = [];
  
  for (const feedUrl of CONFIG.RSS_FEEDS) {
    try {
      const xml = await httpGet(feedUrl);
      const parsed = await parseRSS(xml);
      const items = parsed.rss?.channel?.[0]?.item || [];
      
      items.forEach(item => {
        const title = item.title?.[0] || '';
        const link = item.link?.[0] || '';
        const pubDate = item.pubDate?.[0] || '';
        const description = item.description?.[0] || '';
        
        // 过滤中东相关关键词
        const keywords = ['israel', 'iran', 'gaza', 'middle east', 'hamas', 'hezbollah', 
                         'syria', 'iraq', 'lebanon', '以色列', '伊朗', '中东', '加沙'];
        const isRelevant = keywords.some(kw => 
          (title + description).toLowerCase().includes(kw)
        );
        
        if (isRelevant) {
          allNews.push({
            title: title.replace(/<[^>]+>/g, ''),
            link,
            pubDate: new Date(pubDate).toISOString(),
            source: feedUrl.includes('bbc') ? 'BBC' : 
                   feedUrl.includes('cnn') ? 'CNN' : '新华社',
            description: description.replace(/<[^>]+>/g, '').substring(0, 200)
          });
        }
      });
    } catch (err) {
      console.error(`❌ 获取 ${feedUrl} 失败:`, err.message);
    }
  }
  
  // 按时间排序，取最新的
  allNews.sort((a, b) => new Date(b.pubDate) - new Date(a.pubDate));
  return allNews.slice(0, CONFIG.MAX_NEWS_ITEMS);
}

async function fetchPolymarket() {
  console.log('🎲 获取 Polymarket 预测数据...');
  try {
    const data = await httpGet(CONFIG.POLYMARKET_API);
    const markets = JSON.parse(data);
    
    // 筛选中东相关市场
    const relevant = markets.filter(m => 
      m.question?.toLowerCase().includes('israel') ||
      m.question?.toLowerCase().includes('iran') ||
      m.question?.toLowerCase().includes('middle east') ||
      m.question?.toLowerCase().includes('war')
    ).slice(0, 5);
    
    return relevant.map(m => ({
      question: m.question,
      probability: Math.round(m.outcomePrices?.[0] * 100) || 0,
      volume: m.volume24hr || 0,
      url: `https://polymarket.com/event/${m.slug}`
    }));
  } catch (err) {
    console.error('❌ Polymarket 获取失败:', err.message);
    return [];
  }
}

async function fetchMarketData() {
  console.log('📈 获取市场数据...');
  const results = {};
  
  for (const symbol of CONFIG.YAHOO_FINANCE_SYMBOLS) {
    try {
      // Yahoo Finance Quote API (无需认证)
      const url = `https://query1.finance.yahoo.com/v8/finance/chart/${symbol}?interval=1d&range=5d`;
      const data = await httpGet(url);
      const json = JSON.parse(data);
      
      const quote = json.chart?.result?.[0];
      if (quote) {
        const prices = quote.indicators?.quote?.[0];
        const meta = quote.meta;
        
        results[symbol] = {
          price: meta.regularMarketPrice || 0,
          change: meta.regularMarketPrice - meta.chartPreviousClose || 0,
          changePercent: ((meta.regularMarketPrice / meta.chartPreviousClose - 1) * 100).toFixed(2),
          currency: meta.currency,
          name: symbol === 'CL=F' ? '原油期货' :
                symbol === 'XLE' ? '能源ETF' :
                symbol === 'LMT' ? '洛克希德马丁' :
                symbol === 'NOC' ? '诺斯罗普格鲁曼' :
                symbol === 'RTX' ? '雷神科技' : symbol
        };
      }
    } catch (err) {
      console.error(`❌ 获取 ${symbol} 失败:`, err.message);
    }
  }
  
  return results;
}

// ==================== 数据整合与输出 ====================
async function main() {
  console.log('🚀 开始更新中东局势仪表板数据...\n');
  
  const [news, polymarket, market] = await Promise.all([
    fetchNews(),
    fetchPolymarket(),
    fetchMarketData()
  ]);
  
  const output = {
    lastUpdate: new Date().toISOString(),
    news,
    polymarket,
    market
  };
  
  // 保存 JSON
  fs.writeFileSync(CONFIG.OUTPUT_FILE, JSON.stringify(output, null, 2));
  console.log(`\n✅ 数据已保存到 ${CONFIG.OUTPUT_FILE}`);
  console.log(`📊 统计: ${news.length} 条新闻 | ${polymarket.length} 个预测市场 | ${Object.keys(market).length} 个市场指标`);
  
  // 更新 HTML 中的数据时间戳
  if (fs.existsSync(CONFIG.HTML_FILE)) {
    let html = fs.readFileSync(CONFIG.HTML_FILE, 'utf-8');
    const timestamp = new Date().toLocaleString('zh-TW', { timeZone: 'Asia/Taipei' });
    html = html.replace(
      /最後更新：.*?</,
      `最後更新：${timestamp} (自動)<`
    );
    fs.writeFileSync(CONFIG.HTML_FILE, html);
    console.log(`✅ HTML 时间戳已更新`);
  }
}

// 执行
main().catch(err => {
  console.error('💥 更新失败:', err);
  process.exit(1);
});
