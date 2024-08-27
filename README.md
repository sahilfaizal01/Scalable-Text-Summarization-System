# Scalable-Text-Summarization-System

## Architecture of News Research Tool
<img src="/assets/News_Research_Tool.drawio.png">

## Architecture of Text Summarization System
<img src="/assets/news_summary.png">

## New Summarization UI
<img src="/assets/news_summary_ui.PNG">

## Steps Involved for AWS Setup
1) Create IAM User using AWS Console with permission to access AWS Secrets Manager also
2) Install and configure AWS CLI on local system
3) Setup and store API Keys using AWS Secrets Manager
4) Give IAM Permissions for ECR, ECS Access
5) Create docker image and run docker container on local
6) Create ECR container and upload docker container
7) Create IAM Policy for API Key extraction
8) Create ECS Cluster with FarGate then create task definition to load API_KEY from Secrets Manager and run the Docker Container
9) Run the task on the cluster, expose security group to public API'S
10) Now add load balancer, when creating task definition add health monitoring and auto scaling for horizontal scaling function
11) Expose the API for load balancer for public usecases

