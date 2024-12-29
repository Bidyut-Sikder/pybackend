
# Code written in this file will be accessible to all the test files and folders.

from app.main import app
from fastapi.testclient import TestClient
from app import schemas,config,database,models,auth2
from sqlalchemy import create_engine
from  sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pytest

# TEST_DATABASE_URl = f"postgresql+psycopg2://postgres:bidyut@localhost:5432/pybackend_test_db"
TEST_DATABASE_URl = f"postgresql+psycopg2://{config.settings.database_username}:{config.settings.database_password}@{config.settings.database_host}:{config.settings.database_port}/{config.settings.database_name}_test"
engine = create_engine(TEST_DATABASE_URl)

Testing_Session_SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)



@pytest.fixture(scope="function") #scope='module' is used for holding the session instance for the entire file
def session():

    models.Base.metadata.drop_all(bind=engine)# we drop our table before if we have then we run our test

    models.Base.metadata.create_all(bind=engine)# we create our table before starting the test
    
    db=Testing_Session_SessionLocal()
    try:
        yield db
    finally:
        db.close()




@pytest.fixture()
def client(session):

    # Run our code before we run our test
    def overrid_get_db():
     try:
        yield session
     finally:
        session.close()
        
    app.dependency_overrides[database.get_db]=overrid_get_db
    yield TestClient(app)


@pytest.fixture
def test_users(client,session):
    user_Data={'email':'bidyutsikder4@gmail.com','password':'bidyut'}
    res= client.post('/users',json=user_Data)    
    new_user=res.json()                   
    assert res.status_code==201 
    new_user['password']=user_Data['password']
    return new_user




@pytest.fixture
def test_users2(client,session):
    user_Data={'email':'bidyutsikder41@gmail.com','password':'bidyut'}
    res= client.post('/users',json=user_Data)    
    new_user=res.json()                   
    assert res.status_code==201 
    new_user['password']=user_Data['password']
    return new_user











@pytest.fixture
def token(test_users):
    return auth2.create_access_token({"user_id":test_users['id']})
    
@pytest.fixture
def authorized_client(client,token):
    client.headers={
        **client.headers,
        "Authorization":f"Bearer {token}"
        }
    return client
    
    
# Creating some dummy posts..
@pytest.fixture
def test_posts(test_users,session,test_users2):
    posts_data=[
        {'title':'first post','content':'first post content','user_id':test_users['id']},
        {'title':'second post','content':'second post content','user_id':test_users['id']},
        {'title':'third post','content':'third post content','user_id':test_users['id']},
        {'title':'third post','content':'third post content','user_id':test_users2['id']}
        ]
    def create_post_modal(post):
       return models.Post(**post)
        
    posts_map=map(create_post_modal,posts_data)
   
    posts=list(posts_map)
    print(posts)
    session.add_all(posts) # we converted map to list
    session.commit()
    posts=session.query(models.Post).all()
    return posts
















