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