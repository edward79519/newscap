import requests
from newscap.yahoo_news_arti import articlepy
from newscap.Article import Article
from bs4 import BeautifulSoup
import time

def yahoopy(keywords):
    url = "https://tw.news.yahoo.com/search?p=" + keywords
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    html = BeautifulSoup(response.text)
    content = html.find("div", id="Main")
    metas = content.find_all("li", class_="StreamMegaItem")
    article_all = []

    for m in metas:
        try:
            text_title = m.find('h3', class_="Mb(5px)").text #標題
            text_url = "https://tw.news.yahoo.com" + m.find('a')["href"] #連結
            text_in = articlepy(text_url)
            time.sleep(1)
            text_bfcont = m.find("p").text[:100]
            #print(text_title, text_in["time"], text_in["name"], text_in["provider"], text_url)
            #print(text_bfcont)
            article = Article(text_title, text_in["time"], text_in["name"], text_in["provider"], text_url, text_bfcont)
            # print(article)
            article_all.append(article)

        except:
            print("Wrong")

    return article_all



def main():
    article_all = yahoopy("%E5%AF%B6%E6%99%B6")
    print(len(article_all))

main()
