#!/bin/bash

# Script to install Docker on Amazon Linux 2

echo "Updating the system..."
sudo yum update -y

echo "Installing Docker..."
sudo yum install -y docker

echo "Starting Docker service..."
sudo systemctl start docker

echo "Enabling Docker to start on boot..."
sudo systemctl enable docker

echo "Adding ec2-user to the docker group..."
sudo usermod -aG docker ec2-user

echo "Docker installation and setup complete."
echo "You may need to log out and back in for group changes to take effect."
