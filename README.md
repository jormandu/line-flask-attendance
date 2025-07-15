# LINE Flask Attendance Bot

簡單的上下班打卡 LINE bot，使用 Python Flask 實作，部署於 Render。

## 🚀 快速部署步驟

1. 登入 [https://render.com](https://render.com)
2. 新增 Web Service，選擇上傳 ZIP 或從 GitHub 部署
3. 設定：
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
4. 設定環境變數：
   - `LINE_CHANNEL_ACCESS_TOKEN`
   - `LINE_CHANNEL_SECRET`
5. 在 LINE Developer Console 設定 Webhook URL（例如 https://你的網址.onrender.com/webhook）

完成後即可使用「上班」/「下班」打卡指令
