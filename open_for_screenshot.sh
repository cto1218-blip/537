#!/bin/bash
# 自动打开Chrome并提示截图

HTML_FILE="/Users/hoimanszeto/.openclaw/workspace/Ignite X&Y 创新机制升级.html"

echo "📱 即将打开浏览器，请按照以下步骤操作："
echo ""
echo "方法1（推荐 - 使用Chrome开发者工具）："
echo "1. 浏览器打开后，按 Cmd + Option + I 打开开发者工具"
echo "2. 按 Cmd + Shift + M 切换到移动设备模拟模式"
echo "3. 选择设备型号（如 iPhone 13 Pro Max）"
echo "4. 按 Cmd + Shift + P 打开命令面板"
echo "5. 输入 'screenshot' 选择 'Capture full size screenshot'"
echo "6. 长图会自动下载到你的下载文件夹"
echo ""
echo "方法2（手动截长图）："
echo "1. 浏览器打开后，按 Cmd + Shift + 5"
echo "2. 选择'截取选定窗口'"  
echo "3. 然后从上往下滚动截图（或使用第三方工具如 CleanShot X）"
echo ""
echo "按回车键继续..."
read

open -a "Google Chrome" "$HTML_FILE"
