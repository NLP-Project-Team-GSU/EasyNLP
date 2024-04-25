from flask import Blueprint, request
from wordcloud import WordCloud

word_cloud = Blueprint('word_cloud', __name__)


@word_cloud.route('/word_cloud', methods=['POST'])
def generate_word_cloud():
    text = request.json.get('text')
    wordcloud = WordCloud(width=800, height=400).generate(text)
    # Convert wordcloud to image and return it
    return wordcloud.to_image()
