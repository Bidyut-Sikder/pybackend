
from typing import List
from app import schemas
import pytest


@pytest.mark.parametrize('title,content,published',[
    ('fruits tree 1','trees cut down',True),
    ('fruits tree 10','fence fell apart',True),
    ('fruits tree 14','divide the land',False),
    ])
def test_create_posts(authorized_client,title,content,published,test_users):
    res=authorized_client.post('/posts',json={
        "title": title,
        "content": content,
        "published": published

    })
    new_post=res.json()
    check_schema=schemas.Post(**new_post)
    assert check_schema.title==title
    assert check_schema.content==content
    assert check_schema.user_id==test_users['id']
    assert res.status_code==201


def test_create_posts_defalut_published_true(authorized_client,test_users):
    res=authorized_client.post('/posts',json={
        "title": 'mango tree',
        "content": 'mango'
    })
    new_post=res.json()
    check_schema=schemas.Post(**new_post)
    assert check_schema.title=='mango tree'
    assert check_schema.content== 'mango'
    assert check_schema.user_id==test_users['id']
    assert res.status_code==201




def test_unauthorized_create_posts(client,test_users):
    res=client.post('/posts/',json={
        "title": 'mango tree',
        "content": 'mango'
    })

    assert res.status_code==401



def test_authorized_delete_posts(authorized_client,test_posts):
    res=authorized_client.delete(f'/posts/{test_posts[0].id}')

    assert res.status_code==200

def test_delete_non_exist_posts(authorized_client,test_posts):
    res=authorized_client.delete(f'/posts/444')

    assert res.status_code==404



def test_unauthorized_delete_posts(client,test_posts):
    res=client.delete(f'/posts/{test_posts[0].id}')

    assert res.status_code==401



def test_delete_other_user_posts(authorized_client,test_posts):
    res=authorized_client.delete(f'/posts/{test_posts[3].id}')

    assert res.status_code==403




def test_update_posts(authorized_client,test_posts,test_users):
    json_data={
        "title": 'a nice salad for the dinner',
        "content": 'cucumbar',
        "id":test_posts[0].id
        
    }
    res=authorized_client.put(f'/posts/{test_posts[0].id}',json=json_data)
    updated_post=schemas.Post(**res.json())
    assert updated_post.title==json_data['title']
    assert updated_post.content==json_data['content']    
    assert res.status_code==200


def test_update_other_user_posts(authorized_client,test_posts,test_users,test_users2):
    json_data={
        "title": 'a nice salad for the dinner',
        "content": 'cucumbar',
        "id":test_posts[3].id
        
    }
    res=authorized_client.put(f'/posts/{test_posts[3].id}',json=json_data)   
    assert res.status_code==403



def test_unauthorized_update_posts(client,test_posts):
    json_data={
        "title": 'a nice salad for the dinner',
        "content": 'cucumbar',
        "id":test_posts[2].id
        
    }
    res=client.put(f'/posts/{test_posts[3].id}',json=json_data)   
    assert res.status_code==401



def test_update_non_exist_posts(authorized_client,test_posts):
    json_data={
        "title": 'a nice salad for the dinner',
        "content": 'cucumbar',
        "id":test_posts[2].id
        
    }
    res=authorized_client.put(f'/posts/55',json=json_data)   
    assert res.status_code==404








def test_all_posts(authorized_client,test_posts):
    res=authorized_client.get('/posts')
    def schema_validation(post):
        return schemas.PostOut(**post)
    
    posts_map=map(schema_validation,res.json())
    post_lists=list(posts_map)
    # print(post_lists)
    assert len(res.json())==len(test_posts)






def test_unauthorized_all_posts(client,test_posts):
    res=client.get('/posts')
    assert res.status_code==401





def test_unauthorized_post_by_id(client,test_posts):
    res=client.get(f'/posts/{test_posts[0].id}')
    assert res.status_code==401



def test_post_not_exist_by_id(authorized_client,test_posts):
    res=authorized_client.get(f'/posts/5454')
    assert res.status_code==404




def test_authorized_post_by_id(authorized_client,test_posts):
    res=authorized_client.get(f'/posts/{test_posts[0].id}')

    check_schema=schemas.PostOut(**res.json())
    assert check_schema.post.title==test_posts[0].title
    assert res.status_code==200

















































