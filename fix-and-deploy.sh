#!/bin/bash

echo "🔧 修复Git推送问题..."
echo ""

# 1. 只添加HTML文件
echo "📄 添加HTML文件..."
git add middle-east-tracker-zh-TW.html

# 2. 创建提交
echo "💾 创建提交..."
git commit -m "Initial commit: 中东局势追踪仪表板"

# 3. 确保在main分支
echo "🌿 确认分支..."
git branch -M main

# 4. 检查是否已有远程仓库
if git remote get-url origin > /dev/null 2>&1; then
    echo "✅ 远程仓库已存在"
else
    echo "📝 请输入你的GitHub用户名："
    read github_username
    git remote add origin "https://github.com/${github_username}/middle-east-tracker.git"
    echo "✅ 远程仓库已添加"
fi

# 5. 推送到GitHub
echo ""
echo "🚀 推送到GitHub..."
echo "如果提示输入密码，请粘贴你的Personal Access Token"
echo ""

git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 推送成功！"
    echo ""
    echo "接下来："
    echo "1. 访问你的GitHub仓库"
    echo "2. 点击 Settings → Pages"
    echo "3. Source 选择 main 分支"
    echo "4. 点击 Save"
    echo "5. 等待1-2分钟后访问："
    echo ""
    GITHUB_USER=$(git remote get-url origin | sed 's|https://github.com/||' | sed 's|/.*||')
    echo "   https://${GITHUB_USER}.github.io/middle-east-tracker/middle-east-tracker-zh-TW.html"
    echo ""
else
    echo ""
    echo "❌ 推送失败"
    echo ""
    echo "请检查："
    echo "1. GitHub用户名是否正确"
    echo "2. Personal Access Token是否正确"
    echo "3. Token权限是否包含 repo"
fi
