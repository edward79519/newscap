import requests
from bs4 import BeautifulSoup
from datetime import datetime

def articlepy(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    html = BeautifulSoup(response.text)
    arti_title = html.find("header", id="Col1-1-HeadComponentTitle").text
    arti_provi = html.find('span', class_="provider-link").text
    arti_name = html.find("div", itemprop="name").text
    arti_time = html.find("time", itemprop="datePublished")["datetime"]
    #print(arti_title, arti_provi, arti_name, arti_time)

    atri_dict = {
        "title": arti_title,
        "time": arti_time,
        "name": arti_name,
        "provider": arti_provi,
    }
    return atri_dict
