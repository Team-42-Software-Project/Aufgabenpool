from flaskr.users.models import User

def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, and role fields are defined correctly
    """
    user = User(username="XY", email="me@me.com", password="abc")
    assert user.email == 'me@me.com'
    assert user.password == 'abc'
    assert user.username == 'XY'
    assert user.id == None
    assert user.image_file == None
    assert user.posts == []
    assert user.topics == []
    assert user.sheets == []
