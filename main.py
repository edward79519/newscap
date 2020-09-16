from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, create_engine, exc, DateTime
from sqlalchemy.orm import sessionmaker
from newscap.yahoo_news import yahoopy
from newscap.cna_news import cnapy
from newscap.storm_news import stormpy
from newscap.udnmoney_news import udnmoneypy
from datetime import datetime

Base = declarative_base()
engine = create_engine('mysql+pymysql://it_user:it_password@192.168.11.171/it_test?charset=utf8&binary_prefix=true', echo=True)
DBsession = sessionmaker(bind=engine)
session = DBsession()

class News(Base):
    __tablename__ = 'news3'

    title = Column(String(100))
    #time = Column(String(100))
    time = Column(DateTime)
    author = Column(String(100))
    provider = Column(String(100))
    url = Column(String(1000), primary_key=True)
    bfcn = Column(String(500))

    def __repr__(self):
        return ("標題： {}\n時間： {}\n作者： {}\n資料來源: {}\n網址: {}\n摘要: {}\n".format(
            self.title, self.time, self.author, self.provider, self.url, self.bfcn
        ))


def main():
    keywords = "%E5%AF%B6%E6%99%B6"

    article_yahoo = yahoopy(keywords)
    article_cna = cnapy(keywords)
    article_storm = stormpy(keywords)
    article_udnmny = udnmoneypy(keywords)

    article_all = article_cna + article_yahoo + article_udnmny + article_storm


    # news_list = []
    for a in article_all:
        news_item = News(title=a.title, time=a.time, author=a.author, provider=a.provider, url=a.url, bfcn=a.bfcn)
        #news_list.append(news_item)

        '''
        session.add(news_item)
        session.commit()
        '''

        try:
            session.add(news_item)
            session.commit()
        except exc.IntegrityError as e:
            print("error: ", e)
        except exc.InvalidRequestError as e:
            print("error: ", e)
        print(a)

    #session.add_all(news_list)
    #session.commit()
    session.close()

main()