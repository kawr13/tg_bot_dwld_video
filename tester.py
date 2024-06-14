import asyncio
import os
import glob
import httpx
import requests
from icecream import ic
import pyktok as pyk

client = httpx.AsyncClient()


cookies = {
    'XSRF-TOKEN': 'eyJpdiI6Im5yaEc4Q3NBOTdxTFh6ZXBranpTYkE9PSIsInZhbHVlIjoiVHZ6RnBVU3I2VWlwazJtWUZ3b3lMMmwxZUswN3BVczRlWlBpRkpVUXRoK0Q3TVRRVEIxUkxZVnRmN1FFZWU4ZVUyTXlQUEV6Sy92VmNqeUV4QzBsSjhPTTNpclNDK2NBbDVtRmdWM1I5SzlRVDI1WTdOTTNjTS9zVU5aMEZ4SnciLCJtYWMiOiJjNmNkODc0ZWNlZjU1Mzc5ZTZlMzYxNGZjYTcyYjIxYWFlNTNiODg2OGU5ZjUxYzFjYTFkOTZlYzIwNDdlOWE2IiwidGFnIjoiIn0%3D',
    'savefromkim_clone_session': 'eyJpdiI6IlhQRUU1ZHRhbXpUdkkxSjVSTWVTT3c9PSIsInZhbHVlIjoiRjhabFBkTlV6VFcxWnFBS21xeHpNVVdLVE85Y0ZPYnoyZy9ORmNwaDFhb0FWckV3Qk1oQU10SzFtN2lNUzBaWEhNM3c4Vjk1bVYrdEZZUmV4OXhGQllyQXZDYXlXNVNrZ3ZsTXI5VFQzOWR5S01SQnRYVWkzbkh4VTgzd0dJNjkiLCJtYWMiOiJkMTdmNzg3OTI1N2M4ZmYxNWY2OTcwMTlkNzQ0ODg3ZWM2ZjE2M2JkYTI1NGViMDNjMjc0OWYzM2RmZmUxY2IyIiwidGFnIjoiIn0%3D',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.8',
    'content-type': 'application/json',
    # 'cookie': 'XSRF-TOKEN=eyJpdiI6Im5yaEc4Q3NBOTdxTFh6ZXBranpTYkE9PSIsInZhbHVlIjoiVHZ6RnBVU3I2VWlwazJtWUZ3b3lMMmwxZUswN3BVczRlWlBpRkpVUXRoK0Q3TVRRVEIxUkxZVnRmN1FFZWU4ZVUyTXlQUEV6Sy92VmNqeUV4QzBsSjhPTTNpclNDK2NBbDVtRmdWM1I5SzlRVDI1WTdOTTNjTS9zVU5aMEZ4SnciLCJtYWMiOiJjNmNkODc0ZWNlZjU1Mzc5ZTZlMzYxNGZjYTcyYjIxYWFlNTNiODg2OGU5ZjUxYzFjYTFkOTZlYzIwNDdlOWE2IiwidGFnIjoiIn0%3D; savefromkim_clone_session=eyJpdiI6IlhQRUU1ZHRhbXpUdkkxSjVSTWVTT3c9PSIsInZhbHVlIjoiRjhabFBkTlV6VFcxWnFBS21xeHpNVVdLVE85Y0ZPYnoyZy9ORmNwaDFhb0FWckV3Qk1oQU10SzFtN2lNUzBaWEhNM3c4Vjk1bVYrdEZZUmV4OXhGQllyQXZDYXlXNVNrZ3ZsTXI5VFQzOWR5S01SQnRYVWkzbkh4VTgzd0dJNjkiLCJtYWMiOiJkMTdmNzg3OTI1N2M4ZmYxNWY2OTcwMTlkNzQ0ODg3ZWM2ZjE2M2JkYTI1NGViMDNjMjc0OWYzM2RmZmUxY2IyIiwidGFnIjoiIn0%3D',
    'origin': 'https://savefrom.kim',
    'priority': 'u=1, i',
    'referer': 'https://savefrom.kim/ru/',
    'sec-ch-ua': '"Brave";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'x-xsrf-token': 'eyJpdiI6Im5yaEc4Q3NBOTdxTFh6ZXBranpTYkE9PSIsInZhbHVlIjoiVHZ6RnBVU3I2VWlwazJtWUZ3b3lMMmwxZUswN3BVczRlWlBpRkpVUXRoK0Q3TVRRVEIxUkxZVnRmN1FFZWU4ZVUyTXlQUEV6Sy92VmNqeUV4QzBsSjhPTTNpclNDK2NBbDVtRmdWM1I5SzlRVDI1WTdOTTNjTS9zVU5aMEZ4SnciLCJtYWMiOiJjNmNkODc0ZWNlZjU1Mzc5ZTZlMzYxNGZjYTcyYjIxYWFlNTNiODg2OGU5ZjUxYzFjYTFkOTZlYzIwNDdlOWE2IiwidGFnIjoiIn0=',
}


headers_t = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.5',
    'content-type': 'application/json',
    'origin': 'https://www.tiktok.com',
    'priority': 'u=1, i',
    'referer': 'https://www.tiktok.com/',
    'sec-ch-ua': '"Brave";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}

params_t = {
    'bid': 'tiktok_webapp',
    'store': '1',
}


async def find_file_by_suffix(suffix):
    directory = os.getcwd()
    for root, dirs, files in os.walk(directory):

        for file in files:
            if file.endswith(suffix):
                ic(f'{root}/{file}')
                return file
    return None


async def dwnld_vid(url, cookies=None, headers=None, data=None):
    resp = requests.post(url, cookies=cookies, headers=headers, json=data)
    return resp


async def download_tiktok_video(url):
    pyk.specify_browser('chrome')
    data = pyk.save_tiktok(f'{url}?is_copy_url=1&is_from_webapp=v1',
                    True,
                    'video_data.csv',
                    'chrome')


async def load_main(string):
    url = 'https://savefrom.kim/api/convert'
    json_data = {
        'url': string,
    }

    resp = await dwnld_vid(url, data=json_data)
    dict_ = resp.json()
    quality = dict_['video_quality']
    quality.append('audio')
    title = dict_['meta']['title']
    urls = dict_['url']
    return urls, quality, title


async def download_tiktok_start(url):
    await download_tiktok_video(url)
    suffix = url.split('/')[-1] + '.mp4'
    count = 0
    while True:
        file_path = await find_file_by_suffix(suffix)
        if file_path:
            return file_path
        else:
            await asyncio.sleep(10)
            count += 1
            if count == 10:
                break



if __name__ == '__main__':
    asyncio.run(download_tiktok_start('https://www.tiktok.com/@maryaznn/video/7030872841532738818'))
