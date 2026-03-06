#!/bin/bash
# GitHub推送设置脚本

echo "=== GitHub推送设置 ==="

# 检查是否已配置远程仓库
if git remote -v | grep -q "origin"; then
    echo "✓ 远程仓库已配置"
    git remote -v
else
    echo "⚠ 未配置远程仓库"
    
    # 提示用户输入GitHub仓库URL
    echo ""
    echo "请提供GitHub仓库URL："
    echo "格式: https://github.com/用户名/仓库名.git"
    echo ""
    echo "例如:"
    echo "  https://github.com/yourusername/news-brief-system.git"
    echo ""
    read -p "请输入GitHub仓库URL: " github_url
    
    if [ -n "$github_url" ]; then
        git remote add origin "$github_url"
        echo "✓ 已添加远程仓库: $github_url"
    else
        echo "⚠ 未提供GitHub URL，跳过远程仓库配置"
    fi
fi

echo ""
echo "=== 当前分支状态 ==="
git branch -v

echo ""
echo "=== 推送说明 ==="
echo "要推送到GitHub，请运行以下命令："
echo ""
echo "1. 首次推送:"
echo "   git push -u origin master"
echo ""
echo "2. 后续推送:"
echo "   git push"
echo ""
echo "3. 如果需要强制推送:"
echo "   git push -f origin master"
echo ""
echo "=== 完成 ==="