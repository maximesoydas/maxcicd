from django import urls
# Create your tests here.

'''
Test Models,
with the help of fixtures in the conftest
'''

# Test User


def test_set_check_password(user_1):
    user_1.set_password("new-password")
    assert user_1.check_password("new-password") is True


def test_check_username(user_1):
    assert user_1.username == 'test-user'


'''
Test Views
with the corresponding URI
'''

# Test HomePage/Index page

# with Profile entry


def test_render_profiles_view_data(db, client):
    temp_url = urls.reverse('index')
    response = client.get(temp_url)
    assert response.status_code == 200 and "Welcome to Holiday Homes" in str(response.content)
