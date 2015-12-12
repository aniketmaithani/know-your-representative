# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse

# Pytest
import pytest
from .. factories import MPFactory

pytestmark = pytest.mark.django_db


def test_api_endpoints(client):
    url = '/api/complaints/'
    content = client.get(url)
    assert content.status_code == 405  # GET METHOD NOT ALLOWED ON THE ENDPOINT
    data = {
        "name_of_the_complainee": "test_name",
        "phone_number_of_the_complainee": "9999000909",
        "geolocation": "14 N, 32 E",
        "description_of_the_problem": "test description",
        "name_of_the_mp_for_problem_redressal": "ME"
    }
    content_post = client.post(url, data)
    assert content_post.status_code == 201  # Success

    data = {
        "name_of_the_complainee": "test_name",
        "phone_number_of_the_complainee": "9999000909",
        "geolocation": "14 N, 32 E",
        "description_of_the_problem": "",
        "name_of_the_mp_for_problem_redressal": "ME"
    }
    content_post = client.post(url, data)
    assert content_post.status_code == 400  # Bad Request [FIELD REQUIRED]


def test_get_method(client):
    test_mp = MPFactory.create()  # Creating a Test MP

    url = reverse('member-search',
                  kwargs={'name_of_the_mp': test_mp.name_of_the_mp})
    data = {}
    response = client.post(url, data)
    assert response.status_code == 405  # POST Method Not Allowed
    content_get = client.get(url)
    assert content_get.status_code == 200
    # Testing whether the value exists or not
    assert content_get.data['results'][0][
        'name_of_the_mp'] == test_mp.name_of_the_mp
