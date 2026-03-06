#!/usr/bin/env python3
import os

print("测试文件保存位置")
print(f"当前目录: {os.getcwd()}")
print(f"脚本目录: {os.path.dirname(os.path.abspath(__file__))}")

# 测试保存文件
filename = "test_file.md"
workspace_dir = os.path.dirname(os.path.abspath(__file__))
workspace_path = os.path.join(workspace_dir, filename)

print(f"\n工作空间路径: {workspace_path}")
print(f"文件是否存在: {os.path.exists(workspace_path)}")

# 创建文件
with open(workspace_path, 'w') as f:
    f.write("测试内容")

print(f"文件已创建: {workspace_path}")
print(f"文件现在是否存在: {os.path.exists(workspace_path)}")