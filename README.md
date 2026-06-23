# Cloud-Native Application Deployment on Amazon EKS using Terraform, Docker, ECR and GitHub Actions

## Project Overview

This project demonstrates a complete cloud-native DevOps platform built using AWS EKS, Terraform, Docker, Kubernetes, Amazon ECR, and GitHub Actions.

The application is a Python Flask-based web application containerized using Docker, deployed to Amazon EKS Kubernetes cluster, and managed through Infrastructure as Code (IaC) using Terraform.

---

## Architecture

Developer

↓ Push Code

GitHub Repository

↓ CI Pipeline

GitHub Actions

↓ Build Container

Docker Image

↓ Push Image

Amazon ECR

↓ Deployment

Amazon EKS Cluster

↓ Kubernetes Objects

Deployment + Service (LoadBalancer)

↓ Access Application

AWS Load Balancer Endpoint


---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| Cloud | AWS |
| Infrastructure as Code | Terraform |
| Containerization | Docker |
| Container Registry | Amazon ECR |
| Container Orchestration | Amazon EKS Kubernetes |
| CI/CD | GitHub Actions |
| Programming | Python Flask |
| OS | Linux |

---

# Project Structure

```
eks-devops-platform
│
├── .github/workflows/main.yaml
│   └── GitHub Actions CI Pipeline
│
├── app
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── kubernetes
│   ├── deployment.yaml
│   └── service.yaml
│
├── terraform
│   ├── provider.tf
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
```

---

## Infrastructure Provisioning using Terraform

Terraform provisions:

- AWS VPC
- Public and Private Subnets
- Internet Gateway
- NAT Gateway
- Route Tables
- DNS Hostnames
- Amazon EKS Cluster
- EKS Managed Node Group
- IAM Roles and Policies

### EKS Cluster Configuration

- Kubernetes Version: 1.28
- Node Group: Managed Node Group
- Instance Type: t3.small
- Capacity Type: ON_DEMAND
- Worker Nodes: 1
- Region: ap-south-1

---

## CI/CD Pipeline

GitHub Actions pipeline performs the following tasks:

1. Checkout source code from GitHub
2. Setup Python 3.9 environment
3. Install Python dependencies
4. Validate Python application syntax
5. Build Docker container image

Pipeline file:

```
.github/workflows/main.yaml
```

---

## Docker Containerization

The Flask application is containerized using Docker.

Docker process:

- Python 3.9 base image
- Working directory configuration
- Application code copy
- Dependency installation using pip
- Expose application port 5000
- Start Flask application

---

## Kubernetes Deployment

The application is deployed into Amazon EKS using:

### Deployment

- Replica Count: 2
- Container Image from Amazon ECR
- Automatic image pull using latest tag

### Service

- Service Type: LoadBalancer
- External access through AWS Load Balancer
- Port Mapping:
  - Port 80 → Container Port 5000

---

## Application Features

The Flask application displays:

- Pod hostname
- Operating System
- OS Version
- Machine Architecture
- Application execution timestamp

This helps verify Kubernetes pod scheduling and application deployment.

---

## Deployment Workflow

Developer Code

↓ 

GitHub

↓

GitHub Actions CI

↓

Docker Build

↓

Amazon ECR

↓

Amazon EKS

↓

Kubernetes Deployment

↓

AWS Load Balancer

↓

End User


---

## Terraform Commands

Initialize Terraform:

```bash
terraform init
```

Preview infrastructure:

```bash
terraform plan
```

Create infrastructure:

```bash
terraform apply
```

Destroy infrastructure:

```bash
terraform destroy
```

---

## Kubernetes Commands

View Nodes:

```bash
kubectl get nodes
```

View Pods:

```bash
kubectl get pods
```

View Services:

```bash
kubectl get svc
```

Deploy Application:

```bash
kubectl apply -f kubernetes/
```

---

## Learning Outcomes

Through this project, I gained hands-on experience in:

- Designing AWS network architecture
- Provisioning infrastructure using Terraform
- Creating Amazon EKS clusters
- Managing Kubernetes workloads
- Containerizing applications with Docker
- Implementing CI pipelines using GitHub Actions
- Deploying scalable applications in Kubernetes environments
- Working with cloud-native DevOps workflows

---

## Future Enhancements

- Integrate Amazon ECR push in GitHub Actions
- Implement CD pipeline for automated Kubernetes deployment
- Use Terraform remote backend with S3 and DynamoDB locking
- Add Kubernetes monitoring using Prometheus and Grafana
- Implement Helm charts for Kubernetes deployment
