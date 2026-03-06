#!/bin/bash
# 设置新闻收集定时任务

echo "设置新闻收集定时任务..."
echo "每天0点、6点、12点、18点自动运行"

# 获取脚本绝对路径
SCRIPT_PATH="$(cd "$(dirname "$0")" && pwd)/auto_news_collector.py"
echo "脚本路径: $SCRIPT_PATH"

# 创建crontab条目
CRON_ENTRIES="
# 新闻收集定时任务 - 每天0点、6点、12点、18点
0 0 * * * /usr/bin/python3 $SCRIPT_PATH >> ~/news_collector.log 2>&1
0 6 * * * /usr/bin/python3 $SCRIPT_PATH >> ~/news_collector.log 2>&1
0 12 * * * /usr/bin/python3 $SCRIPT_PATH >> ~/news_collector.log 2>&1
0 18 * * * /usr/bin/python3 $SCRIPT_PATH >> ~/news_collector.log 2>&1
"

# 添加到crontab
(crontab -l 2>/dev/null; echo "$CRON_ENTRIES") | crontab -

echo "定时任务已设置完成！"
echo "运行时间: 每天 00:00, 06:00, 12:00, 18:00"
echo "日志文件: ~/news_collector.log"
echo ""
echo "当前crontab任务:"
crontab -l