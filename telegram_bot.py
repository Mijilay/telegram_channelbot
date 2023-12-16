import telegram
import os
from os import listdir
import random
from time import sleep
from dotenv import load_dotenv


def upload_files(bot):
    while True:
        folders = ["EPIC_images", "images", "launch_photos"]
        folder = random.choice(folders)
        files = listdir(folder)
        random.shuffle(files)
        for file in files:
            file_path = os.path.join(folder, file)
            with open(file_path, 'rb') as f:
                bot.send_document(chat_id=chat_id, document=f)
            sleep(14400)


def main():
    load_dotenv()
    bot_api_key = os.environ['BOT_API_KEY']
    chat_id = os.environ['TG_CHAT_ID']
    bot = telegram.Bot(token=bot_api_key)
    upload_files(bot)


if __name__ == '__main__':
    main()
