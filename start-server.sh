#!/bin/bash

PORT=9999

echo "🚀 启动中东局势追踪服务器..."
echo ""

# 获取本机IP地址（Mac适配）
IP=$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null || echo "localhost")

echo "📱 在手机浏览器（Safari/Chrome）中访问："
echo ""
echo "   http://${IP}:${PORT}/middle-east-tracker-zh-TW.html"
echo ""
echo "⚠️  确保电脑和手机连接同一WiFi"
echo "⏹️  按 Ctrl+C 停止服务器"
echo ""
echo "服务器日志："
echo "-----------------------------------"

# 启动Python简单HTTP服务器
python3 -m http.server $PORT
