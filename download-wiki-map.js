const https = require('https');
const fs = require('fs');

const url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Middle_East_political_map_2021.svg/2560px-Middle_East_political_map_2021.svg.png';

const options = {
  headers: {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
  }
};

https.get(url, options, (res) => {
  if (res.statusCode !== 200) {
    console.error(`HTTP ${res.statusCode}: ${res.statusMessage}`);
    process.exit(1);
  }
  
  const data = [];
  res.on('data', chunk => data.push(chunk));
  res.on('end', () => {
    const buffer = Buffer.concat(data);
    
    // 驗證是真正的圖片
    if (buffer.length < 1000) {
      console.error('Error: File too small, probably HTML error page');
      console.error(buffer.toString('utf8').substring(0, 200));
      process.exit(1);
    }
    
    // 檢查 PNG 魔術頭
    const header = buffer.toString('hex', 0, 8);
    if (header !== '89504e470d0a1a0a') {
      console.error('Error: Not a valid PNG file');
      console.error('First bytes:', header);
      process.exit(1);
    }
    
    console.log(`Downloaded ${buffer.length} bytes`);
    
    // 保存圖片
    fs.writeFileSync('middle-east-map.png', buffer);
    console.log('Saved to middle-east-map.png');
    
    // 生成 Base64 並保存到文件（避免終端截斷）
    const base64 = buffer.toString('base64');
    fs.writeFileSync('map-base64.txt', `data:image/png;base64,${base64}`);
    console.log('Base64 saved to map-base64.txt');
    console.log(`Base64 length: ${base64.length} chars`);
  });
}).on('error', err => {
  console.error('Network error:', err.message);
  process.exit(1);
});
