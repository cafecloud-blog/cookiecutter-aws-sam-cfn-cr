# {{ cookiecutter.resource_type }} Custom CloudFormation resource Lambda
This project contains the assets for the development, testing and deployment
of an [AWS CloudFormation Custom Resource]

## Usage
From inside the project root directory, install the project dependencies using [pipenv](https://pipenv.pypa.io/en/latest/#install-pipenv-today)

```bash
pipenv install --dev
```

Build the source project with the [sam cli](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

```bash
sam build
```

Run your function locally with a cloudformation crete-request event
```bash
sam local invoke -e events/create_event.json

```

## Deployment
Once local development is completed, you can deploy the Lambda function using the 

## About
Created by [Jonathan Pelletier](https://www.linkedin.com/in/jonathan-p-089033186/)
