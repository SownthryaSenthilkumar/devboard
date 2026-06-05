# DevBoard - Task Management API

## Overview
DevBoard is a RESTful Task Management API built using FastAPI.  
It provides basic CRUD operations for managing tasks and demonstrates backend development, containerization, and deployment practices.

---

## Live Demo
API Base URL:  
https://devboard-ngmt.onrender.com  

API Documentation (Swagger UI):  
https://devboard-ngmt.onrender.com/docs  

---

## Tech Stack
- Python
- FastAPI
- Uvicorn
- Docker
- Render (Cloud Deployment)
- GitHub Actions (CI/CD)

---

## Features
- Create tasks
- Retrieve all tasks
- Update tasks
- Delete tasks
- Interactive API documentation via Swagger UI

---

## Project Structure

devboard/
│
├── backend/
│ ├── main.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── .github/workflows/
│ └── docker.yml
│
└── README.md

## CI/CD Pipeline
- GitHub Actions automatically builds and pushes Docker image on every push to main
- Deployed on Render with automatic redeploys
