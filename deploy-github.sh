#!/bin/bash

echo "🚀 GitHub Pages 部署脚本"
echo ""

# 检查是否已有git仓库
if [ ! -d ".git" ]; then
    echo "📦 初始化Git仓库..."
    git init
    git add middle-east-tracker-zh-TW.html
    git commit -m "Initial commit: 中东局势追踪仪表板"
    echo ""
    echo "✅ Git仓库已初始化"
    echo ""
    echo "📝 接下来请执行："
    echo "1. 在 GitHub 创建新仓库（名称如：middle-east-tracker）"
    echo "2. 执行以下命令："
    echo ""
    echo "   git remote add origin https://github.com/你的用户名/middle-east-tracker.git"
    echo "   git branch -M main"
    echo "   git push -u origin main"
    echo ""
    echo "3. 在GitHub仓库设置中启用 Pages（Settings → Pages → Source: main branch）"
    echo ""
    echo "4. 访问 https://你的用户名.github.io/middle-east-tracker/middle-east-tracker-zh-TW.html"
else
    echo "📤 更新到GitHub..."
    git add middle-east-tracker-zh-TW.html
    git commit -m "Update: $(date '+%Y-%m-%d %H:%M')"
    git push
    echo ""
    echo "✅ 更新完成！稍等1-2分钟后刷新页面即可看到最新数据"
fi
