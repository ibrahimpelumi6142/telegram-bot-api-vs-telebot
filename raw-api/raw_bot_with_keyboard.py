import requests
import time

BOT_TOKEN = "YOUR_BOT_TOKEN"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def send_message(chat_id, text, reply_markup=None):
    url = f"{BASE_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    if reply_markup:
        payload["reply_markup"] = reply_markup

    requests.post(url, json=payload)


def get_updates(offset=None):
    url = f"{BASE_URL}/getUpdates"
    params = {"timeout": 30}
    if offset:
        params["offset"] = offset

    return requests.get(url, params=params).json()


def start_keyboard():
    return {
        "keyboard": [
            [{"text": "📄 About"}, {"text": "❓ Help"}]
        ],
        "resize_keyboard": True,
        "one_time_keyboard": False
    }


def inline_keyboard():
    return {
        "inline_keyboard": [
            [
                {"text": "🌍 Website", "url": "https://example.com"},
                {"text": "❓ Help", "callback_data": "help"}
            ]
        ]
    }


def main():
    print("🤖 RAW Telegram bot with keyboard running...")
    offset = None

    while True:
        updates = get_updates(offset)

        for update in updates.get("result", []):
            offset = update["update_id"] + 1

            # Handle normal messages
            if "message" in update:
                msg = update["message"]
                chat_id = msg["chat"]["id"]
                text = msg.get("text", "")

                if text == "/start":
                    send_message(
                        chat_id,
                        "Welcome! Choose an option:",
                        reply_markup=start_keyboard()
                    )

                elif text == "📄 About":
                    send_message(chat_id, "This bot uses RAW Telegram Bot API.")

                elif text == "❓ Help":
                    send_message(chat_id, "Use the keyboard buttons to interact.")

                elif text == "/inline":
                    send_message(
                        chat_id,
                        "Inline keyboard:",
                        reply_markup=inline_keyboard()
                    )

                else:
                    send_message(chat_id, f"You said: {text}")

            # Handle inline callbacks
            elif "callback_query" in update:
                callback = update["callback_query"]
                chat_id = callback["message"]["chat"]["id"]
                data = callback["data"]

                if data == "help":
                    send_message(chat_id, "This is inline help from RAW API.")

        time.sleep(1)


if __name__ == "__main__":
    main()
