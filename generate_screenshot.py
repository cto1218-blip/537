#!/usr/bin/env python3
"""
使用Playwright生成HTML页面长图
"""
import asyncio
import os
from playwright.async_api import async_playwright

async def generate_screenshot():
    html_path = os.path.abspath("Ignite X&Y 创新机制升级.html")
    output_path = os.path.abspath("Ignite创新机制介绍-长图.png")
    
    print("🚀 正在启动浏览器...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # 设置手机屏幕宽度（iPhone 13 Pro Max）
        await page.set_viewport_size({"width": 428, "height": 926})
        
        print(f"📄 正在加载HTML文件: {html_path}")
        await page.goto(f"file://{html_path}", wait_until="networkidle")
        
        # 等待页面渲染完成
        await page.wait_for_timeout(1000)
        
        print("📸 正在生成长图...")
        # 截取整个页面（全长图）
        await page.screenshot(
            path=output_path,
            full_page=True,
            type="png"
        )
        
        print(f"✅ 长图已生成: {output_path}")
        await browser.close()

if __name__ == "__main__":
    os.chdir("/Users/hoimanszeto/.openclaw/workspace")
    asyncio.run(generate_screenshot())
