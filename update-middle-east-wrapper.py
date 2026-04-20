#!/usr/bin/env python3
import sys
import json

# 读取临时 JSON 文件
with open('/tmp/middle-east-update.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 调用主脚本
import subprocess
subprocess.run(['python3', 'update-middle-east.py', json.dumps(data, ensure_ascii=False)])
