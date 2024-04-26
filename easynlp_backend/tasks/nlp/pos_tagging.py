import nltk
from flask import Blueprint, request, jsonify
from nltk.tokenize import word_tokenize
import os
import ssl

# Disable SSL certificate verification for NLTK
ssl._create_default_https_context = ssl._create_unverified_context

# Add path to included NLTK data directory
nltk_data_path = '/nltk_data'
nltk.data.path.append(nltk_data_path)

# Download NLTK resources if not already downloaded
if not os.path.isdir(os.path.join(nltk_data_path, 'tokenizers')):
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')

pos_tagging_bp = Blueprint('pos_tagging_bp', __name__)


@pos_tagging_bp.route('/pos_tagging', methods=['POST'])
def pos_tag_text():
    text = request.json.get('text')
    tokens = word_tokenize(text)
    tagged_words = nltk.pos_tag(tokens)
    return jsonify({'tagged_words': tagged_words})
