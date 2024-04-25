from flask import Blueprint, request, jsonify
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

ps = PorterStemmer()

stemming = Blueprint('stem', __name__)


@stemming.route('/stem', methods=['POST'])
def stem_text():
    text = request.json.get('text')
    tokens = word_tokenize(text)
    stemmed_tokens = [ps.stem(word) for word in tokens]
    stemmed_text = ' '.join(stemmed_tokens)
    return jsonify({'stemmed_text': stemmed_text})
