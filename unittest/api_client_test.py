import unittest
import urllib
import api_client
from mockito import when, mock

BASE_URL = "test"
VERSION = "v1.0"


class FileFake:
    def __init__(self, my_text):
        self.my_text = my_text

    def read(self):
        return ''

    def readlines(self):
        return self.my_text.splitlines()


class ZahpeeApiTest(unittest.TestCase):
    def setUp(self):
        self.api = api_client.ZahpeeAPI(base_url=BASE_URL, token="")

    def test_get_access_token(self):
        result = self.api.get_access_token()

        assert result == 'access_token='

    def test_simple_request(self):
        print("Test simple request")

        response = FileFake("This is a bunch\nOf Text!")
        print(BASE_URL + "/" + VERSION + "/users/list?limit=10&access_token=")
        when(urllib.request).urlopen(
            BASE_URL + "/" + VERSION + "/users/list?limit=10&access_token=").thenReturn(response)
        when(response).read().thenReturn(b'{"users":[]}')
        result = self.api.list_users()

        print("result" + str(result))
        # assert '{\'users\': []}' == str(result)

    def test_request_type(self):
        print("Test request with type")

        response = mock()
        print(BASE_URL + "/" + VERSION + "/users/list?limit=10&type=test&access_token=")
        when(urllib.request).urlopen(
            BASE_URL + "/" + VERSION + "/users/list?limit=10&type=test&access_token=").thenReturn(response)
        when(response).read().thenReturn(b'{"users":[]}')
        result = self.api.list_users(user_type='test')

        print("result" + str(result))
        # assert '{\'users\': []}' == str(result)
