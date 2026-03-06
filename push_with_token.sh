#!/bin/bash
# 使用Personal Access Token推送的脚本

echo "=== GitHub推送脚本（使用Token）==="

# 仓库信息
REPO_OWNER="ou_a565ab0428a04deaee3173345d273fab"
REPO_NAME="news-brief-system"

echo "仓库: $REPO_OWNER/$REPO_NAME"

# 检查当前Git状态
echo ""
echo "=== 当前Git状态 ==="
git status --short

# 提示输入Personal Access Token
echo ""
echo "=== 需要GitHub Personal Access Token ==="
echo "如果没有Token，请到以下地址创建："
echo "  https://github.com/settings/tokens"
echo ""
echo "需要的权限："
echo "  - repo (全部仓库权限)"
echo ""
read -s -p "请输入GitHub Personal Access Token: " GITHUB_TOKEN
echo ""

if [ -z "$GITHUB_TOKEN" ]; then
    echo "❌ 未提供Token，退出"
    exit 1
fi

# 使用Token配置远程仓库
echo "配置远程仓库..."
REMOTE_URL="https://${GITHUB_TOKEN}@github.com/${REPO_OWNER}/${REPO_NAME}.git"
git remote set-url origin "$REMOTE_URL"

# 验证远程仓库
echo ""
echo "=== 远程仓库配置 ==="
git remote -v

# 尝试推送
echo ""
echo "=== 开始推送 ==="
if git push -u origin master; then
    echo ""
    echo "✅ 推送成功！"
    echo ""
    echo "仓库地址: https://github.com/${REPO_OWNER}/${REPO_NAME}"
    echo "最新提交: $(git log --oneline -1)"
    
    # 恢复SSH远程地址（为了安全）
    echo ""
    echo "恢复SSH远程地址..."
    git remote set-url origin "git@github.com:${REPO_OWNER}/${REPO_NAME}.git"
    echo "远程仓库已恢复为SSH"
else
    echo ""
    echo "❌ 推送失败"
    echo "可能的原因："
    echo "1. Token无效或权限不足"
    echo "2. 仓库不存在"
    echo "3. 网络问题"
    echo ""
    echo "建议："
    echo "1. 确认仓库名称: $REPO_OWNER/$REPO_NAME"
    echo "2. 确认Token有repo权限"
    echo "3. 确认仓库已设置为公开(Public)"
fi

echo ""
echo "=== 完成 ==="