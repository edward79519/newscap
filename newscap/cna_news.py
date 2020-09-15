import requests
from bs4 import BeautifulSoup
from newscap.cna_news_arti import articlepy
from newscap.Article import Article

def cnapy(keyword):

    url = "https://www.cna.com.tw/search/hysearchws.aspx?q=" + keyword
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    html = BeautifulSoup(response.text)
    content = html.find("ul", id="jsMainList")
    metas = content.find_all("li")
    article_all = []

    for m in metas:
        url = m.find("a")["href"]
        title = m.find("h2").text
        a_time = m.find("div", class_="date").text
        provider = "中央社"
        arti_dict = articlepy(url)
        # print(title, a_time, provider, arti_dict["name"], url, arti_dict["bfcn"])
        arti = Article(title=title, time=a_time, author=arti_dict["name"], provider=provider, url=url, bfcn=arti_dict["bfcn"])
        article_all.append(arti)
        # print(arti)

    return article_all


'''
def main():
    cnapy("%E5%AF%B6%E6%99%B6")
main()
'''