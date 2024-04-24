from flask import Flask, jsonify, request
from common_checks import detect_language, check_word_count
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

app = Flask(__name__)
ps = PorterStemmer()


@app.route('/stem', methods=['POST'])
def stem_text():
    text = request.json.get('text')
    if text:
        language = detect_language(text)
        if language and check_word_count(text):
            tokens = word_tokenize(text)
            stemmed_tokens = [ps.stem(word) for word in tokens]
            stemmed_text = ' '.join(stemmed_tokens)
            return jsonify(stemmed_text)
        else:
            return jsonify({'error': 'Language detection failed or word count exceeds limit'})
    else:
        return jsonify({'error': 'Text not provided'})


if __name__ == '__main__':
    app.run(debug=True)
