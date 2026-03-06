# 📰 自动化新闻收集系统

## 系统概述
这是一个自动化的新闻收集系统，每天在0点、6点、12点、18点自动收集科技、金融、军事新闻，并推送到GitHub仓库。

## 系统架构

### 1. 核心组件
- **新闻收集脚本**: `auto_news_collector.py`
- **定时任务**: Crontab配置
- **搜索工具**: Tavily-search技能
- **存储仓库**: GitHub上的Obsidian笔记库

### 2. 文件结构
```
~/.openclaw/workspace-news/
├── auto_news_collector.py      # 主收集脚本
├── setup_cron.sh              # 定时任务设置脚本
├── check_news_cron.sh         # 状态检查脚本
├── NEWS_SYSTEM_README.md      # 系统文档
└── 今日新闻简报_*.md          # 生成的新闻简报

~/my_obsidian/daily_news/
├── 2026-03-04_0052-daily-news.md  # 带时间戳的新闻文件
├── 2026-03-04-daily-news.md       # 日期新闻文件
└── ...                            # 历史新闻文件
```

## 配置详情

### 定时任务配置
```bash
# 每天0点、6点、12点、18点运行
0 0 * * * /usr/bin/python3 /home/xieyq/.openclaw/workspace-news/auto_news_collector.py >> ~/news_collector.log 2>&1
0 6 * * * /usr/bin/python3 /home/xieyq/.openclaw/workspace-news/auto_news_collector.py >> ~/news_collector.log 2>&1
0 12 * * * /usr/bin/python3 /home/xieyq/.openclaw/workspace-news/auto_news_collector.py >> ~/news_collector.log 2>&1
0 18 * * * /usr/bin/python3 /home/xieyq/.openclaw/workspace-news/auto_news_collector.py >> ~/news_collector.log 2>&1
```

### 新闻收集流程
1. **搜索新闻**: 使用Tavily API搜索最新新闻
2. **分类整理**: 按科技、金融、军事分类
3. **生成报告**: 包含标题、摘要、来源、链接
4. **保存文件**: 保存到`~/my_obsidian/daily_news/`
5. **推送到GitHub**: 自动提交和推送

## 文件命名规则
- **带时间戳**: `YYYY-MM-DD_HHMM-daily-news.md` (如: `2026-03-04_0052-daily-news.md`)
- **仅日期**: `YYYY-MM-DD-daily-news.md` (如: `2026-03-04-daily-news.md`)

## 新闻内容格式
```markdown
# 📰 新闻简报 (YYYY-MM-DD HH:MM)

*报告生成时间: YYYY-MM-DD HH:MM:SS*
*数据来源: Tavily搜索 API*

## 🔬 科技新闻

### 1. 新闻标题
新闻摘要...
**来源**: Tavily搜索  |  **查询**: `搜索关键词`
**链接**: https://example.com/news

## 💰 金融新闻
...

## ⚔️ 军事新闻
...

---
**自动化新闻收集系统**
- 运行时间: YYYY-MM-DD HH:MM:SS
- 收集频率: 每天0点、6点、12点、18点
- 文件命名: YYYY-MM-DD_HHMM-daily-news.md
```

## 管理命令

### 1. 手动运行新闻收集
```bash
python3 auto_news_collector.py
```

### 2. 检查系统状态
```bash
./check_news_cron.sh
```

### 3. 查看日志
```bash
tail -f ~/news_collector.log
```

### 4. 重新设置定时任务
```bash
./setup_cron.sh
```

## 依赖项
1. **Python 3.8+**
2. **Tavily-search技能**: 已安装并配置
3. **Git**: 用于推送到GitHub
4. **Crontab**: 用于定时任务调度

## GitHub仓库
- **仓库地址**: `Ocean52-XIE/my_obsidian`
- **新闻目录**: `daily_news/`
- **提交信息**: `📰 Add daily news for YYYY-MM-DD_HHMM`

## 故障排除

### 常见问题
1. **Tavily搜索失败**: 检查API密钥配置
2. **Git推送失败**: 检查网络连接和Git配置
3. **定时任务不运行**: 检查crontab服务和日志
4. **Python脚本错误**: 检查Python环境和依赖

### 检查步骤
1. 运行 `./check_news_cron.sh` 检查系统状态
2. 查看 `~/news_collector.log` 日志文件
3. 检查crontab服务状态: `systemctl status cron`
4. 手动运行脚本测试: `python3 auto_news_collector.py`

## 扩展功能
1. **添加更多新闻类别**: 修改脚本中的搜索关键词
2. **调整收集频率**: 修改crontab配置
3. **添加通知功能**: 新闻收集完成后发送通知
4. **数据分析**: 对收集的新闻进行趋势分析

## 版本历史
- **v1.0** (2026-03-04): 初始版本，支持基本新闻收集和Git推送
- **v1.1** (2026-03-04): 添加时间戳文件命名，完善来源和链接信息

---
*系统维护: News Agent*
*最后更新: 2026年3月4日*