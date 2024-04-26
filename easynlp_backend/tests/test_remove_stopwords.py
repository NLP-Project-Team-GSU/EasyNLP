import pytest
from flask import Flask, jsonify
from tasks.remove_stopwords import remove_stopwords_bp

app = Flask(__name__)
app.register_blueprint(remove_stopwords_bp)

client = app.test_client()

def test_remove_stopwords():
    response = client.post('/remove_stopwords', json={'text': 'This is a test sentence'})
    assert response.status_code == 200
    data = response.get_json()
    filtered_text = data.get('filtered_text')
    assert filtered_text == 'test sentence'

def test_remove_stopwords_empty():
    response = client.post('/remove_stopwords', json={'text': ''})
    assert response.status_code == 200
    data = response.get_json()
    filtered_text = data.get('filtered_text')
    assert filtered_text == ''

def test_remove_stopwords_no_text():
    response = client.post('/remove_stopwords', json={})
    assert response.status_code == 200
    data = response.get_json()
    filtered_text = data.get('filtered_text')
    assert filtered_text is None

if __name__ == "__main__":
    pytest.main()
