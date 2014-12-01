import unittest

from zahpeeapi.api_client import ZahpeeAPI


BASE_URL = "http://test"
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
        self.api = ZahpeeAPI(base_api_url="")

    def test_simple_request(self):
        """ Test a simple request in api without custom parameter
        """
        #
        # response = FileFake("This is a bunch\nOf Text!")
        # print("test/v1.0/users/list?{'limit': 10}")
        # when(request).urlopen("test/v1.0/users/list?{'limit': 10}").thenReturn(response)
        # when(response).read().thenReturn(b'{"users":[]}')
        # result = self.api.list_users()
        #
        # print(result)
        # assert result == b"{'users': []}"

    def test_request_type(self):
        """ Test a request in api changing parameter type
        """

        # response = FileFake("This is a bunch\nOf Text!")
        # print("test/v1.0/users/list?{'type': 'test', 'limit': 10}")
        # when(request).urlopen("test/v1.0/users/list?{'type': 'test', 'limit': 10}").thenReturn(response)
        # when(response).read().thenReturn(b'{"users":[]}')
        # result = self.api.list_users(user_type='test')

        # print(result)
        # assert result == b"{'users': []}"
