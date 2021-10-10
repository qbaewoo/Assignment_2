import requests
from bs4 import BeautifulSoup as bs

URL = 'https://coinmarketcap.com/ru/currencies/bitcoin/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0', 'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = bs(html, 'html.parser')
    items = soup.find_all(
        'p')

    print(items)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')


parse()
