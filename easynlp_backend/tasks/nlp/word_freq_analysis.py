from collections import Counter
import nltk
from flask import Blueprint, request, jsonify
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

word_freq_analysis_bp = Blueprint('word_freq_analysis_bp', __name__)

@word_freq_analysis_bp.route('/word_freq_analysis', methods=['POST'])
def word_freq_count():
    text = request.json.get('text')
    tokens = word_tokenize(text.lower())  # Convert text to lowercase
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]

    word_freq = Counter(filtered_tokens)
    most_common_words = word_freq.most_common(10)  # Change 10 to desired number of most frequent words

    return jsonify({
        'most_common_words': most_common_words,
    })
