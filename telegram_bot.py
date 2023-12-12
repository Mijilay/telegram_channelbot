import telegram
import os
from os import listdir
import random
from time import sleep
from dotenv import load_dotenv


def takeFiles(bot):
    while True:
        folders = ["EPIC_images", "images", "launch_photos"]
        folder = random.choice(folders)
        files = listdir(folder)
        random.shuffle(files)
        for file in files:
            file_path = os.path.join(folder, file)
            with open(file_path, 'rb') as f:
                bot.send_document(chat_id='@jujsen', document=f)
            sleep(1)

def main():
    load_dotenv()
    botapikey = os.environ['BOT_API_KEY']
    bot = telegram.Bot(token=botapikey)
    takeFiles(bot)

if __name__ == '__main__':
    main()
