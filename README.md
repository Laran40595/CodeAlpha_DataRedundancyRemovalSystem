# CodeAlpha Data Redundancy Removal System

A cloud-ready data validation and redundancy removal system developed as part of the CodeAlpha Cloud Computing Internship.

## Project Overview

The Data Redundancy Removal System validates incoming user data, checks it against existing records, identifies duplicate or invalid information, and stores only unique and verified records.

The system is built with Python, FastAPI, SQLAlchemy, and SQLite.

## Key Features

- Validates incoming user data
- Validates email addresses
- Validates name length
- Validates phone number length
- Detects duplicate records using email addresses
- Classifies data as:
  - `UNIQUE`
  - `REDUNDANT`
  - `INVALID`
- Prevents duplicate records from being stored
- Stores verified records in a database
- Provides REST API endpoints
- Interactive API documentation with Swagger UI
- Health-check endpoint
- Cloud-ready architecture

## Technology Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- REST API
- Git & GitHub
- Docker

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check that the application is running |
| GET | `/health` | Application health check |
| POST | `/users` | Validate and add a user |
| GET | `/users` | Retrieve stored users |
| GET | `/docs` | Interactive Swagger API documentation |

## Data Classification

### UNIQUE

The submitted data is valid and does not already exist in the database.

```text
UNIQUE -> accepted -> stored

## 📸 Project Screenshots

The following screenshots demonstrate the functionality, API documentation, deployment, and testing of the Data Redundancy Removal System.

### Application & API

![Screenshot 53](./Screenshot%20%2853%29.png)

![Screenshot 54](./Screenshot%20%2854%29.png)

![Screenshot 55](./Screenshot%20%2855%29.png)

### System Functionality & Results

![Screenshot 56](./Screenshot%20%2856%29.png)

![Screenshot 57](./Screenshot%20%2857%29.png)

![Screenshot 58](./Screenshot%20%2858%29.png)

### Deployment & Testing

![Screenshot 59](./Screenshot%20%2859%29.png)

![Screenshot 60](./Screenshot%20%2860%29.png)

![Screenshot 61](./Screenshot%20%2861%29.png)

![Screenshot 62](./Screenshot%20%2862%29.png)
