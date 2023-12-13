import requests
import os
from download import download_pic
from dotenv import load_dotenv


def fetch_spacex_last_launch(launch_id):
    launches_id_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(launches_id_url)
    response.raise_for_status()
    os.mkdir('launch_photos')
    pics = response.json()['links']['flickr']['original']
    for number, pic in enumerate(pics):
        filename = f'spacex{number}.jpg'
        filepath = os.path.join('launch_photos', filename)
        download_pic(pic, filepath)


def main():
    parser = argparse.ArgumentParser(
        description='Програма позволяет скачивать фотографии с запуска SpaceX и сохранять их в папку'
    )
    parser.add_argument('--id', dest="launch_id", help='Напишите id запуска SpaceX', default = "5eb87d47ffd86e000604b38a")
    args = parser.parse_args()
    fetch_spacex_last_launch(args.launch_id)


if __name__ == "__main__":
    main()
