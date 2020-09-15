from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('mysql+pymysql://it_user:it_password@192.168.11.171/it_test', echo=True)
metadata = MetaData(engine)
article = Table('news2', metadata,
                Column('title', String(100)),
                Column('time', String(100)),
                Column('author', String(100)),
                Column('provider', String(100)),
                Column('url', String(1000), primary_key=True),
                Column('bfcn', String(500)),
                )
metadata.create_all(engine)