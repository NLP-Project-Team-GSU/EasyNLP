import nltk
from flask import Blueprint, request, jsonify
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

pos_tagging = Blueprint('pos_tagging', __name__)


@pos_tagging.route('/pos_tagging', methods=['POST'])
def pos_tag_text():
    text = request.json.get('text')
    tokens = word_tokenize(text)
    tagged_words = nltk.pos_tag(tokens)
    return jsonify({'tagged_words': tagged_words})
