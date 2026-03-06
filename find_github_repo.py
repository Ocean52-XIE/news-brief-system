#!/usr/bin/env python3
"""
查找GitHub仓库的脚本
"""

import requests
import sys

def check_repository(owner, repo):
    """检查仓库是否存在"""
    url = f"https://api.github.com/repos/{owner}/{repo}"
    
    try:
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            return {
                "exists": True,
                "name": data["full_name"],
                "description": data.get("description", "无描述"),
                "visibility": data.get("visibility", "public"),
                "url": data["html_url"],
                "clone_url": data["clone_url"],
                "ssh_url": data["ssh_url"]
            }
        elif response.status_code == 404:
            return {"exists": False, "reason": "仓库不存在"}
        elif response.status_code == 403:
            return {"exists": True, "reason": "仓库可能是私有的或无访问权限"}
        else:
            return {"exists": False, "reason": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"exists": False, "reason": str(e)}

def suggest_variations(owner, repo):
    """建议可能的变体"""
    variations = []
    
    # 可能的用户名变体
    owner_variants = [
        owner,
        owner.replace("ou_", ""),
        owner.replace("_", "-"),
        owner.replace("_", ""),
        "openclaw",
        "news-agent",
        "xieyq"  # 系统用户名
    ]
    
    # 可能的仓库名变体
    repo_variants = [
        repo,
        "news-brief-system",
        "news_brief_system",
        "news-brief",
        "newsbrief",
        "openclaw-news",
        "daily-news-brief"
    ]
    
    return owner_variants, repo_variants

def main():
    print("=== GitHub仓库查找工具 ===\n")
    
    # 当前尝试的仓库
    current_owner = "ou_a565ab0428a04deaee3173345d273fab"
    current_repo = "news-brief-system"
    
    print(f"当前配置: {current_owner}/{current_repo}")
    print(f"HTTPS URL: https://github.com/{current_owner}/{current_repo}.git")
    print(f"SSH URL: git@github.com:{current_owner}/{current_repo}.git")
    
    print("\n" + "="*50 + "\n")
    
    # 检查当前配置
    print("检查当前配置...")
    result = check_repository(current_owner, current_repo)
    
    if result["exists"]:
        print(f"✅ 仓库存在: {result['name']}")
        print(f"   描述: {result['description']}")
        print(f"   可见性: {result['visibility']}")
        print(f"   URL: {result['url']}")
        print(f"   Clone URL: {result['clone_url']}")
        print(f"   SSH URL: {result['ssh_url']}")
        return
    else:
        print(f"❌ {result['reason']}")
    
    print("\n" + "="*50 + "\n")
    
    # 建议可能的变体
    print("尝试可能的变体...")
    owner_variants, repo_variants = suggest_variations(current_owner, current_repo)
    
    found = False
    for owner in owner_variants[:3]:  # 只检查前3个用户名变体
        for repo in repo_variants[:3]:  # 只检查前3个仓库名变体
            if owner == current_owner and repo == current_repo:
                continue  # 跳过已检查的
            
            print(f"尝试: {owner}/{repo}...", end=" ")
            result = check_repository(owner, repo)
            
            if result["exists"]:
                print("✅ 找到!")
                print(f"   名称: {result['name']}")
                print(f"   URL: {result['url']}")
                found = True
                break
            else:
                print("❌ 未找到")
        
        if found:
            break
    
    if not found:
        print("\n" + "="*50 + "\n")
        print("未找到匹配的仓库。")
        print("\n建议：")
        print("1. 确认GitHub用户名是否正确")
        print("2. 确认仓库名称是否正确")
        print("3. 确认仓库是否已设置为公开(Public)")
        print("4. 尝试在浏览器中直接访问:")
        print(f"   https://github.com/{current_owner}/{current_repo}")
        print("\n可能的用户名:")
        for owner in owner_variants:
            print(f"   - {owner}")
        print("\n可能的仓库名:")
        for repo in repo_variants:
            print(f"   - {repo}")

if __name__ == "__main__":
    main()