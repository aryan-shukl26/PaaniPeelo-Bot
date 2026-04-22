import asyncio
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram.ext import ApplicationBuilder

# ── Config ────────────────────────────────────────────────────
BOT_TOKEN = "8071045891:AAEUIsDyvE-LSTMtxT6O-RRTfRnGYlLmS7g"
CHAT_ID = 5525340838
REEL_URL = "https://www.instagram.com/reel/DVqtOvjivva/?igsh=MXNlNHcxZnFhcHlrMw=="
INTERVAL_HOURS = 1

# ── Dummy web server to satisfy Render ───────────────────────
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"PaaniPeelo bot is running!")
    def log_message(self, format, *args):
        pass  # Suppress logs

def run_server():
    server = HTTPServer(("0.0.0.0", 10000), Handler)
    server.serve_forever()

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
    # Start dummy web server in background thread
    thread = threading.Thread(target=run_server)
    thread.daemon = True
    thread.start()
    print("🌐 Web server started on port 10000")

    # Start bot
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.job_queue.run_repeating(
        send_reminder,
        interval=INTERVAL_HOURS * 3600,
        first=1
    )
    print(f"🚀 PaaniPeelo bot started! Sending reminders every {INTERVAL_HOURS} hour(s).")
    app.run_polling()