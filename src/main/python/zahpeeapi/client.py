from urllib import request, parse
import json

# Users Endpoint
ENDPOINT_USERS_LIST = "users/list"
ENDPOINT_USERS = "users/"


class ZahpeeAPI:
    """ This class was created with the goal to be a separated module.

    The documentation for this API can be found at this link: https://api.zahpee.com/doc/index.html
    """

    def __init__(self,
                 base_api_url="https://api.zahpee.com",
                 base_app_url="https://app.zahpee.com",
                 user_id=None,
                 version="v1.0",
                 token=""):

        """ Constructor for api

        :param base_api_url: Api url
        :param base_app_url: App url
        :param user_id: Id of user that is request
        :param version: API version
        :param token: Access Token from api
        """
        self.base_api_url = base_api_url
        self.base_app_url = base_app_url
        self.user_id = user_id
        self.version = version
        self.access_token = token

    @staticmethod
    def _make_post_request(request_uri, params):
        """ Makes, parses and decodes a POST request to the app or the API

        :param request_uri: The request URI
        :param params: The request parameters in dic format
        :return The decoded response
        """
        data = parse.urlencode(params)

        requests = request.Request(request_uri, data.encode("utf8"))
        response = requests.urlopen(request)

        return json.loads(response.read().decode("utf8"))

    @staticmethod
    def _make_get_request(request_uri, params):
        """ Makes, parses and decodes a GET request to the app or the API

        :param request_uri: The request URI
        :param params: The request parameters in dic format
        :return The decoded response
        """

        if params and params != {}:
            request_uri = request_uri + '?' + parse.urlencode(params)

        return json.loads(request.urlopen(request_uri).read().decode("utf8"))

    def login(self, client_id, client_secret, grant_type, user, password):
        """ Logs the user in, returning an access token if the login goes OK, or throwing an error otherwise

        :param client_id: Client id of Zahpee API
        :param client_secret: Client secret of Zahpee API
        :param grant_type: Type of access of access, possible values (password)
        :param password: The user password

        :return The generated access token
        """

        params = {
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": grant_type,
            "password": password,
            "username": user,
        }

        return self._make_get_request(self.base_app_url + "/oauth/token/", params)

    def list_users(self, ids):
        """ List all users wanted

        :param ids: List of ids

        :return: List of users
        """

        request_uri = self.base_api_url + "/" + self.version + "/" + ENDPOINT_USERS_LIST

        params = {
            "ids": ids,
            "access_token": self.access_token
        }

        return self._make_get_request(request_uri, params)


    def create_user(self, email, name):
        """ Create a Zahpee Events user

        :param email: User email
        :param name: User name
        :return: The generated subscription token
        """

        request_uri = self.base_api_url + "/" + self.version + "/" + ENDPOINT_USERS

        params = {
            'name': name,
            'email': email,
            'access_token': self.access_token
        }

        return self._make_post_request(request_uri, params)
