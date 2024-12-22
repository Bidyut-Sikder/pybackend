


import time
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from psycopg2.extras import RealDictCursor
from . import config

# username = "postgres"
# password = "bidyut"
# host = "localhost"  
# port = "5432"      
# database = "pybackend"

# print(config.settings)
# Create the connection string
DATABASE_URL = f"postgresql://{config.settings.database_username}:{config.settings.database_password}@{config.settings.database_host}:{config.settings.database_port}/{config.settings.database_name}"
# print(DATABASE_URL)
# DATABASE_URL = f"postgresql://{username}:{password}@{host}:{port}/{database}"
# print(DATABASE_URLl)


engine = create_engine(DATABASE_URL)



SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)


Base=declarative_base()


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()



# if we want to use raw sql query in our application we can use the following code.

# import psycopg2
# while True:
#     try:
#         conn=psycopg2.connect(host='localhost',database='pybackend',
#                               user='postgres',
#                               password='bidyut',
#                               cursor_factory=RealDictCursor)
#         cursor=conn.cursor()    
    
#         print("Database connection was successful")
#         break
#     except Exception as error:
#         print("Failed to connect to database")
#         print("Error:",error)
#         #time.sleep(2)
       
  
 



#we have posts table and users table.
#right join means we want to get all the right table data though the left table data is null
#left join means we want to get all the left table data though the right table data is null

# SELECT email,count(posts.id)  FROM posts right join users on 
# posts.user_id=users.id group by users.email

# We can grouping the data by using group by keyword in sql query

# SELECT email,count(posts.id)  FROM posts right join users on 
# posts.user_id=users.id group by users.email


# SELECT posts.* ,count(votes.post_id) FROM posts left join votes 
# on votes.post_id=posts.id where posts.id=17
# group by posts.id





