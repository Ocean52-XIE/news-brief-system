#!/usr/bin/env python3
import os

# 模拟 save_and_push_to_github 函数中的逻辑
filename = "今日新闻简报_2026-03-05_test.md"

# 模拟函数开始
obsidian_dir = os.path.expanduser("~/my_obsidian")
daily_news_dir = os.path.join(obsidian_dir, "daily_news")

print(f"1. Obsidian目录: {obsidian_dir}")
print(f"2. Daily新闻目录: {daily_news_dir}")

# 保存到Obsidian
filepath = os.path.join(daily_news_dir, filename)
print(f"3. Obsidian文件路径: {filepath}")

# Git操作前保存当前目录
current_dir_before_git = os.getcwd()
print(f"4. Git操作前当前目录: {current_dir_before_git}")

# 切换到Obsidian目录进行Git操作
os.chdir(obsidian_dir)
print(f"5. Git操作时当前目录: {os.getcwd()}")

# Git操作完成后，保存到工作空间
workspace_dir = os.path.dirname(os.path.abspath(__file__))
print(f"6. 工作空间目录: {workspace_dir}")

# 切换回工作空间目录
os.chdir(workspace_dir)
workspace_path = os.path.join(workspace_dir, filename)
print(f"7. 工作空间文件路径: {workspace_path}")

# 恢复原目录
os.chdir(current_dir_before_git)
print(f"8. 恢复后当前目录: {os.getcwd()}")

print(f"\n最终文件应该保存在: {workspace_path}")
print(f"文件是否存在: {os.path.exists(workspace_path)}")