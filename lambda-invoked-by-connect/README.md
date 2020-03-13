
# Lambda invoked by Connect

Amazon Connect から呼び出し可能な Lambda 関数をデプロイするテンプレ

# commands

```bash
# deploy cloudformation stack
STACK_NAME=mystack
sam deploy --template-file ./template.yaml --capabilities CAPABILITY_IAM --stack-name $STACK_NAME

# get Lambda Function Name
LAMBDA_FUNCTION_NAME=$(aws cloudformation describe-stack-resources --stack-name $STACK_NAME | jq -r '.StackResources[] | select(.ResourceType == "AWS::Lambda::Function") | .PhysicalResourceId')
echo $LAMBDA_FUNCTION_NAME

# get Lambda Function Details
aws lambda get-function --function-name $LAMBDA_FUNCTION_NAME

# invoke Lambda Function, raw log to stdout
aws lambda invoke --function-name $LAMBDA_FUNCTION_NAME --payload '{ "name": "Bob" }' --log-type Tail outputfile.txt | jq -r '.LogResult' | base64 -D

# If Use AWS CLI v2
aws lambda invoke --function-name $LAMBDA_FUNCTION_NAME --payload $(echo '{ "name": "Bob" }' | base64) --log-type Tail outputfile.txt | jq -r '.LogResult' | base64 -D

# delete payload save file
rm outputfile.txt

# cleanup cloudformation stack
aws cloudformation delete-stack --stack-name $STACK_NAME
```

# ref

Lambda 関数を呼び出す - Amazon Connect  
https://docs.aws.amazon.com/ja_jp/connect/latest/adminguide/connect-lambda-functions.html
