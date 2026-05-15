# 🌙 心境探店 MoodPlace

> 不问哪里评分高，只问哪里懂你的心

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**心境探店（MoodPlace）** 是一款以情绪为入口、以 AI 为引擎的个性化场所发现应用。它首创将心理学 VAD 情绪三维模型与 AIGC 技术深度融合，通过理解用户当下的情绪状态，推荐最契合心境的真实场所，并为每一处推荐生成专属 AI 氛围图。

本项目为 **vivo 第三届 AIGC 创新应用大赛** 参赛作品。

---

## ✨ 核心特性

- 🧠 **VAD 情绪向量解析** — 基于 Valence-Arousal-Dominance 三维情绪模型，将抽象情绪转化为结构化向量
- 🕐 **情境感知推荐** — 自动注入时间段上下文（深夜/午间等），动态调整推荐策略
- 🎨 **AI 氛围图生成** — 调用 Doubao-Seedream-4.5 为每个推荐场所实时生成专属氛围图
- 🗺️ **真实 POI 检索** — 集成地理搜索服务，推荐真实可导航的场所
- 💾 **智能本地缓存** — 氛围图 24h 本地缓存，避免重复生成消耗配额
- 📝 **探店情绪反馈闭环** — 记录探店前后情绪变化，积累个性化数据
- 💡 **长程情绪陪伴** — 历史探店记忆回溯，主动展示情绪洞察提示

---

## 🖼️ 界面预览

| 启动页 | 情绪选择 | AI 推理中 | 结果页 |
|--------|----------|-----------|--------|
| 沉浸式宇宙星云视觉 | 6 种情绪快捷标签 + 自然语言描述 | 三阶段动态进度管道 | VAD 面板 + 氛围图 + 场所卡片 |

---

## 🚀 快速启动

### 环境要求

- Python 3.8+
- vivo AI 开放平台 API Key（[申请地址](https://ai.vivo.com.cn/)）

### 安装与运行

```bash
# 1. 克隆仓库
git clone https://github.com/SilenVale/MoodPlace.git
cd MoodPlace

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置环境变量
cp .env.example .env
# 编辑 .env，填入你的 vivo API Key

# 4. 启动服务
python server.py

# 5. 浏览器打开
# http://localhost:5001
```

---

## 🏗️ 技术架构

```
┌─────────────────────────────────────┐
│  Browser (SPA)                      │  ← 单页应用，沉浸式交互
├─────────────────────────────────────┤
│  Flask Proxy Server (:5001)         │  ← 统一 API 代理与编排
├─────────────────────────────────────┤
│  vivo AI API                        │
│  ├── /v1/chat/completions           │  ← 蓝心大模型（情绪分析）
│  ├── /api/v1/image_generation       │  ← Doubao 图像生成
│  └── /search/geo                    │  ← POI 地理搜索
└─────────────────────────────────────┘
```

### 技术栈

| 层级 | 技术 |
|------|------|
| 前端 | HTML5 + CSS3 + Vanilla JS（单页应用，无框架依赖） |
| 后端 | Python + Flask |
| 大模型 | vivo 蓝心大模型（Volc-DeepSeek-V3.2） |
| 图像生成 | Doubao-Seedream-4.5 |
| 情绪模型 | VAD（Valence-Arousal-Dominance） |
| 地图服务 | 高德地图 DeepLink |

---

## 📁 项目结构

```
MoodPlace/
├── index.html          # 前端单页应用
├── server.py           # Flask 代理服务器
├── requirements.txt    # Python 依赖
├── test_apis.py        # API 接口测试脚本
├── .env.example        # 环境变量模板
├── .gitignore          # Git 忽略规则
└── README.md           # 项目说明
```

---

## 🎯 核心交互流程

1. **情绪表达** — 选择情绪标签或自由描述心情
2. **AI 解析** — 蓝心大模型解析 VAD 情绪向量 + 空间需求
3. **场所匹配** — 结合城市 + 时间段检索真实 POI
4. **氛围呈现** — 为每个场所生成专属 AI 氛围图
5. **一键导航** — 点击跳转高德地图，直接前往
6. **情绪反馈** — 探店后记录心情变化，形成闭环

---

## ⚠️ 注意事项

- 图像生成有每日配额限制（已内置 24h 本地缓存机制）
- 首次图像生成约需 10-30 秒，请耐心等待
- POI 搜索返回 `statusCode: 4` 属正常现象，以 `pois` 数组为准

---

## 📄 License

MIT License © 2026 MoodPlace Team
