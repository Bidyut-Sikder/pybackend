
from typing import List
from app import schemas,models
import pytest



def test_vote_on_post(authorized_client,test_users,test_posts):
    post_id = test_posts[1].id
    res=authorized_client.post('/votes',json={"post_id": post_id,"direction": 1})

    assert res.status_code==201
    



@pytest.fixture()
def test_vote(test_users,test_posts,authorized_client,session):
    post_id = test_posts[3].id
    new_vote=models.Vote(post_id= post_id,user_id=test_users['id'])
    session.add(new_vote)
    session.commit()
    # return new_vote

    

def test_vote_twice_on_post(authorized_client,test_users,test_posts,test_vote):
    post_id = test_posts[3].id
    res=authorized_client.post('/votes',json={"post_id": post_id,"direction": 1})
    assert res.status_code==409
    





def test_delete_vote_on_post(authorized_client,test_users,test_posts,test_vote):
    post_id = test_posts[3].id
    res=authorized_client.post('/votes',json={"post_id": post_id,"direction": 0})
    assert res.status_code==201
    



def test_delete_vote_non_exist_post(authorized_client,test_users,test_posts):
    post_id = test_posts[3].id
    res=authorized_client.post('/votes',json={"post_id": post_id,"direction": 0})
    assert res.status_code==404
    


def test_vote_non_exist_post(authorized_client,test_users,test_posts):
    res=authorized_client.post('/votes',json={"post_id": 88,"direction": 1})
    assert res.status_code==404
    



def test_unauthorized_vote_on_post(client,test_users,test_posts):
    post_id = test_posts[3].id
    res=client.post('/votes',json={"post_id": post_id,"direction": 1})
    assert res.status_code==401
    










