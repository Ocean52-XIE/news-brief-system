#!/bin/bash
# 只推送新闻文件的脚本

echo "=== 新闻文件推送脚本 ==="
echo "只推送新闻简报文件到GitHub"
echo ""

# 设置工作目录
WORKDIR=$(pwd)
echo "工作目录: $WORKDIR"

# 检查是否有新的新闻文件
NEWS_FILES=$(find . -name "Daily_News_Brief_*.md" -o -name "Real_News_Brief_*.md" | head -10)

if [ -z "$NEWS_FILES" ]; then
    echo "❌ 未找到新闻文件"
    exit 1
fi

echo "找到的新闻文件:"
for file in $NEWS_FILES; do
    echo "  - $(basename $file)"
done

echo ""
echo "=== Git状态 ==="

# 检查是否在Git仓库中
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "❌ 当前目录不是Git仓库"
    exit 1
fi

# 添加新闻文件
echo "添加新闻文件..."
git add Daily_News_Brief_*.md Real_News_Brief_*.md 2>/dev/null

# 检查是否有更改
if git diff --cached --quiet; then
    echo "⚠ 没有新的新闻文件需要提交"
    exit 0
fi

# 提交更改
COMMIT_MSG="新闻更新: $(date '+%Y-%m-%d %H:%M')"
echo "提交更改: $COMMIT_MSG"
git commit -m "$COMMIT_MSG"

# 推送到GitHub
echo "推送到GitHub..."
if git push origin master; then
    echo ""
    echo "✅ 新闻文件推送成功！"
    echo ""
    echo "推送的文件:"
    git log --oneline -1 --name-only
else
    echo ""
    echo "❌ 推送失败"
    echo "请检查网络连接和GitHub权限"
    exit 1
fi

echo ""
echo "=== 完成 ==="