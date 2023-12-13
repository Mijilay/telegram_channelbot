import requests
import os
from datetime import datetime
from download import download_pic
from dotenv import load_dotenv


def save_epic_pics(apikey):
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    count = 5
    params={'api_key' : apikey,'count':count}
    response = requests.get(epic_url, params=params)
    response.raise_for_status()
    pictures = response.json()
    os.mkdir('EPIC_images')
    for picture in pictures:
        epic_name = picture['image']
        epic_date = picture['date']
        stnd_date = datetime.fromisoformat(epic_date).strftime('%Y/%m/%d')
        formatted_url = f"https://api.nasa.gov/EPIC/archive/natural/{stnd_date}/png/{epic_name}.png"
        filepath = os.path.join('EPIC_images', f'{epic_name}.png')
        download_pic(formatted_url, filepath, params)


def main():
    load_dotenv()
    apikey = os.environ['NASA_API_KEY']
    save_epic_pics(apikey)


if __name__ == '__main__':
    main()

