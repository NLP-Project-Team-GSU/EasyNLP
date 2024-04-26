from flask import Blueprint, request, jsonify
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()

lemmatization_bp = Blueprint('lemmatization_bp', __name__)


@lemmatization_bp.route('/lemmatization', methods=['POST'])
def generate_word_cloud():
    text = request.json.get('text')
    tokens = word_tokenize(text)
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]
    lemmatized_text = ' '.join(lemmatized_tokens)
    return jsonify(lemmatized_text)
