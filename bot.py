import os
import asyncio
import threading
import random
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram.ext import ApplicationBuilder

# ── Config ────────────────────────────────────────────────────
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = int(os.environ.get("CHAT_ID"))
INTERVAL_HOURS = 1

# ── Rotating messages ─────────────────────────────────────────
MESSAGES = [ """📱 Tera phone: 15% battery

Tu: *ignores*

Tera body: 15% hydration

Tu: *also ignores*

Bhai dono charge kar le ek saath. Paani pi! 🔋😂

https://www.instagram.com/reel/DVqtOvjivva/?igsh=MXNlNHcxZnFhcHlrMw==""",

"""🪦 Epitaph idea for dehydrated people:

"Yahan woh insaan sota hai,
Jo chai peeta tha, paani nahi.
Kidneys ne maafi nahi di.
RIP. 🪦"

Ye tu nahi banna chahta na? PAANI PI! 😂

https://www.instagram.com/reel/DVqtOvjivva/?igsh=MXNlNHcxZnFhcHlrMw==""",

"""📊 Aaj ki report:

Coffee pi: ✅  
Cold drink pi: ✅
Paani piya: ❌❌❌

Beta ye kaunsa health plan hai? 😭
Ja paani pi, abhi ke abhi!

https://www.instagram.com/reel/DVqtOvjivva/?igsh=MXNlNHcxZnFhcHlrMw==""",

"""
Bhayaa ek chewnchi bucks ki paani ki bottle dedo, muje pyas lagi haii!

https://www.instagram.com/reel/DVqtOvjivva/?igsh=MXNlNHcxZnFhcHlrMw==""",

"""👻 Agar dehydration ka bhoot hota na…

Toh sabse pehle tujhe hi pakadta. 💀

Bachna hai? PAANI PI!

https://www.instagram.com/reel/DVqtOvjivva/?igsh=MXNlNHcxZnFhcHlrMw==""",

"""Ant bant ka tola jisne paani nhi piyaa woh.....

https://www.instagram.com/reel/DVqtOvjivva/?igsh=MXNlNHcxZnFhcHlrMw==""",

"""This goat is a subtle reminder that if we too drink water we can be GOAT too..

https://www.instagram.com/reel/DVqtOvjivva/?igsh=MXNlNHcxZnFhcHlrMw==""",

""" pstttttttt... dekh halka sa gala sookh rha hoga, ek scheme deta hu

PAANI PEELE :)

https://www.instagram.com/reel/DVqtOvjivva/?igsh=MXNlNHcxZnFhcHlrMw=="""

]

# ── Dummy web server ──────────────────────────────────────────
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"PaaniPeelo bot is running!")
    def log_message(self, format, *args):
        pass

def run_server():
    server = HTTPServer(("0.0.0.0", 10000), Handler)
    server.serve_forever()

# ── Reminder message ──────────────────────────────────────────
async def send_reminder(context):
    message = random.choice(MESSAGES)
    await context.bot.send_message(
        chat_id=CHAT_ID,
        text=message
    )
    print("✅ Reminder sent!")

# ── Entry point ───────────────────────────────────────────────
if __name__ == "__main__":
    thread = threading.Thread(target=run_server)
    thread.daemon = True
    thread.start()
    print("🌐 Web server started on port 10000")

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.job_queue.run_repeating(
        send_reminder,
        interval=INTERVAL_HOURS * 3600,
        first=1
    )
    print(f"🚀 PaaniPeelo bot started! Sending reminders every {INTERVAL_HOURS} hour(s).")
    app.run_polling()