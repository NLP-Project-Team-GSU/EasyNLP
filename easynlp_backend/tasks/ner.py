from flask import Blueprint, jsonify, request
import spacy
from common_checks import detect_language, check_word_count

ner_bp = Blueprint('ner', __name__)

nlp = spacy.load("en_core_web_sm")


@ner_bp.route('/ner', methods=['POST'])
def named_entity_recognition():
    text = request.json.get('text')
    if text:
        language = detect_language(text)
        if language and check_word_count(text):
            doc = nlp(text)
            entities = [{'text': ent.text, 'label': ent.label_} for ent in doc.ents]
            return jsonify({'entities': entities})
        else:
            return jsonify({'error': 'Language detection failed or word count exceeds limit'})
    else:
        return jsonify({'error': 'Text not provided'})
