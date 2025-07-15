# LINE Bot 打卡功能範本

這是一個使用 Python Flask 搭配 LINE Messaging API 的上下班打卡 Bot 專案。

## ✅ 功能說明

- 使用者輸入「上班」、「下班」，回覆打卡時間
- 可部署於 Render 免費主機平台

## 🚀 Render 部署步驟

1. 建立 GitHub Repo，推送此專案
2. 到 [Render.com](https://render.com) 建立 Web Service
3. 設定：
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
   - 環境變數：
     - `LINE_CHANNEL_ACCESS_TOKEN`
     - `LINE_CHANNEL_SECRET`
4. 設定 LINE Webhook URL 至 `/webhook`

## 📲 使用說明

- 在 LINE 對話框輸入：
  - `上班` → 回覆打卡時間
  - `下班` → 回覆打卡時間
