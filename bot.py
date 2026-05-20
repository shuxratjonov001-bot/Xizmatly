import requests
import time

BOT_TOKEN = "8976214135:AAHowyeJ_IHnX76tJp8r7rfEvG83qD2FlrU"
WEBAPP_URL = "https://xizmatlyy.netlify.app"
API = f"https://api.telegram.org/bot{BOT_TOKEN}"

offset = 0

def send_message(chat_id, text, reply_markup=None):
    data = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
    if reply_markup:
        import json
        data["reply_markup"] = json.dumps(reply_markup)
    requests.post(f"{API}/sendMessage", data=data)

def handle_update(update):
    if "message" not in update:
        return
    msg = update["message"]
    chat_id = msg["chat"]["id"]
    text = msg.get("text", "")
    
    if text == "/start":
        keyboard = {
            "inline_keyboard": [[
                {
                    "text": "🛠️ Xizmatlyni ochish",
                    "web_app": {"url": WEBAPP_URL}
                }
            ]]
        }
        send_message(
            chat_id,
            "👋 <b>Assalomu alaykum!</b>\n\nXizmatly — mutaxassislar platformasi.\n\nQuyidagi tugmani bosib kirish mumkin 👇",
            keyboard
        )

print("Bot ishga tushdi...")

while True:
    try:
        res = requests.get(f"{API}/getUpdates", params={"offset": offset, "timeout": 30})
        data = res.json()
        
        if data.get("ok"):
            for update in data["result"]:
                offset = update["update_id"] + 1
                handle_update(update)
    except Exception as e:
        print(f"Xato: {e}")
        time.sleep(3)
