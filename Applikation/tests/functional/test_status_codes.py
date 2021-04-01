import pytest
from flask import g
from flask import session

def test_home(client):
    assert client.get("/").status_code == 200
    assert client.get("/home").status_code == 200

def test_users(client):
    assert client.get("/users/login").status_code == 308
    assert client.get("/users/logout").status_code == 302
    assert client.get("/users/register").status_code == 308
    assert client.get("/users/view_users").status_code == 308
  
  
def test_posts(client):
    assert client.get("/posts/new_post").status_code == 308
    assert client.get("/posts/entries").status_code == 308

def test_sheets(client):
    assert client.get("/sheets/new_sheet").status_code == 308
    assert client.get("/sheets/new_sheet2").status_code == 308
    assert client.get("/sheets/new_sheet3").status_code == 308
    assert client.get("/sheets/view_sheet").status_code == 308
    assert client.get("/sheets/view_sheet2").status_code == 308

def test_topics(client):
    assert client.get("/topics/new_topic").status_code == 308
