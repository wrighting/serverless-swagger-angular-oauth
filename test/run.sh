#!/bin/bash
export TOKEN_URL=https://myssohost/sso/oauth2.0/accessToken
export PYTHONPATH=$(pwd)/../swagger/python_client
if [ ! -d client-env ]
then
    virtualenv client-env -p /usr/bin/python3
    source client-env/bin/activate
    pip3 install -r ../swagger/python_client/requirements.txt
    pip3 install -r requirements.txt
fi
source client-env/bin/activate
if [ "$1" = "one" ]
then
    python3 -m unittest test_example.TestExample.test_create

else
    python3 all_tests.py
fi
