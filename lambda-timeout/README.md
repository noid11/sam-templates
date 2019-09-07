# Lambda Timeout

Lambda that induce execution timeout

# Useful commands

```bash
$ STACK_NAME=mystack

# deploy
$ sam deploy --template-file ./template.yaml --capabilities CAPABILITY_IAM --stack-name $STACK_NAME

# destroy
$ aws cloudformation delete-stack --stack-name $STACK_NAME
```
