
import pandas
from sqlalchemy import create_engine

hostname="127.0.0.1"
uname="root"
pwd=""
dbname="zipcodes"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
            .format(host=hostname, db=dbname, user=uname, pw=pwd))

tables = pandas.read_csv(r"D:\Drive D\CNA335\week6\zip_code_database.csv")



connection=engine.connect()
tables.to_sql('States',con = engine, if_exists = 'replace')
connection.close()
print(tables)