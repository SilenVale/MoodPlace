#!/usr/bin/env python3
"""
心境探店 MoodPlace — API 接口测试脚本
在项目目录下运行：python test_apis.py
（不需要启动 Flask，直接测 vivo API）
"""
import requests
import uuid
import time
import json

APP_KEY = "sk-xuanji-2026641233-dEtmaWhEeHdHbXh2amZsQQ=="
BASE_URL = "https://api-ai.vivo.com.cn"

def sep(title):
    print(f"\n{'='*55}")
    print(f"  {title}")
    print('='*55)

# ─────────────────────────────────────────
# 1. 大模型 /v1/chat/completions
# ─────────────────────────────────────────
sep("1/3  蓝心大模型 chat/completions")
try:
    resp = requests.post(
        f"{BASE_URL}/v1/chat/completions",
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {APP_KEY}"
        },
        params={"request_id": str(uuid.uuid4())},
        json={
            "model": "Volc-DeepSeek-V3.2",
            "max_tokens": 300,
            "temperature": 0.8,
            "messages": [
                {
                    "role": "system",
                    "content": "你是情绪感知探店顾问。严格只输出JSON，不加任何其他文字。"
                },
                {
                    "role": "user",
                    "content": "我今天工作压力很大，很疲惫，想找个安静的地方放松一下。城市：武汉"
                }
            ]
        },
        timeout=30
    )
    print(f"HTTP状态: {resp.status_code}")
    data = resp.json()
    print(f"顶层字段: {list(data.keys())}")

    # 验证前端解析路径
    content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
    print(f"\n✅ choices[0].message.content 路径: {'OK' if content else 'EMPTY'}")
    print(f"内容预览: {content[:200]}")

except Exception as e:
    print(f"❌ 失败: {e}")

# ─────────────────────────────────────────
# 2. 图片生成 /api/v1/image_generation
# ─────────────────────────────────────────
sep("2/3  Doubao 图片生成")
print("（约需 10-30 秒，请耐心等待）")
try:
    resp = requests.post(
        f"{BASE_URL}/api/v1/image_generation",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {APP_KEY}"
        },
        params={
            "module": "aigc",
            "request_id": str(uuid.uuid4()),
            "system_time": int(time.time())
        },
        json={
            "model": "Doubao-Seedream-4.5",
            "prompt": "a cozy quiet Japanese cafe, warm lighting, wooden interior, cinematic",
            "parameters": {"size": "1920x1920"}
        },
        timeout=120
    )
    print(f"HTTP状态: {resp.status_code}")
    data = resp.json()
    print(f"顶层字段: {list(data.keys())}")
    print(f"code值: {data.get('code')}")

    # 验证前端解析路径
    url1 = data.get("data", {}).get("images", [{}])[0].get("url") if data.get("data") else None
    url2 = data.get("data", {}).get("image") if data.get("data") else None
    print(f"\n✅ data.images[0].url: {url1}")
    print(f"✅ data.image: {url2}")
    print(f"\n完整响应结构:\n{json.dumps(data, ensure_ascii=False, indent=2)[:600]}")

except Exception as e:
    print(f"❌ 失败: {e}")

# ─────────────────────────────────────────
# 3. POI 搜索 /search/geo
# ─────────────────────────────────────────
sep("3/3  POI 地理搜索")
try:
    resp = requests.get(
        f"{BASE_URL}/search/geo",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {APP_KEY}"
        },
        params={
            "keywords": "咖啡馆",
            "city": "武汉",
            "page_num": 1,
            "page_size": 3,
            "requestId": str(uuid.uuid4())
        },
        timeout=30
    )
    print(f"HTTP状态: {resp.status_code}")
    data = resp.json()
    print(f"顶层字段: {list(data.keys())}")

    # 验证前端解析路径
    pois = data.get("pois", [])
    print(f"\n✅ pois数组长度: {len(pois)}")
    if pois:
        p = pois[0]
        print(f"第一条POI字段: {list(p.keys())}")
        print(f"  name    : {p.get('name')}")
        print(f"  address : {p.get('address')}")
        print(f"  district: {p.get('district')}")
        print(f"  location: {p.get('location')}")
        print(f"  city    : {p.get('city')}")
    else:
        print("⚠️  pois为空，检查statusCode和statusInfo:")
        print(f"  statusCode: {data.get('statusCode')}")
        print(f"  statusInfo: {data.get('statusInfo')}")

except Exception as e:
    print(f"❌ 失败: {e}")

print(f"\n{'='*55}")
print("  测试完成")
print('='*55)
