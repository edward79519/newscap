from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('mysql+pymysql://it_user:it_password@192.168.11.171/it_test', echo=True)
metadata = MetaData(engine)
article = Table('student', metadata,
                Column('name', String(50)),
                Column('birth', String(30)),
                Column('number', String(20)),
                )
metadata.create_all(engine)