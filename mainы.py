import requests 
import os
import random
from dotenv import load_dotenv
import telegram


def download_a_comic_book(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
      file.write(response.content)


def get_count_comic():
    url = "https://xkcd.com//info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    information_of_comic = response.json() 
    number = information_of_comic["num"]
    return number


def get_comic_information():
    url = f"https://xkcd.com/{random.randint(1, get_count_comic())}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    information_of_comic = response.json()
    comment = information_of_comic["alt"]
    title = information_of_comic["title"]
    comic_url = information_of_comic["img"]
    return comment, title, comic_url


def upload_comic(token_tg, tg_chat_id, title, comment):
    bot = telegram.Bot(token=token_tg)
    with open(f"{title}.png", "rb") as f:
      bot.send_document(chat_id=tg_chat_id, document=f, caption=comment)


def main():
    load_dotenv() 
    tg_chat_id = os.environ["TG_CHAT_ID"]
    token_tg = os.environ["TOKEN_TG"]
    try:
        comment, title, comic_url = get_comic_information()
        download_a_comic_book(comic_url, f"{title}.png")
        upload_comic(token_tg, tg_chat_id, title, comment)
    finally:
        os.remove(f"{title}.png")


if __name__ == '__main__':
    main()
