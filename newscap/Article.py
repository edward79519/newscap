class Article:
    def __init__(self, title, time, author, provider, url, bfcn):
        self.title = title
        self.time = time
        self.author = author
        self.provider = provider
        self.url = url
        self.bfcn = bfcn

    def __str__(self):
        return ("標題： {}\n時間： {}\n作者： {}\n資料來源: {}\n網址: {}\n摘要: {}\n".format(
            self.title, self.time, self.author, self.provider, self.url, self.bfcn
        ))