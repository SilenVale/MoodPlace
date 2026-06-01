from flask import Flask, request, jsonify, send_from_directory
import requests
import uuid
import time
import json
import os
from flask_cors import CORS

app = Flask(__name__, static_folder='.')
CORS(app)

APP_KEY = os.environ.get('VIVO_API_KEY', '')
BASE_URL = "https://api-ai.vivo.com.cn"


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': f'Bearer {APP_KEY}'
    }
    params = {'request_id': str(uuid.uuid4())}
    try:
        resp = requests.post(
            f'{BASE_URL}/v1/chat/completions',
            headers=headers,
            params=params,
            json=data,
            timeout=60
        )
        return jsonify(resp.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/image', methods=['POST'])
def image():
    data = request.get_json()
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {APP_KEY}'
    }
    params = {
        'module': 'aigc',
        'request_id': str(uuid.uuid4()),
        'system_time': int(time.time())
    }
    try:
        resp = requests.post(
            f'{BASE_URL}/api/v1/image_generation',
            headers=headers,
            params=params,
            json=data,
            timeout=120
        )
        return jsonify(resp.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/poi', methods=['GET'])
def poi():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {APP_KEY}'
    }
    params = {
        'keywords': request.args.get('keywords', ''),
        'city': request.args.get('city', ''),
        'page_num': 1,
        'page_size': 3,
        'requestId': str(uuid.uuid4())
    }
    try:
        resp = requests.get(
            f'{BASE_URL}/search/geo',
            headers=headers,
            params=params,
            timeout=30
        )
        return jsonify(resp.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    if not APP_KEY:
        print("⚠️ 警告：未设置 VIVO_API_KEY 环境变量")
        print("   本地运行：export VIVO_API_KEY='你的密钥'（Mac/Linux）")
        print("   本地运行：set VIVO_API_KEY=你的密钥（Windows）")
        print("   云端部署：在 Render Dashboard → Environment 中配置")
    print("🌙 心境探店 MoodPlace 后端启动中...")
    print("📍 访问地址: http://localhost:5001")
    app.run(debug=True, port=5001, host='0.0.0.0')
