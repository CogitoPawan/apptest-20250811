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