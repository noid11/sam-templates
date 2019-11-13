# Lambda Step Functions Integration

# Useful commands

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
aws lambda invoke --function-name $LAMBDA_FUNCTION_NAME --payload '{ "hoge": "fuga" }' --log-type Tail outputfile.txt | jq -r '.LogResult' | base64 -D

# delete payload save file
rm outputfile.txt

# get Step Functions State Machine
STATE_MACHINE_ARN=$(aws cloudformation describe-stack-resources --stack-name $STACK_NAME | jq -r '.StackResources[] | select(.ResourceType == "AWS::StepFunctions::StateMachine") | .PhysicalResourceId')

# get State Machine detail
aws stepfunctions describe-state-machine --state-machine-arn $STATE_MACHINE_ARN

# get State Machine definition
aws stepfunctions describe-state-machine --state-machine-arn $STATE_MACHINE_ARN | jq '.definition | fromjson'

# start execution State Machine
aws stepfunctions start-execution --state-machine-arn $STATE_MACHINE_ARN

# start execution State Machine, and save execution ARN
EXECUTION_ARN=$(aws stepfunctions start-execution --state-machine-arn $STATE_MACHINE_ARN --query 'executionArn' --output text)

# get execution detail
aws stepfunctions describe-execution --execution-arn $EXECUTION_ARN

# get execution history
aws stepfunctions get-execution-history --execution-arn $EXECUTION_ARN

# cleanup cloudformation stack
aws cloudformation delete-stack --stack-name $STACK_NAME
```

# Useful Links

Creating a Lambda State Machine Using AWS CloudFormation - AWS Step Functions  
https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-lambda-state-machine-cloudformation.html

stepfunctions — AWS CLI 1.16.278 Command Reference  
https://docs.aws.amazon.com/cli/latest/reference/stepfunctions/index.html