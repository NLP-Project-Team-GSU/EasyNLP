from flask import Flask, jsonify, request
from nltk.tokenize import word_tokenize
from main import app

@app.route('/tokenize', methods=['POST'])
def tokenize_text():
    text = request.json.get('text')
    if text:
        word_count_check = app.jinja_env.globals['check_word_count'](text)
        if word_count_check:
            tokens = word_tokenize(text)
            return jsonify(tokens)
        else:
            return jsonify({'error': 'Word count exceeds limit'})
    else:
        return jsonify({'error': 'Text not provided'})

if __name__ == '__main__':
    app.run(debug=True)
