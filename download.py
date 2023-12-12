import requests


def download_pic(url, filename, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)