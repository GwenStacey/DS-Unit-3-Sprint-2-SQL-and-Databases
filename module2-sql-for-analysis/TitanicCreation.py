import psycopg2
import sqlite3
import pandas as pd

#Quickly establish dataframe, remove single quotes from names
#to run the query properly
df = pd.read_csv('titanic.csv')
df['Name'] = df['Name'].str.replace("'", "", regex=True)
df.head()

#Establish parameters for elephantsql setup
dbname = 'oeoiketr'
user = 'oeoiketr'
password = 'br_jAI5i6XM0D6roMuvNKUY99OWZ_X0D'
host = 'salt.db.elephantsql.com'

#Establish connection to elephantsql db and a cursor
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
curs = conn.cursor()

#Create titanic table in elephantsql db
curs.execute('''CREATE TABLE titanic_table (
                   id SERIAL PRIMARY KEY,
                   survived INT,
                   pclass INT,
                   name VARCHAR(100),
                   sex VARCHAR(10),
                   age FLOAT,
                   sibs_spouse INT,
                   par_child INT,
                   fare FLOAT);
                ''')
conn.commit()

#Create sqlite3 db to ease transition and cursor 
sl_conn = sqlite3.connect('titantic_temp.sqlite3')
sl_curs = sl_conn.cursor()
#Convert dataframe to sqlobject
df.to_sql('titanic_temp', sl_conn)
#Create list of objects to loop through
passengers = sl_curs.execute('SELECT * FROM titanic_temp;').fetchall()
#Loop through items and add them to elephantsql db
for passenger in passengers:
    curs.execute("INSERT INTO titanic_table VALUES" + str(passenger) + ";")

#Finalize changes
conn.commit()