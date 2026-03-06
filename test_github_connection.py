#!/usr/bin/env python3
"""
测试GitHub连接和仓库访问
"""

import subprocess
import requests
import json

def test_github_api():
    """测试GitHub API连接"""
    print("=== 测试GitHub API连接 ===")
    
    # 尝试访问GitHub API
    try:
        response = requests.get("https://api.github.com", timeout=10)
        if response.status_code == 200:
            print("✓ GitHub API可访问")
            return True
        else:
            print(f"⚠ GitHub API返回状态码: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ GitHub API连接失败: {e}")
        return False

def test_ssh_connection():
    """测试SSH连接"""
    print("\n=== 测试SSH连接 ===")
    
    try:
        # 测试SSH到GitHub
        result = subprocess.run(
            ["ssh", "-T", "git@github.com"],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if "successfully authenticated" in result.stderr.lower():
            print("✓ SSH认证成功")
            return True
        else:
            print(f"⚠ SSH认证结果: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"❌ SSH连接测试失败: {e}")
        return False

def test_repository_exists(username, repo_name):
    """测试仓库是否存在"""
    print(f"\n=== 测试仓库是否存在: {username}/{repo_name} ===")
    
    try:
        url = f"https://api.github.com/repos/{username}/{repo_name}"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            repo_info = response.json()
            print(f"✓ 仓库存在: {repo_info['full_name']}")
            print(f"   描述: {repo_info.get('description', '无描述')}")
            print(f"   可见性: {repo_info.get('visibility', '未知')}")
            print(f"   创建时间: {repo_info.get('created_at', '未知')}")
            return True
        elif response.status_code == 404:
            print(f"❌ 仓库不存在: {username}/{repo_name}")
            return False
        else:
            print(f"⚠ API返回状态码: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ 仓库检查失败: {e}")
        return False

def test_git_commands():
    """测试Git命令"""
    print("\n=== 测试Git命令 ===")
    
    commands = [
        ("git版本", ["git", "--version"]),
        ("远程仓库", ["git", "remote", "-v"]),
        ("当前分支", ["git", "branch", "-v"]),
        ("提交历史", ["git", "log", "--oneline", "-3"]),
    ]
    
    for name, cmd in commands:
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
            print(f"{name}:")
            if result.stdout:
                print(f"  {result.stdout.strip()}")
            if result.stderr:
                print(f"  错误: {result.stderr.strip()}")
        except Exception as e:
            print(f"{name}: 失败 - {e}")

def main():
    """主函数"""
    print("GitHub连接测试开始...\n")
    
    # 测试GitHub API
    api_ok = test_github_api()
    
    # 测试SSH连接
    ssh_ok = test_ssh_connection()
    
    # 测试仓库是否存在
    username = "ou_a565ab0428a04deaee3173345d273fab"
    repo_name = "news-brief-system"
    repo_exists = test_repository_exists(username, repo_name)
    
    # 测试Git命令
    test_git_commands()
    
    print("\n=== 测试总结 ===")
    print(f"GitHub API连接: {'✓' if api_ok else '❌'}")
    print(f"SSH认证: {'✓' if ssh_ok else '❌'}")
    print(f"仓库存在: {'✓' if repo_exists else '❌'}")
    
    if repo_exists:
        print("\n建议的仓库URL:")
        print(f"HTTPS: https://github.com/{username}/{repo_name}.git")
        print(f"SSH: git@github.com:{username}/{repo_name}.git")
    
    print("\n=== 下一步建议 ===")
    if not repo_exists:
        print("1. 确认仓库名称是否正确")
        print("2. 确认仓库是否已设置为公开(Public)")
        print("3. 确认有访问权限")
    elif not ssh_ok:
        print("1. 检查SSH密钥配置")
        print("2. 尝试使用HTTPS+Personal Access Token")
    else:
        print("尝试使用HTTPS协议推送:")
        print(f"  git remote set-url origin https://github.com/{username}/{repo_name}.git")
        print("然后使用Personal Access Token进行认证")

if __name__ == "__main__":
    main()