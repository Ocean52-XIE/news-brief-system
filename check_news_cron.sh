#!/bin/bash
# 检查新闻收集定时任务状态

echo "📊 新闻收集定时任务状态检查"
echo "=============================="

# 检查crontab
echo "1. Crontab任务列表:"
crontab -l | grep -A4 "新闻收集定时任务"
echo ""

# 检查日志文件
LOG_FILE="$HOME/news_collector.log"
echo "2. 日志文件状态:"
if [ -f "$LOG_FILE" ]; then
    echo "   ✅ 日志文件存在: $LOG_FILE"
    echo "   文件大小: $(du -h "$LOG_FILE" | cut -f1)"
    echo "   最后修改: $(stat -c %y "$LOG_FILE")"
    echo ""
    echo "   最近5条日志:"
    tail -5 "$LOG_FILE"
else
    echo "   ⚠️  日志文件不存在: $LOG_FILE"
fi
echo ""

# 检查脚本文件
SCRIPT_PATH="/home/xieyq/.openclaw/workspace-news/auto_news_collector.py"
echo "3. 脚本文件状态:"
if [ -f "$SCRIPT_PATH" ]; then
    echo "   ✅ 脚本文件存在: $SCRIPT_PATH"
    echo "   文件权限: $(stat -c %A "$SCRIPT_PATH")"
else
    echo "   ❌ 脚本文件不存在: $SCRIPT_PATH"
fi
echo ""

# 检查Git仓库
OBSIDIAN_DIR="$HOME/my_obsidian"
echo "4. Git仓库状态:"
if [ -d "$OBSIDIAN_DIR/.git" ]; then
    cd "$OBSIDIAN_DIR"
    echo "   ✅ Git仓库存在: $OBSIDIAN_DIR"
    echo "   当前分支: $(git branch --show-current)"
    echo "   最后提交: $(git log --oneline -1)"
    echo ""
    echo "   最近3个新闻文件:"
    ls -lt daily_news/ | head -4
else
    echo "   ❌ Git仓库不存在: $OBSIDIAN_DIR"
fi
echo ""

# 检查Python环境
echo "5. Python环境检查:"
if command -v python3 &> /dev/null; then
    echo "   ✅ Python3可用: $(python3 --version)"
else
    echo "   ❌ Python3不可用"
fi
echo ""

# 检查Tavily技能
TAVILY_SCRIPT="$HOME/.openclaw/workspace/skills/openclaw-tavily-search/scripts/tavily_search.py"
echo "6. Tavily搜索技能:"
if [ -f "$TAVILY_SCRIPT" ]; then
    echo "   ✅ Tavily脚本存在: $TAVILY_SCRIPT"
else
    echo "   ❌ Tavily脚本不存在"
fi
echo ""

echo "📅 下次运行时间:"
echo "   00:00 (午夜)"
echo "   06:00 (早上)"
echo "   12:00 (中午)" 
echo "   18:00 (晚上)"
echo ""
echo "✅ 状态检查完成"