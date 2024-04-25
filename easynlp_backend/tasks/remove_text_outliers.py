import re
import string

from flask import Blueprint, jsonify, request

remove_text_outliers = Blueprint('remove_text_outliers', __name__)


@remove_text_outliers.route('/remove_text_outliers', methods=['POST'])
def remove_text_outliers():
    text = request.json.get('text')
    # Remove punctuation
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))

    # Remove HTML tags if present
    cleaned_text = re.sub(r'<.*?>', '', cleaned_text)

    # Remove URLs
    cleaned_text = re.sub(r'http\S+|www\S+', '', cleaned_text)

    # Remove special characters
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', cleaned_text)

    # Remove extra whitespace
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text.strip())

    # Remove numerical values
    cleaned_text = re.sub(r'\d+', '', cleaned_text)
    return jsonify({'cleaned_text': cleaned_text})
