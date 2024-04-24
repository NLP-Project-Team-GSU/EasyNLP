from flask import Blueprint, jsonify, request
import string

remove_punctuation_bp = Blueprint('remove_punctuation', __name__)

@remove_punctuation_bp.route('/remove_punctuation', methods=['POST'])
def remove_punctuation():
    text = request.json['text']
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
    return jsonify({'cleaned_text': cleaned_text})
