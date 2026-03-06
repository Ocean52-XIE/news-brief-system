#!/bin/bash
# 清理GitHub仓库，只保留新闻文件

echo "=== 清理GitHub仓库 ==="
echo "只保留新闻简报文件，移除其他文件"
echo ""

# 备份当前状态
echo "备份当前Git状态..."
git branch -m master-backup-$(date +%Y%m%d_%H%M%S)
git checkout --orphan temp-cleanup
git add -A
git commit -m "备份当前状态: $(date '+%Y-%m-%d %H:%M:%S')"

# 创建新的干净分支
echo "创建干净的master分支..."
git checkout --orphan master

# 只添加新闻文件和必要的配置文件
echo "添加新闻文件..."
git add Daily_News_Brief_*.md Real_News_Brief_*.md 2>/dev/null || true

# 创建新的.gitignore（只跟踪新闻文件）
echo "创建新的.gitignore..."
cat > .gitignore << 'EOF'
# 只跟踪新闻简报文件，忽略其他所有文件
*

# 允许新闻简报文件
!Daily_News_Brief_*.md
!Real_News_Brief_*.md

# 允许必要的配置文件
!.gitignore
!README.md
EOF

git add .gitignore

# 创建README.md
echo "创建README.md..."
cat > README.md << 'EOF'
# 新闻简报仓库

这个仓库只包含自动生成的新闻简报文件。

## 文件说明
- `Daily_News_Brief_*.md` - 每日新闻简报
- `Real_News_Brief_*.md` - 真实新闻简报

## 生成时间
- 早间简报: 09:00
- 午间更新: 15:00
- 晚间总结: 21:00

## 自动化系统
由OpenClaw新闻助手自动生成和推送。
EOF

git add README.md

# 提交更改
echo "提交清理后的仓库..."
git commit -m "清理仓库: 只保留新闻文件 - $(date '+%Y-%m-%d %H:%M:%S')"

# 强制推送到GitHub
echo "强制推送到GitHub..."
git push -f origin master

echo ""
echo "✅ 仓库清理完成！"
echo ""
echo "当前仓库内容:"
git ls-tree -r master --name-only

echo ""
echo "=== 后续操作 ==="
echo "1. 删除备份分支（可选）:"
echo "   git branch -D master-backup-*"
echo ""
echo "2. 验证仓库状态:"
echo "   git status"
echo "   git log --oneline -3"
echo ""
echo "3. 测试新闻推送:"
echo "   ./push_news_only.sh"
echo ""
echo "=== 完成 ==="