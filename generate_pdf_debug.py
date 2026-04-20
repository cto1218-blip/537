#!/usr/bin/env python3
"""
调试版本：生成PDF前截图验证布局
"""
import asyncio
import os
from playwright.async_api import async_playwright

async def generate_pdf_debug():
    html_path = os.path.abspath("Ignite X&Y 创新机制升级.html")
    output_path = os.path.abspath("Ignite创新机制介绍.pdf")
    screenshot_path = os.path.abspath("debug_screenshot.png")
    
    print("🚀 正在启动浏览器...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        
        # 创建桌面版上下文
        context = await browser.new_context(
            viewport={"width": 1400, "height": 900},
            device_scale_factor=1,
            is_mobile=False,
            has_touch=False
        )
        
        page = await context.new_page()
        
        print(f"📄 正在加载HTML文件: {html_path}")
        await page.goto(f"file://{html_path}", wait_until="networkidle")
        await page.wait_for_timeout(2000)
        
        # 截图验证布局
        print(f"📸 生成截图用于验证: {screenshot_path}")
        await page.screenshot(path=screenshot_path, full_page=True)
        
        # 获取实际视口尺寸
        viewport_size = page.viewport_size
        print(f"📐 实际视口尺寸: {viewport_size}")
        
        # 检查是否有两列布局
        two_columns_visible = await page.evaluate("""
            () => {
                const twoColumns = document.querySelector('.two-columns');
                if (!twoColumns) return false;
                const style = window.getComputedStyle(twoColumns);
                return style.gridTemplateColumns !== '1fr';
            }
        """)
        print(f"✅ 两列布局是否显示: {two_columns_visible}")
        
        print("📑 正在生成PDF...")
        await page.pdf(
            path=output_path,
            format="A4",
            landscape=False,
            print_background=True,
            margin={"top": "8mm", "right": "8mm", "bottom": "8mm", "left": "8mm"},
            scale=0.75,
            prefer_css_page_size=False
        )
        
        print(f"✅ PDF已生成: {output_path}")
        file_size = os.path.getsize(output_path)
        print(f"📦 文件大小: {file_size / 1024 / 1024:.2f} MB")
        
        await browser.close()

if __name__ == "__main__":
    os.chdir("/Users/hoimanszeto/.openclaw/workspace")
    asyncio.run(generate_pdf_debug())
