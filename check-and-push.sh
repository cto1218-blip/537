#!/bin/bash

echo "🔍 检查GitHub仓库状态..."
echo ""

GITHUB_USER="cto1218-blip"
REPO_NAME="middle-east-tracker"

# 检查仓库是否存在
echo "📡 检查远程仓库是否存在..."
if curl -s -o /dev/null -w "%{http_code}" "https://github.com/${GITHUB_USER}/${REPO_NAME}" | grep -q "200"; then
    echo "✅ 仓库已存在"
else
    echo "❌ 仓库不存在！"
    echo ""
    echo "请先在GitHub创建仓库："
    echo "1. 访问 https://github.com/new"
    echo "2. Repository name: ${REPO_NAME}"
    echo "3. 选择 Public"
    echo "4. 不要勾选任何选项"
    echo "5. 点击 Create repository"
    echo ""
    echo "创建完成后重新运行此脚本"
    exit 1
fi

echo ""
echo "🚀 开始推送..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 推送成功！"
    echo ""
    echo "接下来："
    echo "1. 访问 https://github.com/${GITHUB_USER}/${REPO_NAME}"
    echo "2. 点击 Settings → Pages"
    echo "3. Source 选择 main 分支"
    echo "4. 点击 Save"
    echo "5. 等待1-2分钟后访问："
    echo ""
    echo "   https://${GITHUB_USER}.github.io/${REPO_NAME}/middle-east-tracker-zh-TW.html"
    echo ""
else
    echo ""
    echo "❌ 推送失败"
fi
