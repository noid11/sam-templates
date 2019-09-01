# sam-templates

- my serverless-application-model snipets

# Useful Commands

```bash
$ sam init --runtime python3.7
$ sam build
$ sam package --output-template packaged.yaml --s3-bucket mybucket
$ sam deploy --template-file ./packaged.yaml --stack-name mystack --capabilities CAPABILITY_IAM
$ aws cloudformation describe-stack-events --stack-name mystack
$ aws cloudformation describe-stack-resources --stack-name mystack
$ aws cloudformation delete-stack --stack-name mystack
```

# Useful Links

AWS SAM CLI Command Reference - AWS Serverless Application Model
https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.html

cloudformation — AWS CLI 1.16.230 Command Reference
https://docs.aws.amazon.com/cli/latest/reference/cloudformation/index.html

serverless-application-model/2016-10-31.md at master · awslabs/serverless-application-model
https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi

AWS リソースおよびプロパティタイプのリファレンス - AWS CloudFormation
https://docs.aws.amazon.com/ja_jp/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html

OpenAPI Specification | Swagger
https://swagger.io/specification/

OpenAPI に対する API Gateway 拡張 - Amazon API Gateway
https://docs.aws.amazon.com/ja_jp/apigateway/latest/developerguide/api-gateway-swagger-extensions.html
