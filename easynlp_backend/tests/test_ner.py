from flask import Flask, jsonify
from tasks.nlp.ner import ner_bp

app = Flask(__name__)
app.register_blueprint(ner_bp)

client = app.test_client()


def test_named_entity_recognition():
    response = client.post('/ner', json={'text': 'Apple is located in California.'})
    assert response.status_code == 200
    data = response.get_json()
    entities = data.get('entities')
    assert entities is not None
    assert len(entities) == 2
    assert entities[0]['text'] == 'Apple'
    assert entities[0]['label'] == 'ORG'
    assert entities[1]['text'] == 'California'
    assert entities[1]['label'] == 'GPE'
