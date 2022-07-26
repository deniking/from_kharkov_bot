import requests
import random
from bs4 import BeautifulSoup as b

URL = 'https://www.anekdot.ru/release/anekdot/day/'

def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    anekdot = soup.find_all('div', class_='text')
    return [c.text for c in anekdot]

list = parser(URL)
random.shuffle(list)

