import requests
import os
from download import download_pic
from dotenv import load_dotenv


def fetch_spacex_last_launch():
    launches_id_url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(launches_id_url)
    response.raise_for_status()
    pics = response.json()['links']['flickr']['original']
    for number, pic in enumerate(pics):
        filename = f'spacex{number}.jpg'
        filepath = os.path.join('launch_photos', filename)
        download_pic(pic, filepath)
        print('Downloaded spacex{}.jpg'.format(number))
def main():
    fetch_spacex_last_launch()

if __name__ == "__main__":
    main()