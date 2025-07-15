from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os
from datetime import datetime
import sqlite3

def init_db():
    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            action TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_record(user_id, action, timestamp):
    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO records (user_id, action, timestamp) VALUES (?, ?, ?)",
                   (user_id, action, timestamp))
    conn.commit()
    conn.close()

app = Flask(__name__)
init_db()

line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))

@app.route("/")
def home():
    return "LINE Bot 打卡功能啟動成功"

@app.route("/webhook", methods=["POST"])
def webhook():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text.strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if text == "上班":
        save_record(event.source.user_id, text, timestamp)
        reply = f"🟢 上班打卡成功！\n時間：{timestamp}"
    elif text == "下班":
        save_record(event.source.user_id, text, timestamp)
        reply = f"🔴 下班打卡成功！\n時間：{timestamp}"
    else:
        reply = "請輸入「上班」或「下班」來進行打卡。"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply)
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
