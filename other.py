anomaly_detection/
├── README.md
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── endpoints/
│   │   │   ├── __init__.py
│   │   │   ├── anomalies.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── preprocess.py
│   │   ├── detect.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── database.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logging.py
├── tests/
│   ├── __init__.py
│   ├── test_endpoints.py
│   ├── test_models.py
│   ├── test_preprocess.py
│   ├── test_detect.py
├── requirements.txt
└── docker-compose.yml

# Anomaly Detection System

## Setup Instructions

1. Clone the repository:

2. Create and activate a virtual environment:

3. Install dependencies:

4. Set up environment variables:
Create a `.env` file in the root directory and add the following:

5. Initialize the database:

6. Run the application:

## Running Tests
1. Ensure you have `pytest` installed:

2. Run tests:

## API Documentation
API documentation is available at `/docs` once the application is running.

fastapi
uvicorn
pandas
sqlalchemy
psycopg2-binary
scikit-learn
statsmodels
pytest
python-dotenv

version: '3.9'

services:
  web:
    build: .
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - db

  db:
    image: postgres:latest
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: anomaly_db
    ports:
      - "5432:5432"

  redis:
    image: redis:latest
    ports:
      - "6379:6379"