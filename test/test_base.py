from __future__ import print_function
import unittest
import swagger_client
import json
import requests
import os

import boto.cloudformation

class TestBase(unittest.TestCase):


    _auth_token = None
    _configuration = None
    _api_client = None
    _region = None

    """
    """
    def setUp(self):
        with open('./config_dev.json') as json_file:
            args = json.load(json_file)
            r = requests.get(os.getenv('TOKEN_URL'), args, headers = { 'service': 'http://localhost/' })
            at = r.text.split('=')
            token = at[1].split('&')[0]
            self._auth_token = token
            self._region = args['region']

        self._configuration = swagger_client.Configuration()
        self._configuration.access_token = self._auth_token

        conn = boto.cloudformation.connect_to_region(self._region)  # or your favorite region
        stacks = conn.describe_stacks('wrighting-example-service-dev')
        if len(stacks) == 1:
            stack = stacks[0]
            for output in stack.outputs:
                if output.key == 'ServiceEndpoint':
                    self._configuration.host=output.value + '/example-service/v1'

#                print('%s=%s (%s)' % (output.key, output.value, output.description))
        else:
                # Raise an exception or something because your stack isn't there
                pass

        self._api_client = swagger_client.ApiClient(self._configuration)

    """
    """
    def tearDown(self):
        pass


