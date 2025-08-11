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