
import pytest
from app import schemas,config,models
# from .database import client ,session
import jwt




def test_create_users(client,session):
    res=client.post('/users',json={'email':'bidyutsikder42001@gmail.com','password':'bidyut'})

    print(res.json())
    user=schemas.UserResponse(**res.json())

    assert user.email=='bidyutsikder42001@gmail.com'
    assert res.status_code==201



def test_get_users(client,test_users):
    res=client.get(f'/users/{test_users['id']}')

    print(res.json())
    assert res.status_code==200



def test_login_users(client,session,test_users): # data=formdata,json=json data  
    res=client.post('/login',data={'username':test_users['email'],'password':test_users['password']})

    check_response_schemas=schemas.Token(**res.json())
    payload = jwt.decode(check_response_schemas.access_token, config.settings.SECRET_KEY, algorithms=[config.settings.ALGORITHM])
    assert check_response_schemas.token_type=='bearer'

    assert payload['user_id']==test_users['id']
    assert res.status_code==200








































