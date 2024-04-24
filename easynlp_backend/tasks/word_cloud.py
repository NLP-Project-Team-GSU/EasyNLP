from flask import Blueprint, request, jsonify
from wordcloud import WordCloud
from tasks.common_checks import check_word_count

word_cloud_bp = Blueprint('word_cloud', __name__)


@word_cloud_bp.route('/word_cloud', methods=['POST'])
def generate_word_cloud():
    text = request.json.get('text')
    if text:
        wordcloud = WordCloud(width=800, height=400).generate(text)
        # Convert wordcloud to image and return it
        return wordcloud.to_image()
    else:
        return jsonify({'error': 'Text not provided'})
