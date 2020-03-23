# hello-go

golang で Lambda 関数動かすテンプレ

# comamnds

## build

```zsh
cd hello-world
go get

cd ../
make build

go test ./hello-world

sam local invoke --no-event HelloWorldFunction
sam local start-api
```

## deploy

```zsh
# setup
STACK_NAME=mystack
S3_BUCKET=mybucket

# deploy
sam package --output-template-file packaged.yaml --s3-bucket $S3_BUCKET
sam deploy --template-file ./packaged.yaml --stack-name $STACK_NAME --capabilities CAPABILITY_IAM

# cleanup cloudformation stack
aws cloudformation delete-stack --stack-name $STACK_NAME
```