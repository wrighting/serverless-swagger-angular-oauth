from io import BytesIO
import base64
import gzip
import json
import ujson

import logging

def gzip_b64encode(data):
    compressed = BytesIO()
    with gzip.GzipFile(fileobj=compressed, mode='w') as f:
        json_response = ujson.dumps(data, ensure_ascii=False)
        f.write(json_response.encode('utf-8'))
    return base64.b64encode(compressed.getvalue()).decode('ascii')

def create_response(event, retcode, value):

    response_dict = value
    #response_dict = value.to_dict()
    gzip = False
    if 'Accept-Encoding' in event['headers']:
        if 'gzip' in event['headers']['Accept-Encoding']:
            gzip = True

    if gzip:
        return {
            "statusCode": retcode,
            "isBase64Encoded": True,
            "headers": {
                "Access-Control-Allow-Origin" : "*",
                'Content-Type': 'application/json',
                'Content-Encoding': 'gzip'
            },
            "body": gzip_b64encode(response_dict)
        }
    else:
        return {
            "statusCode": retcode,
            "headers": {
                "Access-Control-Allow-Origin" : "*",
                'Content-Type': 'application/json'
            },
            "body": ujson.dumps(response_dict, ensure_ascii=False)
        }

