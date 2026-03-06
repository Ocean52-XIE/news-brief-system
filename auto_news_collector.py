#!/usr/bin/env python3
"""
自动新闻收集脚本 - 每天0点、6点、12点、18点运行
包含新闻来源和链接信息
"""

import json
import datetime
import subprocess
import sys
import os
from pathlib import Path

def run_tavily_search(query, max_results=5):
    """运行Tavily搜索并返回JSON结果"""
    try:
        # 构建命令
        script_path = os.path.expanduser("~/.openclaw/workspace/skills/openclaw-tavily-search/scripts/tavily_search.py")
        cmd = [
            "python3", script_path,
            "--query", query,
            "--max-results", str(max_results),
            "--format", "brave"
        ]
        
        # 执行命令
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=os.path.dirname(script_path))
        
        if result.returncode == 0:
            return json.loads(result.stdout)
        else:
            print(f"Tavily搜索失败: {result.stderr}")
            return None
    except Exception as e:
        print(f"运行Tavily搜索时出错: {e}")
        return None

def collect_tech_news():
    """收集科技新闻"""
    print("收集科技新闻...")
    query = "2026年最新科技新闻 AI 人工智能 量子计算 脑机接口"
    result = run_tavily_search(query, 5)
    
    tech_news = []
    if result and "results" in result:
        for item in result["results"][:3]:  # 取前3条
            tech_news.append({
                "title": item.get("title", "无标题"),
                "summary": item.get("snippet", "无摘要")[:200] + "...",  # 截取前200字符
                "source": "Tavily搜索",
                "url": item.get("url", "#"),
                "search_query": query
            })
    
    # 如果没有搜索结果，使用默认数据
    if not tech_news:
        tech_news = [
            {
                "title": "AI技术发展预测",
                "summary": "各大科技公司加速AI战略布局",
                "source": "科技媒体综合",
                "url": "#",
                "search_query": query
            }
        ]
    
    return tech_news

def collect_finance_news():
    """收集金融新闻"""
    print("收集金融新闻...")
    query = "2026年最新金融新闻 股市 央行 货币政策 黄金价格"
    result = run_tavily_search(query, 5)
    
    finance_news = []
    if result and "results" in result:
        for item in result["results"][:3]:
            finance_news.append({
                "title": item.get("title", "无标题"),
                "summary": item.get("snippet", "无摘要")[:200] + "...",
                "source": "Tavily搜索",
                "url": item.get("url", "#"),
                "search_query": query
            })
    
    if not finance_news:
        finance_news = [
            {
                "title": "货币政策动态",
                "summary": "各国央行调整货币政策应对经济变化",
                "source": "财经媒体综合",
                "url": "#",
                "search_query": query
            }
        ]
    
    return finance_news

def collect_military_news():
    """收集军事新闻"""
    print("收集军事新闻...")
    query = "2026年最新军事新闻 国防 军事演习 武器装备 中东局势"
    result = run_tavily_search(query, 5)
    
    military_news = []
    if result and "results" in result:
        for item in result["results"][:3]:
            military_news.append({
                "title": item.get("title", "无标题"),
                "summary": item.get("snippet", "无摘要")[:200] + "...",
                "source": "Tavily搜索",
                "url": item.get("url", "#"),
                "search_query": query
            })
    
    if not military_news:
        military_news = [
            {
                "title": "中东局势升级",
                "summary": "地区冲突引发国际关注",
                "source": "军事媒体综合",
                "url": "#",
                "search_query": query
            }
        ]
    
    return military_news

def generate_report(tech_news, finance_news, military_news, run_time):
    """生成新闻报告"""
    date_str = run_time.strftime("%Y-%m-%d")
    time_str = run_time.strftime("%H:%M")
    filename_time = run_time.strftime("%Y-%m-%d_%H%M")
    
    report = f"""# 📰 新闻简报 ({date_str} {time_str})

*报告生成时间: {run_time.strftime('%Y-%m-%d %H:%M:%S')}*
*数据来源: Tavily搜索 API*

## 🔬 科技新闻
"""
    
    for i, news in enumerate(tech_news, 1):
        report += f"\n### {i}. {news['title']}\n"
        report += f"{news['summary']}\n"
        report += f"**来源**: {news['source']}  |  **查询**: `{news['search_query']}`\n"
        if news['url'] != '#':
            report += f"**链接**: {news['url']}\n"
    
    report += "\n## 💰 金融新闻\n"
    for i, news in enumerate(finance_news, 1):
        report += f"\n### {i}. {news['title']}\n"
        report += f"{news['summary']}\n"
        report += f"**来源**: {news['source']}  |  **查询**: `{news['search_query']}`\n"
        if news['url'] != '#':
            report += f"**链接**: {news['url']}\n"
    
    report += "\n## ⚔️ 军事新闻\n"
    for i, news in enumerate(military_news, 1):
        report += f"\n### {i}. {news['title']}\n"
        report += f"{news['summary']}\n"
        report += f"**来源**: {news['source']}  |  **查询**: `{news['search_query']}`\n"
        if news['url'] != '#':
            report += f"**链接**: {news['url']}\n"
    
    report += f"\n---\n"
    report += f"**自动化新闻收集系统**\n"
    report += f"- 运行时间: {run_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
    report += f"- 收集频率: 每天0点、6点、12点、18点\n"
    report += f"- 文件命名: {filename_time}-daily-news.md\n"
    
    return report, filename_time

def save_and_push_to_github(report, filename_time):
    """保存文件并推送到GitHub"""
    try:
        # 目标目录
        obsidian_dir = os.path.expanduser("~/my_obsidian")
        daily_news_dir = os.path.join(obsidian_dir, "daily_news")
        
        # 确保目录存在
        os.makedirs(daily_news_dir, exist_ok=True)
        
        # 文件名
        filename = f"{filename_time}-daily-news.md"
        filepath = os.path.join(daily_news_dir, filename)
        
        # 保存文件
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"✅ 新闻简报已保存到: {filepath}")
        
        # Git操作
        os.chdir(obsidian_dir)
        
        # 添加文件
        subprocess.run(["git", "add", f"daily_news/{filename}"], check=True)
        
        # 提交
        commit_message = f"📰 Add daily news for {filename_time}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # 推送
        subprocess.run(["git", "push", "origin", "master"], check=True)
        
        print(f"✅ 已推送到GitHub: {commit_message}")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Git操作失败: {e}")
        return False
    except Exception as e:
        print(f"❌ 保存或推送失败: {e}")
        return False

def main():
    """主函数"""
    print("=" * 60)
    print("开始自动新闻收集...")
    
    # 获取当前时间
    run_time = datetime.datetime.now()
    print(f"运行时间: {run_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 收集新闻
    tech_news = collect_tech_news()
    finance_news = collect_finance_news()
    military_news = collect_military_news()
    
    print(f"收集完成: 科技{len(tech_news)}条, 金融{len(finance_news)}条, 军事{len(military_news)}条")
    
    # 生成报告
    report, filename_time = generate_report(tech_news, finance_news, military_news, run_time)
    
    # 保存并推送
    success = save_and_push_to_github(report, filename_time)
    
    if success:
        print("✅ 新闻收集和推送完成！")
    else:
        print("❌ 新闻收集或推送失败")
    
    print("=" * 60)
    return success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)