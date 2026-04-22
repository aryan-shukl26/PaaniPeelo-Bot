import asyncio
from telegram.ext import ApplicationBuilder

# ── Config ────────────────────────────────────────────────────
BOT_TOKEN = "8071045891:AAEUIsDyvE-LSTMtxT6O-RRTfRnGYlLmS7g"
CHAT_ID = 5525340838
REEL_URL = "https://www.instagram.com/reel/DVqtOvjivva/?igsh=MXNlNHcxZnFhcHlrMw=="

INTERVAL_HOURS = 1

# ── Reminder message ──────────────────────────────────────────
async def send_reminder(context):
    await context.bot.send_message(
        chat_id=CHAT_ID,
        text=f"""🐑 Stay Hydrated!

Even this sheep remembers 😂

Watch this:
{REEL_URL}
"""
    )
    print("✅ Reminder sent!")

# ── Entry point ───────────────────────────────────────────────
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # Send every X seconds
    app.job_queue.run_repeating(
        send_reminder,
        interval=INTERVAL_HOURS * 3600,
        first=1  # Send first reminder after 1 second
    )
    
    print(f"🚀 PaaniPeelo bot started! Sending reminders every {INTERVAL_HOURS} hour(s).")
    app.run_polling()