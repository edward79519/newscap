from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('mysql+pymysql://it_user:it_password@192.168.11.171/it_test', echo=True)
DBsession = sessionmaker(bind=engine)
session = DBsession()

class Stud(Base):
    __tablename__ = 'student'

    name = Column(String(50))
    birth = Column(String(30))
    number = Column(String(20), primary_key=True)


a = Stud(name="Edwad", birth="1990-05-10", number="03")
b = Stud(name="YEEE", birth="1994-05-19", number="02")
aa = [a, b]
session.add_all(aa)
session.commit()
session.close()