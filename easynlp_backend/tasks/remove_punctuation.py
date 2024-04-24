from flask import Blueprint, jsonify, request
import string
from common_checks import detect_language, check_word_count

remove_punctuation_bp = Blueprint('remove_punctuation', __name__)


@remove_punctuation_bp.route('/remove_punctuation', methods=['POST'])
def remove_punctuation():
    text = request.json.get('text')
    if text:
        language = detect_language(text)
        if language and check_word_count(text):
            cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
            return jsonify({'cleaned_text': cleaned_text})
        else:
            return jsonify({'error': 'Language detection failed or word count exceeds limit'})
    else:
        return jsonify({'error': 'Text not provided'})
