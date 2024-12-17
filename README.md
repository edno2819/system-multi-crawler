# Distributed Web Crawler System

This MVP project implements a **scalable and distributed web crawler system** designed for performance, reliability, and ease of management. The architecture leverages modern technologies to handle distributed processing, task queuing, and administration.

## Overview

The system is built using:

- **Celery** for distributed task processing
- **Redis** for queue management
- **Requests** for efficient HTTP requests during crawling
- **Django** as the administration interface
- **MySQL** for database management
- **Docker Compose** for environment orchestration
- **Flower** for monitoring Celery workers and tasks
- **Comprehensive logging** for debugging and system tracking

---

## Features

- **Scalable architecture** with distributed worker nodes
- **Task queue management** for efficient crawling workflows
- **Admin interface** for managing sites, monitoring queues, and launching crawlers
- **Centralized logging** for observability and troubleshooting
- **Dockerized environment** for simplified deployment and execution
- **Real-time monitoring** of worker queues and task execution via Flower

---

## System Architecture

The following diagram illustrates the complete system architecture:

<p align="center">
<img style="border-radius: 5px" src="./images/system.png" alt="System Architecture">
</p>

The system operates with a **distributed model** to ensure performance and scalability. Tasks are distributed across worker nodes managed by Celery and monitored through Flower.

---

## Getting Started

Follow the instructions below to set up and run the crawler system on your local machine.

### 1. Prerequisites

Ensure the following dependencies are installed:
- **Docker** and **Docker Compose**
- **Python 3.8+**

### 2. Setup Docker Volumes

Create a directory to store files downloaded by the crawler:

```bash
mkdir /home/${USER}/crawler
```

### 3. Start the System with Docker Compose

Build and run the Docker containers:

```bash
docker-compose up --build -d
```

### 4. Create a Django Admin User

To access the administration interface, create a Django superuser:

1. Identify the Django container ID:

```bash
docker ps
```

2. Access the container shell and create the superuser:

```bash
docker exec -i -t <django_web_container_id> /bin/bash
python manage.py createsuperuser
```

---

## Usage

### 1. Access the Admin Interface

Open your browser and navigate to:

```
http://localhost:8000
```

### 2. Register a New Site

After logging into the admin interface:

1. Navigate to the **"Sites"** tab in the sidebar.
2. Create a new site entry (e.g., "Arezzo").
   - This corresponds to the directory containing the extraction logic for the specific site.

### 3. Run the Crawlers

Once the site is registered and the extraction logic is available, you can launch the crawler:

<p align="center">
<img width="390" style="border-radius: 5px" height="250" src="./images/runCrawler.png" alt="Run Crawler">
</p>

### 4. Monitor Worker Queues

Monitor the distributed crawler system in real time:

1. In the admin interface, click on **"Go to Flower"**.
2. Flower provides insights into:
   - Active workers
   - Task queues
   - Execution history

<p align="center">
<img style="border-radius: 5px" src="./images/flowers.png" alt="Monitor Workers">
</p>

---

## Logging and Debugging

The system provides comprehensive logs for tracking crawler activities, errors, and performance. Logs are accessible within the containers or through configured log directories.

---

### Development Setup
To set up a local development environment:

1. Clone the repository.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the development server:

```bash
python manage.py runserver
```
