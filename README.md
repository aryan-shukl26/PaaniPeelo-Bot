# 💧 PaaniPeelo Bot

A Telegram bot that sends hourly hydration reminders to your group — because we all forget to drink water. 😂

---

## 🤖 What it does

- Sends a hydration reminder to a Telegram group every hour
- Includes a funny Instagram reel to make people actually read it
- Runs 24/7 on Render — no laptop needed

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- A Telegram bot token from [@BotFather](https://t.me/BotFather)
- A Telegram group chat ID

### Installation

```bash
git clone https://github.com/aryan-shukl26/PaaniPeelo-Bot.git
cd PaaniPeelo-Bot
pip install -r requirements.txt
```

### Configuration

Open `bot.py` and update:

```python
BOT_TOKEN = "your_token_here"
CHAT_ID = your_group_chat_id
REEL_URL = "your_instagram_reel_url"
INTERVAL_HOURS = 1
```

### Run locally

```bash
python bot.py
```

---

## ☁️ Deployment

Deployed on [Render](https://render.com) as a Web Service.

- Start command: `python bot.py`
- Runs continuously with a lightweight web server on port 10000

---

## 👤 Author

**Aryan Shukla**  
Business Analyst @ RBL Bank | B.Tech — AI & ML  
[LinkedIn](https://linkedin.com/in/shuklaryan) • [GitHub](https://github.com/aryan-shukl26)

---

## 📄 License

MIT License
