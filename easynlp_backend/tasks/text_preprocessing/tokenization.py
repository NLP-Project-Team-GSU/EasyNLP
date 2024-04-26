from flask import Blueprint, jsonify, request
from nltk.tokenize import word_tokenize

tokenization_bp = Blueprint('tokenization_bp', __name__)


@tokenization_bp.route('/tokenize', methods=['POST'])
def tokenize_text():
    text = request.json.get('text')
    tokens = word_tokenize(text)
    return jsonify(tokens)
