# CSCIE-91 Cloud DevOps Final Project, 2019

Black group:
* Ethan Haynes
* Sanu Ann Abraham
* Jim DePina

## Overview
An open source project that you are testing and publishing through a public 
GitHub repository.

The repository on GitHub has three branches:
1. __dev__ for development
2. __stage​__ for staging and testing
3. __master​__ for production.

## How does it work?
1. Using webhooks, Jenkins gets notified when a commit is pushed to any of the 
three branches in public GitHub repository.
2. When a developer pushes updates to the dev branch, Jenkins will build (using 
Dockerfile and the site files in the repository) a dev environment in the dev EC2 instance in AWS.
3. If things are fine, Jenkins will merge the dev branch with the stage branch and 
push the merge. The push will trigger Jenkins to build the stage environment in AWS and perform testing on the environment. 
4. Test stage involves testing the contents, whether the site is up or not, and 
whether the HTML file(s) is/are valid.
5. If all tests pass in dev and stage, Jenkins will merge stage with master and 
trigger the production server to build from the new updated master.
6. The sites (Prod, Dev and Stage) will all run on Docker containers on CentOS 7 
machines.

## Run tests
```sh
$: python3 test.py 
All tests passed
```
