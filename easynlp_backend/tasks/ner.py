from flask import Blueprint, jsonify, request
import spacy

ner_bp = Blueprint('ner', __name__)

nlp = spacy.load("en_core_web_sm")

@ner_bp.route('/ner', methods=['POST'])
def named_entity_recognition():
    text = request.json['text']
    doc = nlp(text)
    entities = [{'text': ent.text, 'label': ent.label_} for ent in doc.ents]
    return jsonify({'entities': entities})
