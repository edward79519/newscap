import requests
from bs4 import BeautifulSoup

def articlepy(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    html = BeautifulSoup(response.text)
    meta = html.find_all("div", class_="paragraph")[0]
    title = html.find("h1").text
    author = meta.find_all("p")[0].text.split("）")[0].split("記者")[1][0:3]
    bfcn = meta.find_all("p")[0].text.split("）")[1]


    atri_dict = {
        "title": title,
        "name": author,
        "bfcn": bfcn,
    }
    return atri_dict

'''
def main():
    a = articlepy("https://www.cna.com.tw/news/aloc/202003050410.aspx")
    print(a)
main()
'''