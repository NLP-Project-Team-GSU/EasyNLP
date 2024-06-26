import spacy
from flask import Blueprint, jsonify, request

ner_bp = Blueprint('ner_bp', __name__)

nlp = spacy.load("en_core_web_sm")


@ner_bp.route('/ner', methods=['POST'])
def named_entity_recognition():
    text = request.json.get('text')
    doc = nlp(text)
    entities = [{'text': ent.text, 'label': ent.label_} for ent in doc.ents]
    return jsonify({'entities': entities})
