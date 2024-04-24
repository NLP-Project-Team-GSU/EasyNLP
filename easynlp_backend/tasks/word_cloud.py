from flask import Blueprint, request
from wordcloud import WordCloud

word_cloud_bp = Blueprint('word_cloud', __name__)

@word_cloud_bp.route('/word_cloud', methods=['POST'])
def generate_word_cloud():
    text = request.json['text']
    wordcloud = WordCloud(width=800, height=400).generate(text)
    return wordcloud.to_image()
