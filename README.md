Todo List Application

A simple Todo List web application built with Flask, containerized with Docker, and integrated with a CI/CD pipeline using GitHub Actions. The project demonstrates core DevOps practices, including containerization, automated testing, and infrastructure automation with a shell script for Docker setup.

Features
  - Add, complete, and delete tasks via a web interface
  - Store tasks in a SQLite database
  - Containerized application using Docker for consistent deployment
  - Automated CI/CD pipeline for building and pushing Docker images to Docker Hub
  - Shell script to automate Docker installation and configuration

Technologies
  - Python/Flask: Backend web framework
  - SQLite: Lightweight database for task storage
  - Docker: Containerization for application portability
  - GitHub Actions: CI/CD pipeline for automated testing and deployment
  - Shell Scripting: Automation script for Docker setup

Prerequisites
  - Python 3.8+
  - Docker
  - Git
  - Docker Hub account (for pushing images)

Setup and Running Locally
  - Clone the repository:git clone https://github.com/van49785/todo-app.git
  - cd todo-app

Set up a virtual environment:
  - python -m venv venv



Install dependencies:
  - pip install -r requirements.txt


Run the application:
  - python app.py


Access the app at http://localhost:5000


Run with Docker:
  - docker build -t todo-app .
  - docker run -p 5000:5000 todo-app


Access the app at http://localhost:5000


CI/CD Pipeline

- Trigger: Runs on push to the main branch
- Steps:
    + Checks out code
    + Sets up Python environment
    + Installs dependencies
    + Runs tests (placeholder for unit tests)
    + Builds and pushes Docker image to Docker Hub


Configuration: Store DOCKER_USERNAME and DOCKER_PASSWORD in GitHub Secrets

Automation

- setup-docker.sh: A shell script to automate Docker installation and configuration on Amazon Linux 2. It updates the system, installs Docker, starts the service, and grants permissions to the ec2-user. Designed for EC2 setup but can be adapted for other environments.


