import logging
from urllib import request, parse
import json
from urllib import error

logger = logging.getLogger(__name__)

# Users Endpoint
ENDPOINT_USERS_LIST = "users/list/"
ENDPOINT_USERS = "users/"
ENDPOINT_MONITORINGS = "monitorings/"
ENDPOINT_POSTS = "posts/"
ENDPOINT_HASHTAGS = "hashtags/"
ENDPOINT_HASHTAG = "hashtag"

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
    def _make_post_request(request_uri, params, rawPost=False):
        """ Makes, parses and decodes a POST request to the app or the API

        :param request_uri: The request URI
        :param params: The request parameters in dic format
        :return The decoded response
        """
        
        if rawPost:
            data = json.dumps(params)
        else:
            data = parse.urlencode(params)

        print(request_uri)

        if rawPost:
            requests = request.Request(request_uri, data.encode("utf8"),
                    {'Content-Type': 'application/json'})
        else:
            requests = request.Request(request_uri, data.encode("utf8"))
        
        response = request.urlopen(requests)
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

        print(request_uri)

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

        return self._make_get_request(self.base_app_url + "/oauth/token", params)

    def is_access_token_valid(self, access_token):
        """
        :param access_token: The user access token
        :return True or False
        """

        params = {
            "access_token": access_token,
        }
        try:
            response = self._make_get_request(self.base_api_url + "/" + self.version + "/auth/test", params)
            if response['message'] == 'You are correctly authenticated.':
                return True
            else:
                return False
        except error.HTTPError as e:
            return False

    def refresh(self, client_id, client_secret, refresh_token):
        """ Refreshes the user access token, returning a new and valid access token if it goes OK, or throwing an error

        :param client_id: Client id of Zahpee API
        :param client_secret: Client secret of Zahpee API
        :param refresh_token: The user refresh_token

        :return The generated access token
        """

        params = {
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": 'refresh_token',
            "refresh_token": refresh_token,
            }

        try:
            response = self._make_get_request(self.base_app_url + "/oauth/token", params)
        except Exception as e:
            logging.error('Error trying to access Zahpee Api ' + str(e))
            response = ''

        return response

    def list_users(self, ids):
        """ List all users wanted

        :param ids: List of ids

        :return: List of users
        """

        user_list = ''
        for user_id in ids:
            if user_list == '':
                user_list = str(user_id)
            else:
                user_list = user_list + "," + str(user_id)

        request_uri = self.base_api_url + "/" + self.version + "/" + ENDPOINT_USERS_LIST + user_list

        params = {
            "access_token": self.access_token
        }

        return self._make_get_request(request_uri, params)

    def create_user(self, email, name, password, gmt, user_type):
        """ Create a Zahpee Events user

        :param email: User email
        :param name: User name
        :param password: User password
        :param gmt: User gmt
        :param user_type: User Type : ADMIN OR NO_INTERFACE_ACCESS
        :return: The generated subscription token
        """

        request_uri = self.base_api_url + "/" + self.version + "/" + ENDPOINT_USERS

        if gmt is None:
            gmt = -3

        params = {
            'name': name,
            'email': email,
            'password': password,
            'gmt': gmt,
            'type': user_type,
            'access_token': self.access_token
        }

        return self._make_post_request(request_uri, params)

    def create_post(self, monitoring_id, author_name, author_login,
            author_avatar, content, source, source_id, image,
            upload_date):
        """ Create Zahpee post in given monitoring

        :param monitoring_id Monitoring that should receive the post
        :param author_name Name of the author that published this post
        :param author_login Login of the author that published this post
        :param author_avatar Avatar of the author that published this post
        :param author_url Url of the author's profile page in a social network (e.g. Twitter, Facebook. Google+)
        :param content Post content
        :param source Source of this post (e.g. Twitter, Facebook)
        :param source_id Unique identifier used by 'Source'
        :param image Base64 string of image attached to this post
        :param upload_date Date in which post was published
        :return
        """

        request_uri = self.base_api_url + "/" + self.version + "/" + \
                      ENDPOINT_MONITORINGS + str(monitoring_id) + "/" + ENDPOINT_POSTS + \
                      "?access_token=" + self.access_token

        params = {
            'uploadDate': upload_date,
            'profile': {
                'name': author_name,
                'login': author_login,
                'avatar': author_avatar,
                'url': author_url,
            },
            'content': content,
            'source': source,
            'sourceID': source_id,
            'base64Image': image,
            'uploadDate': upload_date,
        }

        return self._make_post_request(request_uri, params, True)

    def get_posts(self, monitoring_id, limit=10, sentiment='all', noise='notgarbage', themeId='all', source='all',
                  sort='updesc', beginDate='null', endDate='null', pageToken='null', page=0):

        """ Get posts from a specific monitoring.

        :param monitoring_id: The id of the monitoring
        :param limit: The number of posts to be returned
        :return: The posts retrieved
        """

        request_uri = self.base_api_url + "/" + self.version + "/" + \
                      ENDPOINT_MONITORINGS + str(monitoring_id) + "/" + ENDPOINT_POSTS

        params = {
            'limit': limit,
            'sentiment': sentiment,
            'noise': noise,
            'themeId': themeId,
            'channel': source,
            'sort': sort,
            'beginDate': beginDate,
            'endDate': endDate,
            'pageToken': pageToken,
            'page': page,
            'access_token': self.access_token
        }

        return self._make_get_request(request_uri, params)

    def get_hashtags(self, monitoring_id):

        """ Get hashtags associated with a specific monitoring.

        :param monitoring_id: The id of the monitoring
        :return: The list of hashtags retrieved
        """

        request_uri = self.base_api_url + "/" + self.version + "/" + \
                      ENDPOINT_MONITORINGS + str(monitoring_id) + "/" + ENDPOINT_HASHTAGS

        params = {
            'access_token': self.access_token
        }

        return self._make_get_request(request_uri, params)

    def get_monitorings(self):

        """ Get a list of all monitorings associated with a specific user.

        :return: The list of hashtags retrieved
        """

        request_uri = self.base_api_url + "/" + self.version + "/" + ENDPOINT_MONITORINGS

        params = {
            'access_token': self.access_token
        }

        return self._make_get_request(request_uri, params)

    def get_monitoring(self, monitoring_id):

        """ Get the user monitoring with the given id.

        :param monitoring_id: The id of the monitoring
        :return: The list of hashtags retrieved
        """

        request_uri = self.base_api_url + "/" + self.version + "/" + ENDPOINT_MONITORINGS + str(monitoring_id)

        params = {
            'access_token': self.access_token
        }

        return self._make_get_request(request_uri, params)

    def get_monitoring_by_hashtag(self, hashtag):

        """ Get the monitoring with the given hashtag.

        :param hashtag: The hashtag
        :return: The monitoring associated with the hashtag given
        """

        request_uri = self.base_api_url + "/" + self.version + "/" + ENDPOINT_MONITORINGS + ENDPOINT_HASHTAG

        params = {
            'hashtag': str(hashtag),
            'access_token': self.access_token
        }

        try:
            return self._make_get_request(request_uri, params)
        except error.HTTPError as e:
            return None
