# GitHub推送指南

## 📋 当前状态

### Git仓库状态
- ✅ Git仓库已初始化
- ✅ 重要文件已添加到暂存区
- ✅ 初始提交已完成
- ⚠ 远程仓库未配置

### 已提交的文件
1. **配置文件**
   - `news_brief_config.json` - 新闻简报配置
   - `.gitignore` - Git忽略规则

2. **模板文件**
   - `optimized_news_brief_template.md` - 优化版简报模板
   - `AGENTS.md` - 代理配置
   - `SOUL.md` - 身份配置
   - `USER.md` - 用户偏好

3. **生成脚本**
   - `generate_optimized_news_brief.py` - 优化版生成脚本
   - `real_news_collector.py` - 真实新闻收集脚本

4. **文档说明**
   - `NEWS_BRIEF_OPTIMIZATION_README.md` - 优化说明
   - `美股优化完成总结.md` - 美股优化总结

5. **示例简报**
   - `Daily_News_Brief_2026-03-06_1039.md` - 最新优化版简报

## 🚀 推送到GitHub的步骤

### 步骤1: 创建GitHub仓库
1. 访问 https://github.com
2. 点击右上角 "+" → "New repository"
3. 填写仓库信息：
   - Repository name: `news-brief-system` (建议)
   - Description: `OpenClaw新闻简报系统 - 自动化新闻收集与生成`
   - 选择 Public 或 Private
   - 不要初始化README、.gitignore或license
4. 点击 "Create repository"

### 步骤2: 配置远程仓库
```bash
# 添加远程仓库（替换为你的仓库URL）
git remote add origin https://github.com/你的用户名/仓库名.git

# 验证远程仓库
git remote -v
```

### 步骤3: 推送到GitHub
```bash
# 首次推送
git push -u origin master

# 后续推送
git push
```

### 步骤4: 设置自动推送（可选）
可以修改生成脚本，在生成简报后自动推送到GitHub。

## ⏰ 定时任务设置

### 建议的时间安排
1. **早间简报**: 09:00
   - 包含隔夜美股收盘数据
   - 当日市场展望

2. **午间更新**: 15:00
   - A股收盘数据
   - 港股午盘表现
   - 重要新闻更新

3. **晚间总结**: 21:00
   - 全天市场总结
   - 美股开盘预览
   - 深度分析

### 设置定时任务
运行设置脚本：
```bash
./setup_cron_optimized.sh
```

或手动添加crontab：
```bash
# 编辑crontab
crontab -e

# 添加以下内容
0 9 * * * cd /home/xieyq/.openclaw/workspace-news && /usr/bin/python3 generate_optimized_news_brief.py >> /home/xieyq/.openclaw/workspace-news/logs/morning_$(date +\%Y\%m\%d).log 2>&1
0 15 * * * cd /home/xieyq/.openclaw/workspace-news && /usr/bin/python3 generate_optimized_news_brief.py >> /home/xieyq/.openclaw/workspace-news/logs/afternoon_$(date +\%Y\%m\%d).log 2>&1
0 21 * * * cd /home/xieyq/.openclaw/workspace-news && /usr/bin/python3 generate_optimized_news_brief.py >> /home/xieyq/.openclaw/workspace-news/logs/evening_$(date +\%Y\%m\%d).log 2>&1
```

## 🔧 自动化GitHub推送集成

### 方案1: 修改生成脚本
在 `generate_optimized_news_brief.py` 的 `main()` 函数末尾添加：
```python
def push_to_github():
    """推送到GitHub"""
    try:
        import subprocess
        # 添加文件
        subprocess.run(["git", "add", "Daily_News_Brief_*.md"], check=True)
        # 提交
        commit_msg = f"自动更新: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} 新闻简报"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        # 推送
        subprocess.run(["git", "push"], check=True)
        print("✓ 已推送到GitHub")
    except Exception as e:
        print(f"⚠ GitHub推送失败: {e}")
```

### 方案2: 单独的推送脚本
创建 `auto_push_to_github.sh`:
```bash
#!/bin/bash
cd /home/xieyq/.openclaw/workspace-news
git add Daily_News_Brief_*.md
git commit -m "自动更新: $(date '+%Y-%m-%d %H:%M') 新闻简报"
git push
```

然后在crontab中调用：
```bash
5 9 * * * /home/xieyq/.openclaw/workspace-news/auto_push_to_github.sh
5 15 * * * /home/xieyq/.openclaw/workspace-news/auto_push_to_github.sh
5 21 * * * /home/xieyq/.openclaw/workspace-news/auto_push_to_github.sh
```

## 📊 文件管理策略

### 版本控制规则
1. **保留文件**:
   - 配置文件 (.json)
   - 脚本文件 (.py)
   - 模板文件 (.md)
   - 文档说明 (.md)

2. **定期清理**:
   - 新闻简报文件保留最近7天
   - 日志文件保留最近30天
   - 临时文件即时清理

### .gitignore配置
已配置的忽略规则：
- Python缓存文件
- 虚拟环境
- IDE配置文件
- 系统文件
- OpenClaw特定文件
- 测试文件

## 🔍 故障排除

### 常见问题
1. **GitHub认证失败**
   ```bash
   # 使用SSH密钥
   git remote set-url origin git@github.com:用户名/仓库名.git
   
   # 或使用Personal Access Token
   git remote set-url origin https://TOKEN@github.com/用户名/仓库名.git
   ```

2. **推送冲突**
   ```bash
   # 拉取最新更改
   git pull origin master
   
   # 解决冲突后重新推送
   git add .
   git commit -m "解决冲突"
   git push
   ```

3. **定时任务不执行**
   ```bash
   # 检查cron服务
   sudo systemctl status cron
   
   # 检查日志
   grep CRON /var/log/syslog
   
   # 测试脚本权限
   chmod +x generate_optimized_news_brief.py
   ```

## 📈 监控和维护

### 日志监控
```bash
# 查看最新日志
tail -f logs/morning_$(date +%Y%m%d).log

# 查看错误日志
grep -i error logs/*.log

# 查看生成统计
find . -name "Daily_News_Brief_*.md" -type f | wc -l
```

### 定期维护任务
1. **每日**: 检查日志，确保生成正常
2. **每周**: 清理旧文件，备份重要数据
3. **每月**: 更新依赖，优化脚本

## 🎯 下一步行动

### 立即执行
1. [ ] 创建GitHub仓库
2. [ ] 配置远程仓库URL
3. [ ] 执行首次推送
4. [ ] 设置定时任务

### 后续优化
1. [ ] 集成真实新闻API
2. [ ] 添加数据可视化
3. [ ] 实现周度总结
4. [ ] 优化推送自动化

---

**最后更新**: 2026年3月6日 10:45  
**状态**: Git仓库已初始化，等待配置GitHub远程仓库  
**建议**: 先创建GitHub仓库，然后运行 `./github_push_setup.sh` 进行配置