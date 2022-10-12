import pytest
# from django models import Letting, Address
from django.apps import apps
from django.contrib.auth.models import User

'''
PYTEST

A pattern for writing tests:
- Arrange (do you need to connect to the db? an api ? a webapp? ... )
- Act (call a function, a method -> fetch a response http/json...)
- Assert (verify that the outcome corresponds to our wishes)

MARKS:

A mark is a way of adding metadata to a test.

Example:
    - @pytest.mark.skip
    - @pytest.mark.xfail

FIXTURES:

Fixtures are functions.
They run before or after each test function
to which the function is applied.
They are used to feed data
to the tests such db connections,
urls to test and input data.

Example:
    - @pytest.fixture

You can call fixtures at different levels/scopes:
    - function: Run once per test
    - class:    Run once per class of tests
    - module:   Run once per module
    - session:  Run once per session
'''


@pytest.fixture()
def user_1(db):
    user = User.objects.create_user("test-user")
    return user


@pytest.fixture()
def address_1(db):
    address_model = apps.get_model('lettings', 'address')
    address = address_model.objects.create(
        number='595',
        street='Little Street',
        city='Darnfield',
        state='Nevada',
        zip_code='89108',
        country_iso_code='US-NV',
    )
    return address


@pytest.fixture()
def letting_1(db, address_1):
    letting_model = apps.get_model('lettings', 'letting')
    letting = letting_model.objects.create(
        title="Little Street's Mansion",
        address=address_1
    )
    return letting


@pytest.fixture()
def profile_1(db, user_1):
    profile_model = apps.get_model('profiles', 'profile')
    profile = profile_model.objects.create(
        user=user_1,
        favorite_city='Pokhara'
    )
    return profile
