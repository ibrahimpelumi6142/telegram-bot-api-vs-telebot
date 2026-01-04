import requests
import time

BOT_TOKEN = "YOUR_BOT_TOKEN"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def get_updates(offset=None):
    url = f"{BASE_URL}/getUpdates"
    params = {"timeout": 30}
    if offset:
        params["offset"] = offset

    response = requests.get(url, params=params)
    return response.json()


def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=payload)


def main():
    print("🤖 Raw Telegram bot started...")
    offset = None

    while True:
        updates = get_updates(offset)

        for update in updates.get("result", []):
            offset = update["update_id"] + 1

            if "message" not in update:
                continue

            message = update["message"]
            chat_id = message["chat"]["id"]
            text = message.get("text", "")

            if text == "/start":
                send_message(chat_id, "👋 Hello from RAW Telegram API!")
            elif text == "/help":
                send_message(chat_id, "Commands:\n/start\n/help")
            else:
                send_message(chat_id, f"You said: {text}")

        time.sleep(1)


if __name__ == "__main__":
    main()
