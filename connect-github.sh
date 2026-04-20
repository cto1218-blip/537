#!/bin/bash

echo "🔗 连接到GitHub仓库..."
echo ""
echo "请输入你的GitHub用户名："
read github_username

echo ""
echo "📝 添加远程仓库..."
git remote add origin "https://github.com/${github_username}/middle-east-tracker.git"

echo ""
echo "✅ 远程仓库已添加"
echo ""
echo "🚀 准备推送到GitHub..."
echo "如果是第一次推送，可能需要输入GitHub密码或访问令牌"
echo ""

git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 成功！你的页面将在1-2分钟后可以访问："
    echo ""
    echo "   https://${github_username}.github.io/middle-east-tracker/middle-east-tracker-zh-TW.html"
    echo ""
else
    echo ""
    echo "⚠️ 推送失败。可能需要配置GitHub认证"
    echo ""
    echo "解决方法："
    echo "1. 访问 https://github.com/settings/tokens"
    echo "2. 点击 'Generate new token (classic)'"
    echo "3. 勾选 'repo' 权限"
    echo "4. 生成令牌并保存"
    echo "5. 重新执行此脚本，密码处输入令牌"
fi
