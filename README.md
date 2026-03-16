DevOps & Cloud Quiz Application
Project Overview

This project is a DevOps & Cloud Quiz Application deployed on AWS.
Users can attempt 50 multiple-choice questions related to DevOps, Cloud, AWS, Linux, Docker, Kubernetes, CI/CD, and networking.

The application is designed with a serverless backend and a cloud-hosted frontend.

Users must answer all 50 questions before submitting the quiz.
Each correct answer gives 2 points, and results are stored in AWS DynamoDB.

Live Application

Access the quiz application here:

http://13.63.151.189/

Architecture

The application uses the following AWS services:

Frontend

Hosted on Amazon EC2

NGINX used as the web server

HTML, CSS, and JavaScript used for the quiz interface

Backend

API Gateway

Handles HTTP POST requests

AWS Lambda (Python)

Processes quiz submissions

Calculates scores

Amazon DynamoDB

Stores quiz results

Architecture Flow

User Browser
↓
EC2 Instance (NGINX hosting frontend)
↓
API Gateway (POST endpoint /submit)
↓
AWS Lambda (Python function)
↓
DynamoDB (Stores quiz results)

Features

50 DevOps & Cloud quiz questions

Responsive and modern UI

Real-time progress tracking

Serverless backend

Secure API communication

Results stored in DynamoDB

Score calculated automatically

AWS Services Used

Amazon EC2

Amazon API Gateway

AWS Lambda

Amazon DynamoDB

IAM Roles

Security Groups

Quiz Rules

Total Questions: 50

Each Correct Answer: 2 Points

Maximum Score: 100 Points

Users must attempt all 50 questions before submitting

Security Configuration

EC2 Security Group allows:

HTTP (Port 80)

SSH (Port 22 restricted)

API Gateway configured to allow POST requests only

Lambda uses IAM Role to access DynamoDB

CORS enabled in API Gateway
