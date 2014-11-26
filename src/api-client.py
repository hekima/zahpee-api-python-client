import urllib.request
import json

# Users Endpoint
ENDPOINT_LIST_USERS = "users/list"


class ZahpeeAPI:
    """
    This class was created with the goal to be a separated module.

    TODO: In the future it will be in another repository to be used
    https://github.com/zahpee/zahpee-api-python-client.git
    """

    def __init__(self, base_url="https://api.zahpee.com", user_id=None, version="v1.0",
                 token='c5b3d37a-2874-4975-a1fc-d55531fe9d7e'):
        """

        :rtype : object
        :param base_url: Api url
        :param user_id: Id of user that is request
        :param version: API version
        """
        self.base_url = base_url
        self.user_id = user_id
        self.version = version
        self.access_token = token

    def get_access_token(self):
        return 'access_token=' + self.access_token

    def list_users(self, limit=10, user_type=None):
        """
        List all user with filter

        :param limit: Maximum number of users
        :param user_type: Type of users
        :return: List of user
        """

        params = {'limit': limit}

        if user_type:
            params['type'] = user_type

        params = urllib.urlencode(params)
        response = urllib.request.urlopen(self.base_url + "/" + self.version + "/" + ENDPOINT_LIST_USERS + '?%s' % params)

        return json.loads(response.read().decode("utf8"))
