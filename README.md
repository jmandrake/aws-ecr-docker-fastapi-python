[![Test](https://github.com/jmandrake/test-aws-ecr-docker-fastapi-python/actions/workflows/devops.yml/badge.svg)](https://github.com/jmandrake/test-aws-ecr-docker-fastapi-python/actions/workflows/devops.yml)

# test-aws-lambda-fastapi

This demo project was done using this video tutorial:

[Build Real-World AWS Microservices with Python and FastAPI From Zero](https://www.youtube.com/watch?v=SqFFCTNyi88&t=2430s)


1. Create virtual environment venv: python -m venv venv
2. Create empty files: Makefile, requirements.txt, main.py, Dockerfile, mylib/__init__.py
3. Populate the Makefile
    - all: install lint test deploy
4. Set up Continuous Integration, i.e. check code for issues using Pylint
![pylint error](https://user-images.githubusercontent.com/9938598/206826810-69873457-18a1-4aa8-a0b5-ecaa9ef80c60.png)
5. Build CLI using to test the function using fire: 
```
./cli-fire.py --help
./cli-fire.py wiki --length 10
./cli-fire.py wiki --name "Iphone" --length 5
```

## AWS Elastic Container Repository deployment

1) To deploy your docker container to ECR, first create the repo: 
- https://us-east-1.console.aws.amazon.com/ecr/repositories?region=us-east-1
- Use the Push commands for steps on how to push your Docker image to your repository:
-- Add the AWS CLI commands to your Makefile's deploy step on Github

2) Create a project in CodeBuild:
- Doing the deploy step on AWS is easier since your credentials are already set up here
- https://us-east-1.console.aws.amazon.com/codesuite/codebuild/start?region=us-east-1
- Create Build project 
- Source: Github
- Select: Repository in my Github account
- Select Github repository to pull in
- Check: Rebuild every time a code change is pushed to this repository
- Operating system: Amazon Linux 2, Standard runtime
- Check: Priviledged (enable this option for Docker image)
- Use Buildspec.yml file (copy/paste it from Github)
- Create Project
- Click Start Build (This is similar to Github Actions)
- This should push the image into ECR and start the Build process
- Now each time you make a change in Github, the changes will get picked up by CodeBuild automatically and trigger a new build

## Testing your Docker image on ECR with a browser
- Go to AWS App Runner
- Start Service
- Select the container you want (Container image URI)
- Deployment settings: Automatic
- Congratulations: your REST API Microservice project is now in production!


## AWS Codebuild error with pull rate limit

You may get an error that looks like this from AWS CodeBuild during the Build step:

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
More info about that error: https://www.docker.com/increase-rate-limits/

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


![test-aws-lambda-fastapi workflow](https://github.com/jmandrake/test-aws-lambda-fastapi/actions/workflows/devops.yml/badge.svg)

### Notes about Devops
[Key Skills Software Craftsmanship-10 Lessons](https://www.youtube.com/watch?v=qNBr5A0Kzgk)

![image](https://user-images.githubusercontent.com/9938598/207751905-5e80d63a-418c-4bbc-8e4f-222a21458bfb.png)

![image](https://user-images.githubusercontent.com/9938598/207752059-692d7ef9-bb1c-4d88-b080-0d57e8a30547.png)

![image](https://user-images.githubusercontent.com/9938598/207752804-4e3c9fb9-5787-40f3-ac26-cdba8a9aef86.png)


