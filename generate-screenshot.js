const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

(async () => {
  const htmlPath = path.join(__dirname, 'Ignite创新机制介绍.html');
  const outputPath = path.join(__dirname, 'Ignite创新机制介绍-长图.png');

  console.log('正在启动浏览器...');
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  
  // 设置移动端视口（手机宽度）
  await page.setViewport({
    width: 750,
    height: 1334,
    deviceScaleFactor: 2
  });

  console.log('正在加载HTML文件...');
  await page.goto(`file://${htmlPath}`, {
    waitUntil: 'networkidle0'
  });

  console.log('正在生成长图...');
  // 获取页面完整高度
  const bodyHandle = await page.$('body');
  const { height } = await bodyHandle.boundingBox();
  await bodyHandle.dispose();

  // 设置视口高度为整个页面高度
  await page.setViewport({
    width: 750,
    height: Math.ceil(height),
    deviceScaleFactor: 2
  });

  // 截取整个页面
  await page.screenshot({
    path: outputPath,
    fullPage: true,
    type: 'png'
  });

  console.log(`✅ 长图已生成: ${outputPath}`);
  
  await browser.close();
})();
