import requests
import os 
from urllib.parse import unquote, urlparse
from datetime import datetime
from download import download_pic
from dotenv import load_dotenv


def extention_image(url):
    decoded_url = unquote(url)
    parsed_url = urlparse(decoded_url)
    path, fullname = os.path.split(parsed_url.path)
    file_extention_path = os.path.splitext(fullname)
    filename, extention = file_extention_path
    return extention, filename


def fetch_apod_images(apikey):
    os.mkdir('images')
    count = 35
    apod_url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key' : apikey,'count':count}
    response = requests.get(apod_url, params=params)
    response.raise_for_status()
    pictures = response.json()
    for picture in pictures:
        if picture.get('media_type') == 'image':
            if picture.get("hdurl"):
                nasa_url = picture['hdurl']
            else:
                nasa_url = picture['url']
            extention, filename = extention_image(nasa_url)
            filepath = os.path.join('images', f'{filename}{extention}')
            download_pic(nasa_url, filepath)


def main():
    load_dotenv()
    apikey = os.environ['NASA_API_KEY']
    fetch_apod_images(apikey)


if __name__ == "__main__":
    main()
