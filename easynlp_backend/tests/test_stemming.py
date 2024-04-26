import pytest
from flask import Flask, jsonify
from tasks.stemming import stemming_bp

app = Flask(__name__)
app.register_blueprint(stemming_bp)

client = app.test_client()

def test_stem_text():
    response = client.post('/stem', json={'text': 'running jumped beautifully'})
    assert response.status_code == 200
    data = response.get_json()
    stemmed_text = data.get('stemmed_text')
    assert stemmed_text == 'run jump beauti'

def test_stem_text_empty():
    response = client.post('/stem', json={'text': ''})
    assert response.status_code == 200
    data = response.get_json()
    stemmed_text = data.get('stemmed_text')
    assert stemmed_text == ''

def test_stem_text_no_text():
    response = client.post('/stem', json={})
    assert response.status_code == 200
    data = response.get_json()
    stemmed_text = data.get('stemmed_text')
    assert stemmed_text is None

if __name__ == "__main__":
    pytest.main()
