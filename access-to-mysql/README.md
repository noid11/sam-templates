# access-to-mysql

# Useful Commands

```bash
STACK_NAME=vpclambdatomysql
S3_BUCKET=mybucket
SECURITY_GROUP=sg-xxxx
SUBNET_ID=subnet-xxx
DATABASE_USER=sampleuser
DATABASE_PASSWORD='Mypassword'
DATABASE_HOST=mysql.example.com
DATABASE_NAME=mysql
sam build -u; sam package --output-template-file packaged.yaml --s3-bucket $S3_BUCKET; sam deploy --template-file ./packaged.yaml --stack-name $STACK_NAME --capabilities CAPABILITY_IAM --parameter-overrides SecurityGroups=$SECURITY_GROUP SubnetIds=$SUBNET_ID DatabaseUser=$DATABASE_USER DatabasePassword=$DATABASE_PASSWORD DatabaseHost=$DATABASE_HOST DatabaseName=$DATABASE_NAME
```