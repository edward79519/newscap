from sqlalchemy import Column, String, create_engine, exc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('mysql+pymysql://it_user:it_password@192.168.11.171/it_test?charset=utf8', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class News(Base):
    __tablename__ = 'news2'

    title = Column(String(100))
    time = Column(String(100))
    author = Column(String(100))
    provider = Column(String(100))
    url = Column(String(1000), primary_key=True)
    bfcn = Column(String(500))

    def __repr__(self):
        return ("標題： {}\n時間： {}\n作者： {}\n資料來源: {}\n網址: {}\n摘要: {}\n".format(
            self.title, self.time, self.author, self.provider, self.url, self.bfcn
        ))

for instance in session.query(News):
    print(instance.time)

