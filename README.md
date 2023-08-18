# Streamlit App Docker Image

This guide provides step-by-step instructions for setting up and deploying a Streamlit app using Docker on an AWS EC2 instance.

## Prerequisites

- AWS Account: Login to your AWS console and launch an EC2 instance.

## Installation

SSH into your EC2 instance and follow these steps:

1. **Update the package list:**

    ```sh
    sudo apt-get update -y
    ```

2. **Upgrade installed packages:**

    ```sh
    sudo apt-get upgrade
    ```

3. **Install Docker:**

    ```sh
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker ubuntu
    newgrp docker
    ```

4. **Clone your project repository:**

    ```sh
    git clone "your-project"
    ```

5. **Build the Docker image:**

    ```sh
    docker build -t jojis/streamlit:latest .
    ```

6. **View all Docker images:**

    ```sh
    docker images -a
    ```

7. **Run the Docker container:**

    ```sh
    docker run -d -p 8501:8501 jojis/streamlit
    ```

8. **View active containers:**

    ```sh
    docker ps
    ```

9. **Stop a container (replace `container_id` with the actual container ID):**

    ```sh
    docker stop container_id
    ```

10. **Remove stopped containers:**

    ```sh
    docker rm $(docker ps -a -q)
    ```

11. **Login to Docker (if not already logged in):**

    ```sh
    docker login
    ```

12. **Push the Docker image to Docker Hub:**

    ```sh
    docker push jojis/streamlit:latest
    ```

13. **Remove a Docker image (optional):**

    ```sh
    docker rmi jojis/streamlit:latest
    ```

14. **Pull the Docker image (if needed):**

    ```sh
    docker pull jojis/streamlit
    ```

Remember to configure your AWS security groups and firewall settings to allow traffic on port 8501.

**Note:** Ensure that port mapping is done correctly for port 8501.


