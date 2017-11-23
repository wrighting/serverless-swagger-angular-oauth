
In the example-service/config directory you will need to ```cp config.template.json
config.dev.json``` and edit config.dev.json

Add your database connection parameters and OAuth profile url

In example-service run:

sls deploy -v

You will now be able to add the db_host value in your config.dev.json as it will have been created
and you can get the hostname from RDS

If you have trouble creating your stack then it's worth checking the [Cloud Formation Console](https://eu-west-2.console.aws.amazon.com/cloudformation/home)

e.g. I've run into the limit of 5 VPC per region

If you want to access the database directly it's best to create a bastion host within the
VPC - if you want an accessible host - key gotcha is the DependsOn VPCGatewayAttachment

There is some code in the base_controller.py to initialize the database
