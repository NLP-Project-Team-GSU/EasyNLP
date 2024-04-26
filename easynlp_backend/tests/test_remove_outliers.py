import pytest
from flask import Flask, jsonify
from tasks.remove_text_outliers import remove_text_outliers_bp

app = Flask(__name__)
app.register_blueprint(remove_text_outliers_bp)

client = app.test_client()

def test_remove_text_outliers():
    response = client.post('/remove_text_outliers', json={'text': '<p>This is a test 123. You can visit www.example.com</p>'})
    assert response.status_code == 200
    data = response.get_json()
    cleaned_text = data.get('cleaned_text')
    assert cleaned_text == 'This is a test You can visit'

def test_remove_text_outliers_empty():
    response = client.post('/remove_text_outliers', json={'text': ''})
    assert response.status_code == 200
    data = response.get_json()
    cleaned_text = data.get('cleaned_text')
    assert cleaned_text == ''

def test_remove_text_outliers_no_text():
    response = client.post('/remove_text_outliers', json={})
    assert response.status_code == 200
    data = response.get_json()
    cleaned_text = data.get('cleaned_text')
    assert cleaned_text is None

if __name__ == "__main__":
    pytest.main()
