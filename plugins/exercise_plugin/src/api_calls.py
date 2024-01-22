import requests
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
import json

disable_warnings(InsecureRequestWarning)


class APIBase:
    """
    Base class for all API calls
    """

    def __init__(self, host, username, password):
        self.base_url = "https://" + host
        self.auth = (username, password)

    def get_route(self, route):
        return self.base_url + "/" + route

    def _run(self, route):
        try:
            response1 = requests.get(url=self.get_route(route), verify=False, auth=self.auth)
            if response1.status_code == 200:
                pretty_json = json.dumps(response1.json(), indent=4)
                return pretty_json
            else:
                raise Exception("request failed with status code: " + str(response1.status_code))
        except Exception as e:
            return e


class API(APIBase):
    """
    Class for invoking a single API call
    """

    def __init__(self, host, username, password, route):
        super().__init__(host, username, password)
        self.route = route

    def run(self):
        return super()._run(self.route)
