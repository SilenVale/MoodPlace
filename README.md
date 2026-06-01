# 🌙 心境探店 · MoodPlace

> 不问哪里评分高，只问哪里懂你的心。

**直接访问体验链接**：`[部署完成后填入]`

---

## 产品简介

心境探店是一款基于 vivo 蓝心大模型的情绪驱动探店工具。

用户用自然语言描述当下情绪，蓝心大模型将其解析为 VAD 三维向量（效价/唤醒度/掌控感），自动匹配最适合当前情绪状态的空间环境，并生成专属氛围意境图，帮助用户在 30 秒内找到"此刻最想去的地方"。

---

## 🚀 快速体验

### 方式一：在线访问（推荐）

打开浏览器访问：
```
[部署完成后填入]
```

> 首次加载约 30 秒（Render 免费版冷启动），之后正常。

### 方式二：本地运行

**Mac / Linux：**
```bash
cd prototype/v4
bash run.sh
```

**Windows：**
```cmd
cd prototype\v4
run.bat
```

浏览器将自动打开 `http://localhost:5001`。

---

## 🏗️ 技术架构

```
浏览器 (HTML/JS SPA)
    ↓ HTTP
Flask 代理服务器 (Python)
    ↓ 转发
vivo AI 开放平台
    ├── 蓝心大模型 —— 情绪理解 → VAD 向量输出
    ├── Doubao-Seedream 4.5 —— 氛围图生成
    └── 高德 POI —— 附近场所查询
```

---

## 🧠 大模型 API 调用说明

| 模块 | 调用模型/API | 功能描述 |
|------|------------|---------|
| 情绪理解 | vivo 蓝心大模型 (Volc-DeepSeek-V3.2) | 将用户情绪描述解析为 VAD 三维向量 |
| 氛围图生成 | Doubao-Seedream 4.5 | 基于场所类型生成 1920×1920 情绪氛围图 |
| 场所查询 | vivo 高德 POI API | 按城市+关键词搜索附近真实场所 |

**Prompt 工程亮点**：
- System Prompt 内嵌 VAD 心理学模型定义（效价/唤醒度/掌控感）
- 自动注入当前时间段情境（深夜/上午/午间/下午/晚间/夜晚）
- 严格 JSON 格式约束，确保输出可被程序直接解析

---

## 📦 项目结构

```
prototype/v4/
├── index.html          # 前端单页面应用（HTML/JS/CSS）
├── server.py           # Flask 后端代理（API 转发 + CORS）
├── requirements.txt    # Python 依赖
├── Procfile            # Render 部署配置
├── run.sh              # Mac/Linux 一键启动
├── run.bat             # Windows 一键启动
├── test_apis.py        # API 连通性测试
├── test_real_prompt.py # 前端真实 Prompt 测试
└── README.md           # 本文件
```

---

## 🔧 部署到 Render（云端）

1. 将代码推送到 GitHub
2. 登录 [Render](https://render.com) → New Web Service → 连接 GitHub 仓库
3. 配置环境变量（Dashboard → Environment）：
   - `VIVO_API_KEY` = 你的 vivo API 密钥
4. 点击 Deploy，等待 2-3 分钟
5. 获取分配的 `.onrender.com` 域名

---

## 📄 License

本项目为 2026 全国大学生 AIGC 创新大赛参赛作品的 demo 版本。

---

**团队成员**：心境探店团队
**竞赛**：2026 全国大学生 AIGC 创新大赛 · vivo 赛道
