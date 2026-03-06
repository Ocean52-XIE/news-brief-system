#!/usr/bin/env python3
import datetime
import os
import sys

print("=" * 60)
print("测试cron环境")
print(f"运行时间: {datetime.datetime.now()}")
print(f"Python路径: {sys.executable}")
print(f"工作目录: {os.getcwd()}")
print(f"用户: {os.getenv('USER')}")
print(f"HOME: {os.getenv('HOME')}")
print(f"PATH: {os.getenv('PATH')}")

# 测试Tavily脚本
try:
    script_path = os.path.expanduser("~/.openclaw/workspace/skills/openclaw-tavily-search/scripts/tavily_search.py")
    print(f"\nTavily脚本路径: {script_path}")
    print(f"脚本存在: {os.path.exists(script_path)}")
    
    # 尝试导入
    import subprocess
    result = subprocess.run(
        ["python3", script_path, "--query", "测试", "--max-results", "1", "--format", "brave"],
        capture_output=True,
        text=True
    )
    print(f"\nTavily脚本返回码: {result.returncode}")
    if result.returncode == 0:
        print("✅ Tavily脚本运行成功")
    else:
        print(f"❌ Tavily脚本运行失败: {result.stderr}")
        
except Exception as e:
    print(f"❌ 测试过程中出错: {e}")

print("\n" + "=" * 60)