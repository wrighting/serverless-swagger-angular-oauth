test -f swagger-codegen-cli.jar || wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar -O swagger-codegen-cli.jar
#Not working yet
#test -f swagger-codegen-cli.jar || wget https://oss.sonatype.org/content/repositories/snapshots/io/swagger/swagger-codegen-cli/3.0.0/swagger-codegen-cli-3.0.0.jar -O swagger-codegen-cli.jar
if [ "$1" = "server" -o "$1" = "" ]
then
    #.swagger-codegen-ignore must be present
    rm -rf python-flask/*
    java -jar swagger-codegen-cli.jar generate -i example.yml -l python-flask -o python-flask
fi
if [ "$1" = "client" -o "$1" = "" ]
then
    #.swagger-codegen-ignore must be present
    rm -rf ../example-app/src/app/typescript-angular-client/*
    java -jar swagger-codegen-cli.jar generate -i example.yml -l typescript-angular -o ../example-app/src/app/typescript-angular-client
    #.swagger-codegen-ignore must be present
    rm -rf python_client/*
    java -jar swagger-codegen-cli.jar generate -i example.yml -l python -o python_client
fi
