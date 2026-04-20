const https = require('https');
const fs = require('fs');

// 嘗試多個地圖源
const sources = [
  'https://eoimages.gsfc.nasa.gov/images/imagerecords/73000/73909/world.topo.bathy.200407.3x5400x2700.jpg',
  'https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.json',
  'https://unpkg.com/world-atlas@2/countries-110m.json'
];

function tryDownload(url, index = 0) {
  console.log(`Trying source ${index + 1}/${sources.length}: ${url.substring(0, 60)}...`);
  
  const protocol = url.startsWith('https') ? https : require('http');
  
  protocol.get(url, {
    headers: {
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }
  }, (res) => {
    if (res.statusCode === 301 || res.statusCode === 302) {
      console.log(`Redirect to: ${res.headers.location}`);
      return tryDownload(res.headers.location, index);
    }
    
    if (res.statusCode !== 200) {
      console.error(`HTTP ${res.statusCode}`);
      if (index + 1 < sources.length) {
        return tryDownload(sources[index + 1], index + 1);
      }
      console.error('All sources failed');
      process.exit(1);
    }
    
    const data = [];
    res.on('data', chunk => data.push(chunk));
    res.on('end', () => {
      const buffer = Buffer.concat(data);
      console.log(`Downloaded ${buffer.length} bytes`);
      
      if (buffer.length < 500) {
        console.error('Too small, likely error page');
        if (index + 1 < sources.length) {
          return tryDownload(sources[index + 1], index + 1);
        }
        process.exit(1);
      }
      
      const ext = url.includes('.json') ? 'json' : (url.includes('.jpg') ? 'jpg' : 'png');
      fs.writeFileSync(`middle-east-map.${ext}`, buffer);
      console.log(`Saved as middle-east-map.${ext}`);
      
      if (ext !== 'json') {
        const base64 = buffer.toString('base64');
        const dataUri = `data:image/${ext};base64,${base64}`;
        fs.writeFileSync('map-base64.txt', dataUri);
        console.log(`Base64 length: ${base64.length}`);
      }
    });
  }).on('error', err => {
    console.error('Error:', err.message);
    if (index + 1 < sources.length) {
      tryDownload(sources[index + 1], index + 1);
    }
  });
}

tryDownload(sources[0], 0);
