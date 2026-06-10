import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template,request, make_response, jsonify
from datetime import datetime

import os
import json
import firebase_admin
from firebase_admin import credentials, firestore


# 判斷是在 Vercel 還是本地
if os.path.exists('serviceAccountKey.json'):
    # 本地環境：讀取檔案
    cred = credentials.Certificate('serviceAccountKey.json')
else:
    # 雲端環境：從環境變數讀取 JSON 字串
    firebase_config = os.getenv('FIREBASE_CONFIG')
    cred_dict = json.loads(firebase_config)
    cred = credentials.Certificate(cred_dict)

firebase_admin.initialize_app(cred)

app = Flask(__name__) 

@app.route("/webhook", methods=["POST"])
def webhook():
    # build a request object
    req = request.get_json(force=True)
    # fetch queryResult from json
    #action =  req.get("queryResult").get("action")
    #msg =  req.get("queryResult").get("queryText")
    info = "動作：" + action + "； 查詢內容：" + msg
    if (action == "series"):
        rate =  req.get("queryResult").get("parameters").get("name")
        info = "我是星巴克聊天機器人，您選擇的系列是：" + name + "，相關品項：\n"
        db = firestore.client()
        collection_ref = db.collection("星巴克星推薦飲品")
        docs = collection_ref.get()
        result = ""
        for doc in docs:
            dict = doc.to_dict()
            if name in dict["name"]:
                result += "熱量：" + dict["calo"] + "\n"
                result += "容量：" + dict["size"] + "\n"
                result += "價格：" + dict["price"] + "\n\n"
        info += result
    return make_response(jsonify({"fulfillmentText": info}))

if __name__ == "__main__":
    app.run(debug=True)
    
