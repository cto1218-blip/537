const https = require('https');
const fs = require('fs');

// Zoom 6，中東中心區域（伊朗+以色列+海灣）
const bigTile = { z: 6, x: 38, y: 24 };
const url = `https://tile.openstreetmap.org/${bigTile.z}/${bigTile.x}/${bigTile.y}.png`;

console.log(`Downloading: ${url}`);

https.get(url, { headers: { 'User-Agent': 'Mozilla/5.0' } }, (res) => {
  const data = [];
  let size = 0;
  res.on('data', chunk => { data.push(chunk); size += chunk.length; });
  res.on('end', () => {
    const buffer = Buffer.concat(data);
    console.log(`Downloaded ${buffer.length} bytes`);
    
    fs.writeFileSync('middle-east-map.png', buffer);
    
    const base64 = buffer.toString('base64');
    const dataUri = `data:image/png;base64,${base64}`;
    
    // 寫入完整 Base64 到文件
    fs.writeFileSync('map-base64-full.txt', dataUri);
    
    console.log(`Map saved: middle-east-map.png (${buffer.length} bytes)`);
    console.log(`Base64 total length: ${dataUri.length} chars`);
    console.log('Use map-base64-full.txt for embedding');
  });
}).on('error', err => console.error(err.message));
