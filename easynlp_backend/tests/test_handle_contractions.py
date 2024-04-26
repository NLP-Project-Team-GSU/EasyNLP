import pytest
from flask import Flask, jsonify
from tasks.handle_contractions import handle_contractions_bp

app = Flask(__name__)
app.register_blueprint(handle_contractions_bp)

client = app.test_client()

@pytest.mark.parametrize("text, expected_expanded_text", [
    ("I can't do it.", "I cannot do it."),
    ("You'll see.", "You will see."),
    ("They're going.", "They are going."),
    ("It's raining.", "It is raining."),
    ("She'd like some tea.", "She would like some tea."),
    ("He won't go.", "He will not go."),
    ("We've been there.", "We have been there."),
    ("There's no way.", "There is no way."),
])
def test_handle_contractions(text, expected_expanded_text):
    response = client.post('/handle_contractions', json={'text': text})
    assert response.status_code == 200
    data = response.get_json()
    expanded_text = data.get('expanded_text')
    assert expanded_text == expected_expanded_text

def test_handle_contractions_no_text():
    response = client.post('/handle_contractions', json={})
    assert response.status_code == 200
    data = response.get_json()
    assert data == {'expanded_text': None}

def test_handle_contractions_empty_text():
    response = client.post('/handle_contractions', json={'text': ''})
    assert response.status_code == 200
    data = response.get_json()
    assert data == {'expanded_text': ''}

if __name__ == "__main__":
    pytest.main()
