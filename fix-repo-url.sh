#!/bin/bash

echo "🔧 修正远程仓库地址..."
echo ""

# 1. 删除旧的远程仓库
echo "🗑️  删除旧的远程仓库配置..."
git remote remove origin

# 2. 添加正确的远程仓库
echo "📝 添加新的远程仓库..."
git remote add origin https://github.com/cto1218-blip/537.git

# 3. 显示当前配置
echo ""
echo "✅ 远程仓库已更新为："
git remote -v

echo ""
echo "🚀 现在可以推送了..."
echo ""

# 4. 推送到GitHub
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 推送成功！"
    echo ""
    echo "接下来："
    echo "1. 访问 https://github.com/cto1218-blip/537"
    echo "2. 点击 Settings → Pages"
    echo "3. Source 选择 main 分支"
    echo "4. 点击 Save"
    echo "5. 等待1-2分钟后访问："
    echo ""
    echo "   https://cto1218-blip.github.io/537/middle-east-tracker-zh-TW.html"
    echo ""
else
    echo ""
    echo "❌ 推送失败，请检查："
    echo "1. 仓库 https://github.com/cto1218-blip/537 是否已创建"
    echo "2. Personal Access Token 是否正确"
fi
