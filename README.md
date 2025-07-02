# 🤖 Automated Post Creation AI Agent

This project is an AI-powered Python bot that automatically generates and posts content to social media platforms such as **Telegram** and **X (formerly Twitter)**.

## 🚀 Features

- 🧠 Generates engaging content using OpenAI's GPT model
- 📤 Automatically posts to:
  - Telegram Channels or Groups
  - X (Twitter)
- 📅 Supports daily scheduled posting
- 🔐 Uses environment variables or config values to keep API keys secure

## 📁 Project Structure

```
social_ai_poster/
│
├── auto_post.py           # Master script to generate + post
├── generate_post.py       # Uses OpenAI to generate social media content
├── post_to_telegram.py    # Posts message to Telegram bot
├── post_to_x.py           # Posts tweet using Twitter API
├── requirements.txt       # All required Python libraries
└── README.md              # Project documentation (this file)
```

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/emuduko/automated_post_creation_ai_agent.git
cd automated_post_creation_ai_agent
```

### 2. Install dependencies

If using Portable Python:

```bash
python.exe -m pip install -r requirements.txt --target=./
```

### 3. Add your API keys

Update the script files with your:
- OpenAI API key
- Telegram Bot Token & Chat ID
- X (Twitter) API credentials

### 4. Run the bot

```bash
python.exe auto_post.py
```

It will generate a post and share it to Telegram and X.

## ⏰ Automate Posting (Optional)

The script includes `schedule` so it can auto-post daily. You can run it in background or use Task Scheduler to run the `.bat` launcher file.

## 🙏 Credits

- [OpenAI](https://openai.com/)
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [tweepy](https://www.tweepy.org/)

## 📄 License

This project is licensed under the MIT License.

---

Made with ❤️ by [emuduko](https://github.com/emuduko)
