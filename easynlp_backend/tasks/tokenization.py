from flask import Blueprint, jsonify, request
from nltk.tokenize import word_tokenize

tokenization = Blueprint('tokenization', __name__)


@tokenization.route('/tokenize', methods=['POST'])
def tokenize_text():
    text = request.json.get('text')
    tokens = word_tokenize(text)
    return jsonify(tokens)
