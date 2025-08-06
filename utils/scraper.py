# utils/scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_diseases():
    url = 'https://hellobacsi.com/benh/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    disease_list = []
    for item in soup.select('li.css-1g27dsp a.css-1ex9j7m'):
        name = item.text.strip()
        link = item.get('href')
        disease_list.append({
            'name': name,
            'link': link
        })
    return disease_list
