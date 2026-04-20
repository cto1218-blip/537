#!/bin/bash

echo "🔧 更新所有定时任务，添加自动部署功能..."
echo ""

# 所有任务ID
JOBS=(
  "7babccc8-d8fc-44ea-b3a8-293068b169d5"  # 08:00
  "8f134d8c-fb6f-4053-8f08-8483b495e976"  # 09:00
  "6ef40dd0-1321-45a8-b377-6bdacaf002da"  # 10:00
  "349562ee-ecab-41c7-b74c-9fe1b551e504"  # 11:00
  "3dda0b99-7979-479f-851e-808c3c70f1f1"  # 12:00
  "9407e9ac-21fe-4cca-ab8b-0413d3bdf1e2"  # 13:00
  "f86e4a6d-0e00-4317-b92c-a4f21660aad9"  # 14:00
  "11f10770-88e3-4918-8de6-56b4a17b7908"  # 15:00
  "655cea50-f97c-4e4b-a7c8-52a5bfba9212"  # 16:00
  "b3bc3e43-c641-4b96-8753-0b5b5bf92052"  # 17:00
  "c892d5e5-fd14-4d87-a65c-0727e8f95315"  # 18:00
  "623498a3-10b4-400f-9dda-9a4213338dd6"  # 19:00
  "b43c9b55-59b7-4566-a8de-3ae87f6a9a36"  # 20:00
  "0f489de8-608b-4994-9b4f-383cb2d7d905"  # 21:00
  "a1ba8050-df2a-4a79-ab2b-f4898c5aa21c"  # 22:00
  "33e75462-6b07-41ef-9ccb-59b8dfa76433"  # 23:00
  "7ba8a8fa-c85f-41e4-ad5f-d22f7f290fda"  # 00:00
  "8314a370-661c-4946-b6e4-913afc587fcf"  # 01:00
  "3e7339ac-1305-41b1-b421-e595c26ce9d5"  # 04:00
  "b095ba18-c182-4b40-927e-960d9a38a5e0"  # 07:00
)

echo "需要使用 OpenClaw cron API 更新这些任务"
echo "任务数量：${#JOBS[@]}"
echo ""
echo "由于需要API调用，请执行以下命令："
echo ""
for JOB_ID in "${JOBS[@]}"; do
  echo "openclaw cron update $JOB_ID --message-append '\n8. 更新完成後執行：cd ~/.openclaw/workspace && ./deploy-to-537.sh'"
done
