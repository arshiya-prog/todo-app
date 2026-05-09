# 📝 Todo App with CI/CD Pipeline using Jenkins
A simple Todo Application developed with Python and automated using a complete CI/CD pipeline with Jenkins, GitHub Webhooks, Docker, and Kubernetes deployment.

---

## 🚀 Project Overview
This project demonstrates how a CI/CD pipeline can automate the process of building, testing, and deploying an application whenever code changes are pushed to GitHub.

The application is a basic Todo App where users can manage daily tasks. The focus of this project was not only application development but also implementing DevOps practices for continuous integration and deployment.

---

## 🛠️ Technologies Used
- Python
- Flask
- HTML/CSS/Bootstrap
- Jenkins
- GitHub Webhooks
- Docker
- Kubernetes
- Git & GitHub

---

## ⚙️ Features
- Add and manage tasks
- Simple and responsive UI
- Automated CI/CD pipeline using Jenkins
- GitHub webhook integration for automatic builds
- Dockerized application
- Kubernetes deployment support

---

## 🔄 CI/CD Workflow
1. Developer pushes code to GitHub
2. GitHub Webhook triggers Jenkins pipeline
3. Jenkins pulls latest code from repository
4. Application is built and tested
5. Docker image is created
6. Deployment is updated on Kubernetes

This automation reduces manual effort and ensures faster, reliable deployments.

---

## 📂 Project Structure
```bash
todo-app/
│── kubernetes/
│   │── deployment.yaml
│   └── service.yaml
│── templates/
│   └── index.html
│── Dockerfile
│── Jenkinsfile
│── app.py
│── requirements.txt


## Author:
Arshiya Uppal
