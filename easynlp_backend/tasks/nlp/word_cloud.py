from flask import Blueprint, request, send_file
from io import BytesIO
from wordcloud import WordCloud

word_cloud_bp = Blueprint('word_cloud_bp', __name__)

@word_cloud_bp.route('/word_cloud', methods=['POST'])
def generate_word_cloud():
    text = request.json.get('text')
    wordcloud = WordCloud(width=800, height=400).generate(text)

    # Convert wordcloud to byte stream representing the image
    image_stream = BytesIO()
    wordcloud.to_image().save(image_stream, format='PNG')
    image_stream.seek(0)

    # Return the byte stream as an image file
    return send_file(image_stream, mimetype='image/png')
