import pytest

from django.urls import reverse
from django.test import Client
from .models import Letting, Address
from pytest_django.asserts import assertTemplateUsed


# TEST WITH THE RIGHT CLIENT


@pytest.mark.django_db
def test_book_infos_view():
    client = Client()
    address = Address.objects.create(
        number='595',
        street='Little Street',
        city='Darnfield',
        state='Nevada',
        zip_code='89108',
        country_iso_code='US-NV',
    )

    Letting.objects.create(title="Little Street", address=address)
    path = reverse('infos', kwargs={'pk': 1})
    response = client.get(path)
    content = response.content.decode()
    expected_content = ""

    assert content == expected_content
    assert response.status_code == 200
    assertTemplateUsed(response, "book_infos.html")
