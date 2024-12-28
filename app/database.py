


import time
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from psycopg2.extras import RealDictCursor
from . import config


# print(config.settings)
# Create the connection string

# DATABASE_URl = 'postgresql://bidyut:Kknc80HuNRFrAtYlsHEU8KqnqJ5YKWo8@dpg-ctkeuqij1k6c73co8430-a.singapore-postgres.render.com/pybackend'
# DATABASE_URl = f"postgresql+psycopg2://{config.settings.database_username}:{config.settings.database_password}@{config.settings.database_host}.singapore-postgres.render.com/{config.settings.database_name}"

DATABASE_URl = f"postgresql+psycopg2://{config.settings.database_username}:{
    config.settings.database_password}@{
        config.settings.database_host}:5432/{config.settings.database_name}"





engine = create_engine(DATABASE_URl)



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





