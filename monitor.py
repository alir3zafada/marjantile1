import os
import requests

TOKEN = os.environ.get("TOKEN")import os
import requests

TOKEN = os.environ.get("TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

URLS_TO_CHECK = [
    "https://www.marjantileco.com",
    "https://www.marjantileco.com/fa",
]


def send_telegram_message(message):
    if not TOKEN or not CHAT_ID:
        print("TOKEN or CHAT_ID is missing.")
        return

    telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
    }

    response = requests.post(telegram_url, json=payload, timeout=20)
    response.raise_for_status()


def check_website():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    last_error = ""

    for url in URLS_TO_CHECK:
        try:
            response = requests.get(
                url,
                headers=headers,
                timeout=20,
                allow_redirects=True,
            )

            if response.status_code < 400:
                return True, f"{response.url} - status {response.status_code}"

            last_error = f"{url} returned status {response.status_code}"

        except Exception as e:
            last_error = f"{url} error: {e}"

    return False, last_error or "Unknown error"


def main():
    is_up, info = check_website()

    if is_up:
        message = f"🟢 سایت در دسترس است\n{info}"
    else:
        message = f"🔴 سایت در دسترس نیست\n{info}"

    send_telegram_message(message)
    print(message)


if __name__ == "__main__":
    main()

CHAT_ID = os.environ.get("CHAT_ID")ذرزر

URLS_TO_CHECK = [
    "https://www.marjantileco.com",
    "https://www.marjantileco.com/fa",
]


def send_telegram_message(message):
    if not TOKEN or not CHAT_ID:
        print("TOKEN or CHAT_ID is missing.")
        return

    telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
    }

    response = requests.post(telegram_url, json=payload, timeout=20)
    response.raise_for_status()


def check_website():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    last_error = ""

    for url in URLS_TO_CHECK:
        try:
            response = requests.get(
                url,
                headers=headers,
                timeout=20,
                allow_redirects=True,
            )

            if response.status_code < 400:
                return True, f"{response.url} - status {response.status_code}"

            last_error = f"{url} returned status {response.status_code}"

        except Exception as e:
            last_error = f"{url} error: {e}"

    return False, last_error or "Unknown error"


def main():
    is_up, info = check_website()

    if is_up:
        message = f"🟢 سایت در دسترس است\n{info}"
    else:
        message = f"🔴 سایت در دسترس نیست\n{info}"

    send_telegram_message(message)
    print(message)


if __name__ == "__main__":
    main()
