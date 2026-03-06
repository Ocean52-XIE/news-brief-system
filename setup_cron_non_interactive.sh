#!/bin/bash
# 非交互式定时任务设置脚本

echo "=== 新闻简报定时任务设置（非交互式）==="
echo "按照建议的时间配置：09:00, 15:00, 21:00"
echo ""

# 获取当前工作目录
WORKDIR=$(pwd)
echo "工作目录: $WORKDIR"

# 检查Python脚本是否存在
if [ ! -f "generate_optimized_news_brief.py" ]; then
    echo "❌ 错误: generate_optimized_news_brief.py 不存在"
    exit 1
fi

echo "✓ 找到生成脚本: generate_optimized_news_brief.py"

# 创建日志目录
LOGDIR="$WORKDIR/logs"
mkdir -p "$LOGDIR"
echo "✓ 创建日志目录: $LOGDIR"

# 生成crontab配置
CRON_CONFIG="# 新闻简报定时任务 - 优化版
# 每天上午9:00生成早间简报
0 9 * * * cd $WORKDIR && /usr/bin/python3 generate_optimized_news_brief.py >> $LOGDIR/morning_\$(date +\\%Y\\%m\\%d).log 2>&1

# 每天下午3:00生成午间更新
0 15 * * * cd $WORKDIR && /usr/bin/python3 generate_optimized_news_brief.py >> $LOGDIR/afternoon_\$(date +\\%Y\\%m\\%d).log 2>&1

# 每天晚上9:00生成晚间总结
0 21 * * * cd $WORKDIR && /usr/bin/python3 generate_optimized_news_brief.py >> $LOGDIR/evening_\$(date +\\%Y\\%m\\%d).log 2>&1

# 每周五下午6:00生成周度总结（预留）
0 18 * * 5 cd $WORKDIR && echo '周度总结功能待实现' >> $LOGDIR/weekly_\$(date +\\%Y\\%m\\%d).log 2>&1"

echo ""
echo "=== 生成的crontab配置 ==="
echo "$CRON_CONFIG"

# 保存配置到文件
CRON_FILE="$WORKDIR/crontab_config_optimized.txt"
echo "$CRON_CONFIG" > "$CRON_FILE"
echo ""
echo "✓ 配置已保存到: $CRON_FILE"

# 显示安装说明
echo ""
echo "=== 安装说明 ==="
echo "要安装定时任务，请运行以下命令："
echo ""
echo "1. 备份现有crontab:"
echo "   crontab -l > crontab_backup_\$(date +%Y%m%d_%H%M%S).bak"
echo ""
echo "2. 添加新配置:"
echo "   (crontab -l 2>/dev/null; cat $CRON_FILE) | crontab -"
echo ""
echo "3. 验证安装:"
echo "   crontab -l"
echo ""
echo "=== 测试命令 ==="
echo "手动测试: python3 generate_optimized_news_brief.py"
echo "查看日志: tail -f $LOGDIR/*.log"
echo ""
echo "=== 完成 ==="