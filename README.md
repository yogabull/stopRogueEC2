# AWS Lambda Script to stop EC2 instances left running.


![diagram-ec2Stop](https://user-images.githubusercontent.com/34498731/174601680-c241bffd-844a-4497-8b24-39f97248aefe.jpeg)

Architecture diagram.


### Description
An AWS Lambda function that stops EC2 instances.

The goal is to invoke this function daily with AWS EventBridge to stop EC2 instances that were left running.

_UPDATE:_ Lambda function was updated to generate a region list rather than having a region list hard-coded.

### Technologies
Python
AWS Lambda
AWS EventBridge


