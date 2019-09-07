# Lambda General

Generic Lambda template

# Useful commands

## deploy

```bash
$ STACK_NAME=mystack
$ sam deploy --template-file ./template.yaml --capabilities CAPABILITY_IAM --stack-name $STACK_NAME
```

## delete

```bash
$ STACK_NAME=mystack
$ aws cloudformation delete-stack --stack-name $STACK_NAME
```
