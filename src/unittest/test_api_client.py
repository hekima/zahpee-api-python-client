import unittest

from zahpeeapi.client import ZahpeeAPI
from mockito import when
from urllib import request,parse


BASE_URL = "http://test"
VERSION = "v1.0"


class RequestMocked:
    def __init__(self, my_text):
        self.my_text = my_text

    @staticmethod
    def read():
        return ''

    def readlines(self):
        return self.my_text.splitlines()


class ZahpeeApiTest(unittest.TestCase):

    def setUp(self):
        self.api = ZahpeeAPI(base_api_url=BASE_URL)

    def test_no_user_id(self):
        """ Test request without user id
        """
        response = RequestMocked("This is a bunch\nOf Text!")

        when(request).urlopen(BASE_URL+"/v1.0/users/list/?access_token=").thenReturn(response)
        when(response).read().thenReturn(b'{"users":[]}')
        result = self.api.list_users(ids=[])

        assert result == {'users': []}

    def test_one_user_id(self):
        """ Test request with only one user id
        """

        response = RequestMocked("This is a bunch\nOf Text!")
        when(request).urlopen(BASE_URL+"/v1.0/users/list/0?access_token=").thenReturn(response)
        when(response).read().thenReturn(b'{"users":[]}')
        result = self.api.list_users(ids=[0])

        assert result == {'users': []}

    def test_many_user_ids(self):
        """ Test request with many user ids
        """

        response = RequestMocked("This is a bunch\nOf Text!")
        when(request).urlopen(BASE_URL+"/v1.0/users/list/0,1,2,3?access_token=").thenReturn(response)
        when(response).read().thenReturn(b'{"users":[]}')
        result = self.api.list_users(ids=[0, 1, 2, 3])

        assert result == {'users': []}

    def test_create_user(self):
        """ Test simple creation of an user
        """

        email = "contact@zahpee.com"
        name = "Zahpee"
        password = "f4k3P4ss"

        params = {
            'name': name,
            'email': email,
            'password': password,
            'gmt': '-3',
            'invitationType': 'ZAHPEE_EVENTS',
            'access_token': ''
        }

        requests = RequestMocked("This is a bunch\nOf Text!")
        when(request).Request(BASE_URL+"/v1.0/users/", parse.urlencode(params).encode("utf8")).thenReturn(requests)

        response = RequestMocked("This is a bunch\nOf Text!")
        when(request).urlopen(requests).thenReturn(response)
        when(response).read().thenReturn(b'{"name":"Zahpee"}')
        result = self.api.create_user(email=email, name=name, password=password, gmt='-3', user_type='ZAHPEE_EVENTS')

        assert result == {'name': 'Zahpee'}