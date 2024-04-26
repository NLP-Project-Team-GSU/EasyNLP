import pytest
from flask import Flask, jsonify
from tasks.pos_tagging import pos_tagging_bp

app = Flask(__name__)
app.register_blueprint(pos_tagging_bp)

client = app.test_client()

def test_pos_tag_text():
    response = client.post('/pos_tagging', json={'text': 'This is a test sentence.'})
    assert response.status_code == 200
    data = response.get_json()
    tagged_words = data.get('tagged_words')
    assert tagged_words is not None
    assert len(tagged_words) == 5  # Number of words in the sentence
    # Example assert for specific tagging
    assert tagged_words[0][1] == 'DT'  # 'This' should be tagged as 'DT'

def test_pos_tag_text_empty():
    response = client.post('/pos_tagging', json={'text': ''})
    assert response.status_code == 200
    data = response.get_json()
    tagged_words = data.get('tagged_words')
    assert tagged_words == []

def test_pos_tag_text_no_text():
    response = client.post('/pos_tagging', json={})
    assert response.status_code == 200
    data = response.get_json()
    tagged_words = data.get('tagged_words')
    assert tagged_words is None

if __name__ == "__main__":
    pytest.main()
