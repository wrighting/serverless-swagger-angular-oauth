import connexion
import six

from swagger_server.models.example import Example  # noqa: E501
from swagger_server import util

from example_server.controllers.example_controller import ExampleController

example_controller = ExampleController()


def create_example(body, user=None, token_info=None):  # noqa: E501
    """Add a new example

     # noqa: E501

    :param body: Example object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Example.from_dict(connexion.request.get_json())  # noqa: E501

    return example_controller.create_example(body, user, example_controller.token_info(token_info))



def delete_example(exampleId, user=None, token_info=None):  # noqa: E501
    """Deletes a example

     # noqa: E501

    :param exampleId: Example id to delete
    :type exampleId: int

    :rtype: None
    """

    return example_controller.delete_example(exampleId, user, example_controller.token_info(token_info))


def download_example(exampleId, user=None, token_info=None):  # noqa: E501
    """Find example by ID

    Returns a single example # noqa: E501

    :param exampleId: ID of example to return
    :type exampleId: int

    :rtype: Example
    """

    return example_controller.download_example(exampleId, user, example_controller.token_info(token_info))


def download_examples(user=None, token_info=None):  # noqa: E501
    """Find example by ID

    Returns a single example # noqa: E501


    :rtype: Example
    """

    return example_controller.download_examples(user, example_controller.token_info(token_info))


def update_example(body, user=None, token_info=None):  # noqa: E501
    """Update an existing example

     # noqa: E501

    :param body: Example object that needs to be added
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Example.from_dict(connexion.request.get_json())  # noqa: E501

    return example_controller.update_example(body, user, example_controller.token_info(token_info))
