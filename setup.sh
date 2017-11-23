curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs

sudo npm install -g serverless
sudo npm install -g @angular/cli

if [ ! -d example-service ]
then
    serverless create --template aws-python3 --path example-service
    cd example-service
    npm install --save serverless-python-requirements

    ng new example-app

    mkdir swagger
fi
