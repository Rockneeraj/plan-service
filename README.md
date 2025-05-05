# Plan Service

## Overview
This microservice manages recharge plans, including adding, listing, and deleting plans. It is built using Flask and SQLite to keep it lightweight and easy to deploy.

## Features
- Add new recharge plans
- View all available plans
- Delete a specific plan by ID

## API Endpoints

### 1. Add a Plan
- **URL**: `/plans`
- **Method**: `POST`
- **Request Body**:
```json
{
  "name": "Super Saver",
  "price": 149.0,
  "validity": "28 days"
}
```

### 2. Get All Plans
- **URL**: `/plans`
- **Method**: `GET`

### 3. Delete a Plan
- **URL**: `/plans/<id>`
- **Method**: `DELETE`

## Technology Stack
- Python 3.9
- Flask
- Flask-SQLAlchemy
- SQLite

## How to Run with Docker
```bash
docker build -t plans-service:latest .
docker run -p 5001:5001 plans-service:latest
```

## How to Deploy to Kubernetes
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

## Example Data
You can pre-populate plans like:
```json
[
  {
    "name": "Super Saver",
    "price": 149.0,
    "validity": "28 days"
  },
  {
    "name": "Flexi Saver",
    "price": 100.0,
    "validity": "21 days"
  }
]
```
