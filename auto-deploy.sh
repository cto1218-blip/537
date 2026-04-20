#!/bin/bash

echo "🔄 自动部署到云端..."

# 提交更新到Git
git add middle-east-tracker-zh-TW.html
git commit -m "Auto-update: $(date '+%Y-%m-%d %H:%M')"
git push origin main

echo "✅ 部署完成！1-2分钟后生效"
