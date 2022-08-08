import requests
import random
from bs4 import BeautifulSoup as b

URL = 'https://resheto.net/raznosti/310-vyskazyvaniya-fainy-ranevskoj'

def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    aforizm = soup.find_all('p', class_='note')
    aforizm1 = soup.find_all('p', class_='notey')
    return [c.text for c in aforizm and aforizm1]

list = parser(URL)
random.shuffle(list)

