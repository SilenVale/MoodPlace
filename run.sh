#!/bin/bash
# 心境探店 MoodPlace - Mac/Linux 一键启动脚本

echo "🌙 心境探店 MoodPlace 启动中..."

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误：未检测到 Python3，请先安装 Python（建议 3.9+）"
    exit 1
fi

# 检查虚拟环境，如果没有就创建
if [ ! -d "venv" ]; then
    echo "📦 创建虚拟环境..."
    python3 -m venv venv
fi

# 激活虚拟环境
echo "🔧 激活虚拟环境..."
source venv/bin/activate

# 安装依赖
echo "📦 安装依赖..."
pip install -r requirements.txt -q

# 提示设置环境变量
if [ -z "$VIVO_API_KEY" ]; then
    echo ""
    echo "⚠️  提醒：VIVO_API_KEY 环境变量未设置"
    echo "    如果你已有密钥，请运行：export VIVO_API_KEY='你的密钥'"
    echo "    然后重新运行本脚本"
    echo ""
fi

# 启动服务
echo "🚀 启动服务..."
echo "📍 浏览器即将自动打开 http://localhost:5001"
echo "   按 Ctrl+C 停止服务"
echo ""

# 延迟1秒后打开浏览器
(sleep 1 && open http://localhost:5001) &

python3 server.py
