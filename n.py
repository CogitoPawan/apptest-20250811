# tests/test_endpoints.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_anomalies():
    response = client.get("/api/v1/anomalies/")
    assert response.status_code == 200

# tests/test_models.py
from app.core import models
from app.db.database import SessionLocal

def test_get_sales_data():
    db = SessionLocal()
    data = models.get_sales_data(db)
    assert data is not None

# tests/test_preprocess.py
from app.core import preprocess
import pandas as pd

def test_clean_sales_data():
    data = pd.DataFrame({"sales_amount": [1, 2, 3, None]})
    cleaned_data = preprocess.clean_sales_data(data)
    assert cleaned_data.isnull().sum().sum() == 0

# tests/test_detect.py
from app.core import detect
import pandas as pd

def test_detect_anomalies_ml():
    data = pd.DataFrame({"sales_amount": [1, 2, 500, 3, 2, 1]})
    anomalies = detect.detect_anomalies_ml(data)
    assert len(anomalies) > 0

def test_detect_anomalies_stat():
    data = pd.DataFrame({"sales_amount": [1, 2, 500, 3, 2, 1]})
    anomalies = detect.detect_anomalies_stat(data)
    assert len(anomalies) > 0