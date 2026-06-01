@echo off
chcp 65001 >nul
REM 心境探店 MoodPlace - Windows 一键启动脚本

echo 🌙 心境探店 MoodPlace 启动中...

REM 检查 Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误：未检测到 Python，请先安装 Python（建议 3.9+）
    pause
    exit /b 1
)

REM 检查虚拟环境
if not exist "venv" (
    echo 📦 创建虚拟环境...
    python -m venv venv
)

REM 激活虚拟环境
echo 🔧 激活虚拟环境...
call venv\Scripts\activate.bat

REM 安装依赖
echo 📦 安装依赖...
pip install -r requirements.txt -q

REM 提示设置环境变量
if "%VIVO_API_KEY%"=="" (
    echo.
    echo ⚠️  提醒：VIVO_API_KEY 环境变量未设置
    echo     如果你已有密钥，请运行：set VIVO_API_KEY=你的密钥
    echo     然后重新运行本脚本
    echo.
)

REM 启动服务
echo 🚀 启动服务...
echo 📍 浏览器即将自动打开 http://localhost:5001
echo    按 Ctrl+C 停止服务
echo.

REM 延迟2秒后打开浏览器
start "" http://localhost:5001

python server.py
