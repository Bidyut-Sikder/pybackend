
# Code written in this file will be accessible to all the test files and folders.

from app.main import app
from fastapi.testclient import TestClient
from app import schemas,config,database,models
from sqlalchemy import create_engine
from  sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pytest

TEST_DATABASE_URl = f"postgresql+psycopg2://postgres:bidyut@localhost:5432/pybackend_test_db"

engine = create_engine(TEST_DATABASE_URl)

Testing_Session_SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)



@pytest.fixture(scope='function') #scope='module' is used for holding the session instance for the entire file

def session():
    print('my sesssion fixture ran')
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
