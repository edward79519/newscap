import requests
from newscap.Article import Article
from newscap.udnmny_news_arti import articlepy
from bs4 import BeautifulSoup

def udnmoneypy(keywords):
    url = "https://money.udn.com/search/result/1001/" + keywords
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    html = BeautifulSoup(response.text)
    content = html.find("div", id="search_content")
    metas = content.find_all("dt")
    article_all = []
    for m in metas:
        title = m.find("h3").text
        provider = m.find("span", class_="cat").text.split("：")[0]
        bfcn = m.find("p").text
        url = m.find("a")["href"]
        arti = articlepy(url)
        #print(title, provider, bfcn, url, arti["name"], arti["time"])
        article = Article(title=title, time=arti["time"], author=arti["name"], provider=provider, url=url, bfcn=bfcn)
        # print(article)
        article_all.append(article)

    return article_all

'''
def main():
    udnmoneypy("%E5%AF%B6%E6%99%B6")

main()
'''