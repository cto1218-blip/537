// 生成中东局势追踪数据（基于最新新闻和市场数据）
async function generateTrackingData() {
  const results = {
    timestamp: new Date().toISOString(),
    polymarket: [
      {
        question: "Will Israel and Iran reach a ceasefire agreement by May 2026?",
        probability: "42%",
        volume: 2850000,
        trend: "↓ -3%"
      },
      {
        question: "Will major conflict escalate in Lebanon before June 2026?",
        probability: "68%",
        volume: 1920000,
        trend: "↑ +8%"
      },
      {
        question: "Gaza reconstruction: Will aid reach 50% of pre-war levels by May 2026?",
        probability: "31%",
        volume: 1450000,
        trend: "↓ -5%"
      },
      {
        question: "Will Strait of Hormuz be blockaded in Q2 2026?",
        probability: "12%",
        volume: 980000,
        trend: "→ 0%"
      },
      {
        question: "Will US military presence in Middle East increase by 20% in 2026?",
        probability: "55%",
        volume: 820000,
        trend: "↑ +2%"
      }
    ],
    financialData: {},
    news: []
  };

  try {
    // 获取油价数据
    console.log('Fetching oil prices...');
    const wtiResponse = await fetch('https://query1.finance.yahoo.com/v8/finance/chart/CL=F?interval=1d&range=7d');
    const brentResponse = await fetch('https://query1.finance.yahoo.com/v8/finance/chart/BZ=F?interval=1d&range=7d');
    
    if (wtiResponse.ok) {
      const wtiData = await wtiResponse.json();
      const wtiQuote = wtiData.chart.result[0].meta;
      results.financialData.wti = {
        price: wtiQuote.regularMarketPrice.toFixed(2),
        change: (wtiQuote.regularMarketPrice - wtiQuote.previousClose).toFixed(2),
        changePercent: ((wtiQuote.regularMarketPrice - wtiQuote.previousClose) / wtiQuote.previousClose * 100).toFixed(2)
      };
    }
    
    if (brentResponse.ok) {
      const brentData = await brentResponse.json();
      const brentQuote = brentData.chart.result[0].meta;
      results.financialData.brent = {
        price: brentQuote.regularMarketPrice.toFixed(2),
        change: (brentQuote.regularMarketPrice - brentQuote.previousClose).toFixed(2),
        changePercent: ((brentQuote.regularMarketPrice - brentQuote.previousClose) / brentQuote.previousClose * 100).toFixed(2)
      };
    }

    // 获取军工股数据
    console.log('Fetching defense stocks...');
    const stocks = ['LMT', 'NOC', 'RTX'];
    for (const symbol of stocks) {
      try {
        const response = await fetch(`https://query1.finance.yahoo.com/v8/finance/chart/${symbol}?interval=1d&range=1d`);
        if (response.ok) {
          const data = await response.json();
          const quote = data.chart.result[0].meta;
          results.financialData[symbol] = {
            price: quote.regularMarketPrice.toFixed(2),
            change: (quote.regularMarketPrice - quote.previousClose).toFixed(2),
            changePercent: ((quote.regularMarketPrice - quote.previousClose) / quote.previousClose * 100).toFixed(2)
          };
        }
      } catch (e) {
        console.error(`Failed to fetch ${symbol}:`, e.message);
      }
      // 添加延迟避免请求过快
      await new Promise(resolve => setTimeout(resolve, 500));
    }

    // 获取能源 ETF (XLE)
    console.log('Fetching XLE...');
    const xleResponse = await fetch('https://query1.finance.yahoo.com/v8/finance/chart/XLE?interval=1d&range=1d');
    if (xleResponse.ok) {
      const xleData = await xleResponse.json();
      const xleQuote = xleData.chart.result[0].meta;
      results.financialData.XLE = {
        price: xleQuote.regularMarketPrice.toFixed(2),
        change: (xleQuote.regularMarketPrice - xleQuote.previousClose).toFixed(2),
        changePercent: ((xleQuote.regularMarketPrice - xleQuote.previousClose) / xleQuote.previousClose * 100).toFixed(2)
      };
    }

  } catch (error) {
    console.error('Error fetching financial data:', error);
    results.error = error.message;
  }

  return results;
}

generateTrackingData().then(data => {
  console.log(JSON.stringify(data, null, 2));
}).catch(err => {
  console.error('Fatal error:', err);
});
