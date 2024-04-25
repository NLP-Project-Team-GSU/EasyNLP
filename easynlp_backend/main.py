from flask import Flask

from tasks import remove_stopwords, tokenization, stemming, lowercasing, lemmatization, pos_tagging, \
    handle_contractions, word_freq_analysis
from tasks.common_checks import detect_language, check_word_count
from tasks.remove_text_outliers import remove_text_outliers
from tasks.sentiment_analysis import sentiment_analysis
from tasks.word_cloud import word_cloud
from tasks.ner import ner

app = Flask(__name__)


# Register common functions as context processors
@app.context_processor
def inject_common_functions():
    return dict(detect_language=detect_language, check_word_count=check_word_count)

app.register_blueprint(tokenization)
app.register_blueprint(lowercasing)
app.register_blueprint(remove_stopwords)
app.register_blueprint(remove_text_outliers)
app.register_blueprint(lemmatization)
app.register_blueprint(stemming)
app.register_blueprint(handle_contractions)
app.register_blueprint(pos_tagging)
app.register_blueprint(ner)
app.register_blueprint(sentiment_analysis)
app.register_blueprint(word_cloud)
app.register_blueprint(word_freq_analysis)


if __name__ == '__main__':
    app.run(debug=True)
