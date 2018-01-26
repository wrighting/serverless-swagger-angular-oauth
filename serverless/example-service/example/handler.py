import json

import os, sys, inspect

currentframe = os.path.split(inspect.getfile(inspect.currentframe()))[0]
paths = ['.', '../common', '../swagger/python-flask']

for include_path in paths:
    cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(currentframe,include_path)))
    if cmd_subfolder not in sys.path:
         sys.path.insert(0, cmd_subfolder)


import logging

from example_server.controllers.example_controller import ExampleController

from util.response_util import create_response

example_controller = ExampleController()

def create_example(event, context):

    user = event['requestContext']['authorizer']['principalId']
    auth = example_controller.authorizer(event['requestContext']['authorizer'])

    input_body = json.loads(event["body"])

    example = input_body

    value, retcode = example_controller.create_example(example, user, auth)


    return create_response(event, retcode, value)

def download_example(event, context):

    user = event['requestContext']['authorizer']['principalId']
    auth = example_controller.authorizer(event['requestContext']['authorizer'])

    if 'pathParameters' in event:
        example_id = event["pathParameters"]["example_id"]

    value, retcode = example_controller.download_example(example_id, user, auth)

    return create_response(event, retcode, value)

def download_examples(event, context):

    user = event['requestContext']['authorizer']['principalId']
    auth = example_controller.authorizer(event['requestContext']['authorizer'])

    value, retcode = example_controller.download_examples(user, auth)

    value = {
        'count': 1,
        'items': [ 
            { 
                'example_id': 1,
                'example_value': 'fred'
            }
        ]
    }
    return create_response(event, retcode, value)

def update_example(event, context):

    user = event['requestContext']['authorizer']['principalId']
    auth = example_controller.authorizer(event['requestContext']['authorizer'])

    if 'pathParameters' in event:
        example_id = event["pathParameters"]["example_id"]

    input_body = json.loads(event["body"])

    example = input_body

    value, retcode = example_controller.update_example(example_id, example, user, auth)

    return create_response(event, retcode, value)
