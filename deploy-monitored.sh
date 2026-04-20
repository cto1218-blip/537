#!/bin/bash
# 部署监控包装脚本 - 记录详细日志

LOG_FILE="/Users/hoimanszeto/.openclaw/workspace/deployment-detailed.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

echo "========================================" >> "$LOG_FILE"
echo "[$TIMESTAMP] 开始部署" >> "$LOG_FILE"
echo "========================================" >> "$LOG_FILE"

# 记录当前版本信息
echo "当前HEAD: $(git log -1 --format='%h - %s')" >> "$LOG_FILE"
echo "未提交的改动:" >> "$LOG_FILE"
git status --short >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

# 执行部署脚本并捕获所有输出
/Users/hoimanszeto/.openclaw/workspace/deploy-to-537.sh 2>&1 | tee -a "$LOG_FILE"

DEPLOY_STATUS=${PIPESTATUS[0]}

echo "" >> "$LOG_FILE"
echo "[$TIMESTAMP] 部署结束 - 状态码: $DEPLOY_STATUS" >> "$LOG_FILE"

if [ $DEPLOY_STATUS -eq 0 ]; then
    echo "✅ 部署成功" >> "$LOG_FILE"
else
    echo "❌ 部署失败" >> "$LOG_FILE"
fi

echo "========================================" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

exit $DEPLOY_STATUS
