#!/bin/bash

echo "🚀 开始GitHub部署设置..."
echo ""

# 检查Git是否安装
if ! command -v git &> /dev/null; then
    echo "❌ 未检测到Git，请先安装Git"
    echo "访问 https://git-scm.com/download/mac 下载安装"
    exit 1
fi

echo "✅ Git已安装"
echo ""

# 配置Git（如果还没配置过）
if [ -z "$(git config --global user.name)" ]; then
    echo "📝 首次使用Git，需要配置用户信息"
    echo "请输入你的GitHub用户名："
    read github_username
    git config --global user.name "$github_username"
    
    echo "请输入你的邮箱："
    read github_email
    git config --global user.email "$github_email"
    
    echo "✅ Git配置完成"
    echo ""
fi

# 初始化仓库
if [ ! -d ".git" ]; then
    echo "📦 初始化Git仓库..."
    git init
    echo "✅ Git仓库已初始化"
    echo ""
    
    # 添加HTML文件
    echo "📄 添加HTML文件到Git..."
    git add middle-east-tracker-zh-TW.html
    git commit -m "Initial commit: 中东局势追踪仪表板"
    echo "✅ 文件已提交"
    echo ""
    
    # 重命名默认分支为main
    git branch -M main
    echo "✅ 已切换到main分支"
    echo ""
    
    echo "📝 接下来请执行以下命令（替换成你的GitHub用户名）："
    echo ""
    echo "git remote add origin https://github.com/你的用户名/middle-east-tracker.git"
    echo "git push -u origin main"
    echo ""
else
    echo "⚠️  Git仓库已存在"
fi
