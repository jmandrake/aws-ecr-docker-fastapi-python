# test-aws-lambda-fastapi

1. Create virtual environment venv
2. Create empty files: Makefile, requirements.txt, main.py, Dockerfile, mylib/__init__.py
3. Populate the Makefile
    - all: install lint test deploy
4. Set up Continuous Integration, i.e. check code for issues using Pylint
![pylint error](https://user-images.githubusercontent.com/9938598/206826810-69873457-18a1-4aa8-a0b5-ecaa9ef80c60.png)
5. Build CLI using to test the function using fire: 
./cli-fire.py --help
./cli-fire.py wiki --length 10
./cli-fire.py wiki --name "Iphone" --length 5

## AWS Codebuild error with pull rate limit

You may get an error that looks like this from AWS CodeBuild:

Step 1/9 : FROM python:3.10.9-slim-buster
3.10.9-slim-buster: Pulling from library/python
toomanyrequests: You have reached your pull rate limit. You may increase the limit by authenticating and upgrading: https://www.docker.com/increase-rate-limit


```
Step 1/9 : FROM python:3.10.9-slim-buster
3.10.9-slim-buster: Pulling from library/python
toomanyrequests: You have reached your pull rate limit. You may increase the limit by authenticating and upgrading: https://www.docker.com/increase-rate-limit
make: *** [deploy] Error 1

[Container] 2022/12/13 07:50:08 Command did not exit successfully make all exit status 2
[Container] 2022/12/13 07:50:08 Phase complete: BUILD State: FAILED
[Container] 2022/12/13 07:50:08 Phase context status code: COMMAND_EXECUTION_ERROR Message: Error while executing command: make all. Reason: exit status 2
```

This may happen if you had to try to rebuild the project multiple times. Try waiting 6 hours and hit the Retry Build button.
More info about that error: (https://www.docker.com/increase-rate-limits/)[https://www.docker.com/increase-rate-limits/]

Alternatively, you could try to authenticate your docker pull command:

To authenticate a docker pull in AWS CodeBuild, you can use the AWS CLI in the buildspec file for your project. The buildspec file is where you define the build environment and the build steps for your CodeBuild project. Here is an example of how you can use the AWS CLI to authenticate a docker pull in your buildspec.yml file:

```
version: 0.2

phases:
  install:
    runtime-versions:
      docker: 19
    commands:
      - aws --version
      - aws configure set default.region us-east-1
      - $(aws ecr get-login --no-include-email)
  build:
    commands:
      - docker build -t my-image .
      - docker tag my-image:latest 012345678901.dkr.ecr.us-east-1.amazonaws.com/my-repository:latest
      - docker push 012345678901.dkr.ecr.us-east-1.amazonaws.com/my-repository:latest
```

In this example, the install phase installs the required version of Docker and configures the AWS CLI with the default region. Then, the build phase uses the aws ecr get-login command to authenticate with Amazon Elastic Container Registry (ECR) and pull the Docker image for your project. This allows you to use the docker build and docker push commands in the build phase to build and push your Docker image to ECR.

Keep in mind that you need to replace 012345678901.dkr.ecr.us-east-1.amazonaws.com/my-repository with the actual URL of your ECR repository. You can find this URL in the Amazon ECR console.
