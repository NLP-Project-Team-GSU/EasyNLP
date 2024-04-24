from flask import Flask, jsonify, request
from common_checks import detect_language, check_word_count
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

app = Flask(__name__)
stop_words = set(stopwords.words('english'))


@app.route('/remove_stopwords', methods=['POST'])
def remove_stopwords():
    text = request.json.get('text')
    if text:
        language = detect_language(text)
        if language and check_word_count(text):
            tokens = word_tokenize(text)
            filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
            filtered_text = ' '.join(filtered_tokens)
            return jsonify(filtered_text)
        else:
            return jsonify({'error': 'Language detection failed or word count exceeds limit'})
    else:
        return jsonify({'error': 'Text not provided'})


if __name__ == '__main__':
    app.run(debug=True)
