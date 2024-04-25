from flask import Blueprint, jsonify, request
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

nltk.download('punkt')
nltk.download('stopwords')

remove_stopwords_bp = Blueprint('remove_stopwords', __name__)


@remove_stopwords_bp.route('/remove_stopwords', methods=['POST'])
def remove_stopwords():
    text = request.json.get('text')
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))  # Load English stopwords
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    filtered_text = ' '.join(filtered_tokens)
    return jsonify({'filtered_text': filtered_text})
