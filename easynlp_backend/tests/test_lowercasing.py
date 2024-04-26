import pytest
from flask import Flask, jsonify
from tasks.lowercasing import lowercasing_bp

app = Flask(__name__)
app.register_blueprint(lowercasing_bp)

client = app.test_client()

def test_lowercase_text():
    response = client.post('/lowercasing', json={'text': 'HELLO WORLD'})
    assert response.status_code == 200
    data = response.get_json()
    lowercased_text = data.get('lowercased_text')
    assert lowercased_text == 'hello world'

def test_lowercase_text_empty():
    response = client.post('/lowercasing', json={'text': ''})
    assert response.status_code == 200
    data = response.get_json()
    lowercased_text = data.get('lowercased_text')
    assert lowercased_text == ''

def test_lowercase_text_no_text():
    response = client.post('/lowercasing', json={})
    assert response.status_code == 200
    data = response.get_json()
    lowercased_text = data.get('lowercased_text')
    assert lowercased_text is None

if __name__ == "__main__":
    pytest.main()
