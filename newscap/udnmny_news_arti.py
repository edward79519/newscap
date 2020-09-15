import requests
from bs4 import BeautifulSoup

def articlepy(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    html = BeautifulSoup(response.text)
    content = html.find("div", id="story_body")
    title = content.find("h2", id="story_art_title").text
    a_time = content.find("div", class_="shareBar__info--author").find("span").text
    author = content.find("div", class_="shareBar__info--author").text.strip(a_time)
    author = author.replace("記者", "").split(" ")[1][0:3]
    # print(title, a_time, author)
    atri_dict = {
        "title": title,
        "time": a_time,
        "name": author,
    }
    # print(atri_dict)
    return atri_dict

'''
def main():
    articlepy("https://money.udn.com/money/story/5612/4391852")

main()
'''