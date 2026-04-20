const https = require('https');
const fs = require('fs');
const { exec } = require('child_process');

// 中東地區的 OSM 瓦片坐標（zoom level 4）
// 涵蓋伊朗、以色列、沙特等國
const tiles = [
  { z: 4, x: 9, y: 5 },   // 左上
  { z: 4, x: 10, y: 5 },  // 右上
  { z: 4, x: 9, y: 6 },   // 左下
  { z: 4, x: 10, y: 6 }   // 右下
];

let downloaded = 0;

tiles.forEach(tile => {
  const url = `https://tile.openstreetmap.org/${tile.z}/${tile.x}/${tile.y}.png`;
  const filename = `tile-${tile.x}-${tile.y}.png`;
  
  https.get(url, { headers: { 'User-Agent': 'Mozilla/5.0' } }, (res) => {
    const data = [];
    res.on('data', chunk => data.push(chunk));
    res.on('end', () => {
      fs.writeFileSync(filename, Buffer.concat(data));
      console.log(`Downloaded ${filename}`);
      downloaded++;
      
      if (downloaded === tiles.length) {
        console.log('All tiles downloaded');
        
        // 檢查是否有 ImageMagick/GraphicsMagick 來拼接
        exec('which convert magick gm', (err, stdout) => {
          if (stdout.trim()) {
            console.log('Image tool available, can merge tiles');
          } else {
            console.log('No image tool, using first tile as base');
            // 使用第一張瓦片作為基礎圖片
            const base64 = fs.readFileSync('tile-9-5.png').toString('base64');
            fs.writeFileSync('map-base64.txt', `data:image/png;base64,${base64}`);
            console.log('Base64 saved to map-base64.txt');
          }
        });
      }
    });
  }).on('error', err => console.error(`Error downloading ${filename}:`, err.message));
});
