const fs = require('fs');

// 簡單方案：使用其中一張較大的瓦片（zoom 5 更詳細）
const https = require('https');

// 下載更大範圍的單張瓦片（zoom 3，覆蓋整個中東）
const url = 'https://tile.openstreetmap.org/3/4/2.png';

https.get(url, { headers: { 'User-Agent': 'Mozilla/5.0' } }, (res) => {
  const data = [];
  res.on('data', chunk => data.push(chunk));
  res.on('end', () => {
    const buffer = Buffer.concat(data);
    console.log(`Downloaded ${buffer.length} bytes`);
    
    // 保存為圖片
    fs.writeFileSync('middle-east-map.png', buffer);
    
    // 轉 Base64
    const base64 = buffer.toString('base64');
    const dataUri = `data:image/png;base64,${base64}`;
    fs.writeFileSync('map-base64.txt', dataUri);
    
    console.log(`Saved middle-east-map.png (${buffer.length} bytes)`);
    console.log(`Base64 length: ${dataUri.length} chars`);
  });
}).on('error', err => console.error(err.message));
