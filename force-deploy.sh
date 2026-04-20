#!/bin/bash

echo "🔄 强制重新部署到GitHub..."
echo ""

# 添加一个空行到README（触发改动）
if [ ! -f README.md ]; then
    echo "# 中东局势追踪" > README.md
    echo "" >> README.md
    echo "实时追踪2026年美以伊冲突局势" >> README.md
else
    echo "" >> README.md
fi

# 添加到Git
git add README.md middle-east-tracker-zh-TW.html

# 创建提交
git commit -m "Update: 强制重新部署 $(date '+%Y-%m-%d %H:%M')"

# 推送
git push origin main

echo ""
echo "✅ 推送完成！"
echo "⏳ 等待1-2分钟后刷新网页查看"
