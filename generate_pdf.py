#!/usr/bin/env python3
"""
使用Playwright生成HTML页面PDF（强制桌面版布局）
"""
import asyncio
import os
from playwright.async_api import async_playwright

async def generate_pdf():
    html_path = os.path.abspath("Ignite X&Y 创新机制升级.html")
    output_path = os.path.abspath("Ignite创新机制介绍.pdf")
    
    print("🚀 正在启动浏览器...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        # 创建桌面版上下文（非移动设备）
        context = await browser.new_context(
            viewport={"width": 1400, "height": 900},
            device_scale_factor=1,
            is_mobile=False,
            has_touch=False,
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        
        page = await context.new_page()
        
        print(f"📄 正在加载HTML文件: {html_path}")
        await page.goto(f"file://{html_path}", wait_until="networkidle")
        
        # 等待页面渲染完成
        await page.wait_for_timeout(2000)
        
        print("📑 正在生成PDF（桌面版布局）...")
        await page.pdf(
            path=output_path,
            format="A4",
            landscape=False,  # 竖版
            print_background=True,
            margin={
                "top": "8mm",
                "right": "8mm",
                "bottom": "8mm",
                "left": "8mm"
            },
            scale=0.75,  # 适当缩小以适配A4
            prefer_css_page_size=False,
            display_header_footer=False
        )
        
        print(f"✅ PDF已生成: {output_path}")
        
        # 获取文件大小
        file_size = os.path.getsize(output_path)
        print(f"📦 文件大小: {file_size / 1024 / 1024:.2f} MB")
        
        await browser.close()

if __name__ == "__main__":
    os.chdir("/Users/hoimanszeto/.openclaw/workspace")
    asyncio.run(generate_pdf())
