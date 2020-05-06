import pandas as pd

########################
# Create MYSQL DB
#  CREATE DATABASE db_name;

# Push data to mysql

# pip install sqlalchemy
# sudo apt-get install python-mysqldb

import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('data.csv')

#print(df.head())

engine = create_engine('mysql://root:MyPass@localhost/#NAME_OF_THE_DATABASE#')
with engine.connect() as conn, conn.begin():
    df.to_sql('#NAME_OF_THE_TABLE',conn,if_exists='append',index=False)


