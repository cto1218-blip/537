#!/bin/bash

echo "🚀 部署到GitHub仓库 537"
echo "========================================"
echo ""

# 检查Git状态
if [ ! -d ".git" ]; then
    echo "❌ 错误：不在Git仓库中"
    exit 1
fi

# 添加HTML文件
echo "📄 添加文件..."
git add middle-east-tracker-zh-TW.html

# 检查是否有改动需要提交
if git diff --cached --quiet; then
    echo "⚠️  没有新的改动需要提交"
    echo "最后提交: $(git log -1 --format='%h - %s')"
else
    echo "💾 创建提交..."
    git commit -m "Update: 中东局势追踪 $(date '+%Y-%m-%d %H:%M')"
    
    if [ $? -ne 0 ]; then
        echo "❌ 提交失败！"
        exit 1
    fi
fi

# 配置远程仓库
echo "🔗 配置远程仓库..."
if git remote get-url origin > /dev/null 2>&1; then
    CURRENT_URL=$(git remote get-url origin)
    TARGET_URL="https://github.com/cto1218-blip/537.git"
    
    if [ "$CURRENT_URL" != "$TARGET_URL" ]; then
        echo "   更新远程仓库地址..."
        git remote set-url origin "$TARGET_URL"
    else
        echo "   ✅ 远程仓库配置正确"
    fi
else
    echo "   添加远程仓库..."
    git remote add origin https://github.com/cto1218-blip/537.git
fi

echo ""
echo "🚀 推送到GitHub..."

# 使用force push避免冲突，并捕获输出
OUTPUT=$(git push -f origin main 2>&1)
PUSH_STATUS=$?

if [ $PUSH_STATUS -eq 0 ]; then
    echo ""
    echo "✅ 推送成功！"
    echo "   Commit: $(git log -1 --format='%h - %s')"
    echo ""
    echo "📱 页面地址："
    echo "   https://cto1218-blip.github.io/537/middle-east-tracker-zh-TW.html"
    echo ""
    exit 0
else
    echo ""
    echo "❌ 推送失败！"
    echo ""
    echo "错误详情："
    echo "$OUTPUT"
    echo ""
    echo "常见问题："
    echo "1. Personal Access Token 过期或错误"
    echo "2. 网络连接问题"
    echo "3. Token权限不足（需要 repo 权限）"
    echo ""
    exit 1
fi
