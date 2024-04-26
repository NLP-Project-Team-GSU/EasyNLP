import pytest
from flask import Flask, jsonify
from tasks.tokenization import tokenization_bp

app = Flask(__name__)
app.register_blueprint(tokenization_bp)

client = app.test_client()

@pytest.mark.parametrize("text, expected_tokens", [
    ("The cat is on the mat.", ['The', 'cat', 'is', 'on', 'the', 'mat', '.']),
    ("John loves pizza.", ['John', 'loves', 'pizza', '.']),
    ("I saw a red car.", ['I', 'saw', 'a', 'red', 'car', '.']),
])
def test_tokenize_text(text, expected_tokens):
    response = client.post('/tokenize', json={'text': text})
    assert response.status_code == 200
    data = response.get_json()
    tokens = data
    assert tokens == expected_tokens

def test_tokenize_text_no_text():
    response = client.post('/tokenize', json={})
    assert response.status_code == 200
    data = response.get_json()
    assert data == []

def test_tokenize_text_empty_text():
    response = client.post('/tokenize', json={'text': ''})
    assert response.status_code == 200
    data = response.get_json()
    assert data == []

if __name__ == "__main__":
    pytest.main()
