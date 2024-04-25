from collections import Counter

import matplotlib.pyplot as plt
import nltk
from flask import Blueprint, request, jsonify
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

word_freq_analysis = Blueprint('word_freq_analysis', __name__)


@word_freq_analysis.route('/word_freq_analysis', methods=['POST'])
def word_freq_count():
    text = request.json.get('text')
    tokens = word_tokenize(text.lower())  # Convert text to lowercase
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]

    word_freq = Counter(filtered_tokens)
    most_common_words = word_freq.most_common(10)  # Change 10 to desired number of most frequent words

    words, frequencies = zip(*most_common_words)

    plt.figure(figsize=(10, 6))
    plt.bar(words, frequencies, color='skyblue')
    plt.title('Top 10 Most Frequent Words (Excluding Stopwords)')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Convert plot to base64 string
    import io
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    import base64
    plot_data = base64.b64encode(buf.read()).decode('utf-8')

    return jsonify({
        'most_common_words': most_common_words,
        'plot_data': plot_data
    })
