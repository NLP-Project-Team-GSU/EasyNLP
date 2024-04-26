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

    # Save the byte stream contents to a file
    with open('wordcloud.png', 'wb') as f:
        f.write(image_stream.getvalue())

    # Return a response indicating successful image generation
    return 'Word cloud image generated successfully'

@word_cloud_bp.route('/word_cloud_image', methods=['GET'])
def get_word_cloud_image():
    # Load the saved image file
    image_path = 'wordcloud.png'

    # Return the image file
    return send_file(image_path, mimetype='image/png')
