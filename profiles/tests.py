from .models import Profile
import pytest
from distutils.log import error
from django.contrib.auth.models import User
from django import urls
# Create your tests here.

'''
Test Models,
with the help of fixtures in the conftest
'''

# Test Profile Model

def test_check_profiles(profile_1):
    assert Profile.objects.count() == 1
    
def test_check_profiles_city(profile_1):
    assert profile_1.favorite_city == "Pokhara"
    

'''
Test Views
with the corresponding URI
'''

# Test Profile List Page

# without Profile entry
@pytest.mark.django_db
@pytest.mark.parametrize('param', [('profiles:index')])
def test_render_profiles_view_no_data(client, param):
    temp_url = urls.reverse(param)
    response = client.get(temp_url)
    assert response.status_code == 200 and "No profiles" in str(response.content)

# with Profile entry
def test_render_profiles_view_data(db, client, profile_1):
    temp_url = urls.reverse('profiles:index')
    response = client.get(temp_url)
    assert response.status_code == 200 and "No profiles" not in str(response.content)


# Test Profile Detail Page

# without Profile entry
def test_render_profile_detail_view_no_data(db, client):
    user_id = 1
    try:
        temp_url = urls.reverse('profiles:profile', kwargs={'user':user_id})
        response = client.get(temp_url)
    except:
        assert Profile.objects.filter(user=user_id).first() is None

    
# with Profile entry 
def test_render_profile_detail_view_data(db, client, profile_1):
    username = profile_1.user.username
    temp_url = urls.reverse('profiles:profile', kwargs={'username':username})
    response = client.get(temp_url)
    assert response.status_code == 200 and "Pokhara" in str(response.content)
