import pytest
from flask import Flask, jsonify
from tasks.lemmatization import lemmatization_bp

app = Flask(__name__)
app.register_blueprint(lemmatization_bp)

client = app.test_client()

@pytest.mark.parametrize("text, expected_lemmatized_text", [
    ("dogs running", "dog running"),  # Singularize
    ("I am flying", "I am flying"),  # No change for verbs
    ("The quick brown foxes", "The quick brown fox"),  # Singularize
    ("went", "went"),  # No change for irregular verbs
    ("the apples are red", "the apple are red"),  # Singularize
])
def test_lemmatization(text, expected_lemmatized_text):
    response = client.post('/lemmatization', json={'text': text})
    assert response.status_code == 200
    data = response.get_json()
    lemmatized_text = data.get('lemmatized_text')
    assert lemmatized_text == expected_lemmatized_text

def test_lemmatization_no_text():
    response = client.post('/lemmatization', json={})
    assert response.status_code == 200
    data = response.get_json()
    assert data == {'lemmatized_text': None}

def test_lemmatization_empty_text():
    response = client.post('/lemmatization', json={'text': ''})
    assert response.status_code == 200
    data = response.get_json()
    assert data == {'lemmatized_text': ''}

if __name__ == "__main__":
    pytest.main()
