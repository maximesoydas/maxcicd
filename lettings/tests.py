from distutils.log import error
from http.client import INTERNAL_SERVER_ERROR
from sqlite3 import InternalError
from xmlrpc.client import INTERNAL_ERROR
import pytest
from .models import Letting, Address
from django.contrib.auth.models import User
from django import urls
from django.core.exceptions import ObjectDoesNotExist
import lettings
'''
Test Models,
with the help of fixtures in the conftest
'''

# Test Address

def test_check_address(address_1):
    assert Address.objects.count() == 1


def test_check_address_city(address_1):
    assert address_1.city == 'Darnfield'


# Test Letting

def test_check_lettings(letting_1):
    assert Letting.objects.count() == 1


def test_check_lettings_address(letting_1):
    assert Address.objects.count() == 1 and Letting.objects.count() == 1


'''
Test Views,
with the corresponding URI
'''

# Test Letting List Page

# without letting entry


@pytest.mark.django_db
@pytest.mark.parametrize('param', [('lettings:index')])
def test_render_lettings_view_no_data(client, param):
    temp_url = urls.reverse(param)
    response = client.get(temp_url)
    assert response.status_code == 200 and "No lettings" in str(response.content)

# with letting entry


def test_render_lettings_view_data(db, client, letting_1):
    temp_url = urls.reverse('lettings:index')
    response = client.get(temp_url)
    assert response.status_code == 200 and "No lettings" not in str(response.content)


# Test Letting Detail Page

# without letting entry
def test_render_letting_detail_view_no_data(db, client):
    letting_id = 1
    try:
        temp_url = urls.reverse('lettings:letting', kwargs={'letting_id': letting_id})
        response = client.get(temp_url)
    except:
        assert Letting.objects.filter(id=letting_id).first() is None

# with letting entry


def test_render_letting_detail_view_data(db, client, letting_1):
    temp_url = urls.reverse('lettings:letting', kwargs={'letting_id': 1})
    response = client.get(temp_url)
    assert response.status_code == 200 and "Darnfield" in str(response.content)
