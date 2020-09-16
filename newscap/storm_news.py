import requests
from newscap.Article import Article
from bs4 import BeautifulSoup
from datetime import datetime

def stormpy(keywords):
    url = "https://www.storm.mg/site-search/result?q=" + keywords
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    html = BeautifulSoup(response.text)
    content = html.find("div", id="category_content")
    metas = content.find_all("div", class_="category_card")
    article_all = []

    for m in metas:
        title = m.find("p", class_="card_title").text
        author = m.find("span", class_="info_author").text
        # a_time = m.find("span", class_="info_time").text
        a_time = datetime.strptime(m.find("span", class_="info_time").text, "%Y-%m-%d %H:%M")
        provider = "風傳媒"
        bfcn = m.find("a", class_="card_substance").text
        url = "https://www.storm.mg" + m.find("a", class_="card_link")["href"]
        #print(title, author, a_time, url, bfcn)
        arti = Article(title=title, time=a_time, author=author, provider=provider, url=url, bfcn=bfcn)
        article_all.append(arti)
        #print(arti)

    return article_all

'''
def main():
    stormpy("%E5%AF%B6%E6%99%B6")

main()
'''