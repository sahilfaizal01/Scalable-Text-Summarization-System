# Scalable-Text-Summarization-System

## Architecture of Text Summarization System
<img src="/assets/news_summary.png">

## Steps Involved for AWS Setup
1) Create IAM User using AWS Console with permission to access AWS Secrets Manager also
2) Install and configure AWS CLI on local system
3) Setup and store API Keys using AWS Secrets Manager
4) Give IAM Permissions for ECR, ECS Access
5) Create docker image and run docker container on local
6) Create ECR container and upload docker container
7) Create IAM Policy for API Key extraction
8) Create ECS Cluster with FarGate then create task definition to load API_KEY from Secrets Manager and run the Docker Container
9) Run the task on the cluster, expose security group to public APIS
