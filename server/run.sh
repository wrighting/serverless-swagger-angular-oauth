VIRTUAL_ENV_HOME=.
export CREATE_SCHEMA_IF_MISSING=true
if [ "$1" = "build" ]
then
    virtualenv server-env -p /usr/bin/python3
    (cd ../swagger;./generate.sh server)
fi
if [ -f ${VIRTUAL_ENV_HOME}/server-env/bin/activate ]
then
    source ${VIRTUAL_ENV_HOME}/server-env/bin/activate
    if [ "$1" = "build" ]
    then
        pip3 install -r requirements.txt
        pip3 install -r ../swagger/python-flask/requirements.txt
    fi
    rm -rf local_server
    cp -pr ../swagger/python-flask local_server
    cp -pr overlay/* local_server
    mkdir local_server/database
    cp ../database/schema.psql local_server/database
    cd local_server
    export PYTHONPATH=$(pwd):$(pwd)/../../common:${PYTHONPATH}
    echo "http://localhost:8080/v1/ui/"
    python3 -m swagger_server
fi
