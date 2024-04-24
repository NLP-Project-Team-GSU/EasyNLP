from flask import Flask, jsonify, request
from common_functions import detect_language, check_word_count
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

app = Flask(__name__)
lemmatizer = WordNetLemmatizer()

@app.route('/lemmatize', methods=['POST'])
def lemmatize_text():
    text = request.json.get('text')
    if text:
        language = detect_language(text)
        if language and check_word_count(text):
            tokens = word_tokenize(text)
            lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]
            lemmatized_text = ' '.join(lemmatized_tokens)
            return jsonify(lemmatized_text)
        else:
            return jsonify({'error': 'Language detection failed or word count exceeds limit'})
    else:
        return jsonify({'error': 'Text not provided'})

if __name__ == '__main__':
    app.run(debug=True)
