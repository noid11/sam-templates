# lambda-vpc

# Useful Commands

```bash
STACK_NAME=vpclambdatomysql
SECURITY_GROUP=sg-xxxx
SUBNET_ID=subnet-xxx
sam deploy --template-file ./template.yaml --stack-name $STACK_NAME --capabilities CAPABILITY_IAM --parameter-overrides SecurityGroups=$SECURITY_GROUP SubnetIds=$SUBNET_ID
```