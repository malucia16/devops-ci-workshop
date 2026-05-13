import app

def test_home():
    client = app.app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"
    assert data["service"] == "devops-api"

def test_health():
    client = app.app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert 'cpu_percent' in data
    assert 'memory_percent' in data
    assert 'status' in data

def test_metrics():
    client = app.app.test_client()
    response = client.get('/metrics')
    assert 'app_cpu_percent' in text
    assert 'app_memory_percent' in text
