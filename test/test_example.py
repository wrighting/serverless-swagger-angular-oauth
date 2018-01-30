import swagger_client
from swagger_client.rest import ApiException
from test_base import TestBase

import copy
import uuid

class TestExample(TestBase):


    """
    """
    def test_create(self):

        api_instance = swagger_client.ExampleApi(self._api_client)

        try:

            loc = swagger_client.Example(example_id=None, example_value='An Example create')
            created = api_instance.create_example(loc)
            fetched = api_instance.download_example(created.example_id)
            self.assertEqual(created, fetched, "create response != download response")
            api_instance.delete_example(created.example_id)

        except ApiException as error:
            self.fail("test_create: Exception when calling ExampleApi->create_example: %s\n" % error)

    """
    """
    def test_delete(self):

        api_instance = swagger_client.ExampleApi(self._api_client)

        try:

            loc = swagger_client.Example(example_id=None, example_value='An Example delete')
            created = api_instance.create_example(loc)
            api_instance.delete_example(created.example_id)
            #Check it's gone
            with self.assertRaises(Exception) as context:
                fetched = api_instance.download_example(created.example_id)
            self.assertEqual(context.exception.status, 404)

        except ApiException as error:
            self.fail("test_delete: Exception when calling ExampleApi->delete_location: %s\n" % error)

    """
    """
    def test_update(self):

        api_instance = swagger_client.ExampleApi(self._api_client)

        try:

            loc = swagger_client.Example(example_id=None, example_value='An Example created for update')
            created = api_instance.create_example(loc)
            created.example_value = 'Updated example'
            api_instance.update_example(created.example_id, created)
            fetched = api_instance.download_example(created.example_id)
            self.assertEqual(created, fetched, "create response != download response")
            api_instance.delete_example(created.example_id)

        except ApiException as error:
            self.fail("test_create: Exception when calling ExampleApi->update_example: %s\n" % error)

