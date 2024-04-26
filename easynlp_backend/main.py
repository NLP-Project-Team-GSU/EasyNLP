from flask import Flask

from tasks.utility.common_checks import detect_language, check_word_count
from tasks.text_preprocessing.handle_contractions import handle_contractions_bp
from tasks.text_preprocessing.lemmatization import lemmatization_bp
from tasks.text_preprocessing.lowercasing import lowercasing_bp
from tasks.nlp.pos_tagging import pos_tagging_bp
from tasks.text_preprocessing.remove_stopwords import remove_stopwords_bp
from tasks.text_preprocessing.remove_text_outliers import remove_text_outliers_bp
from tasks.nlp.sentiment_analysis import sentiment_analysis_bp
from tasks.text_preprocessing.stemming import stemming_bp
from tasks.text_preprocessing.tokenization import tokenization_bp
from tasks.nlp.word_cloud import word_cloud_bp
from tasks.nlp.ner import ner_bp
from tasks.nlp.word_freq_analysis import word_freq_analysis_bp

app = Flask(__name__)


# Register common functions as context processors
@app.context_processor
def inject_common_functions():
    return dict(detect_language=detect_language, check_word_count=check_word_count)


app.register_blueprint(tokenization_bp)
app.register_blueprint(lowercasing_bp)
app.register_blueprint(remove_stopwords_bp)
app.register_blueprint(remove_text_outliers_bp)
app.register_blueprint(lemmatization_bp)
app.register_blueprint(stemming_bp)
app.register_blueprint(handle_contractions_bp)
app.register_blueprint(pos_tagging_bp)
app.register_blueprint(ner_bp)
app.register_blueprint(sentiment_analysis_bp)
app.register_blueprint(word_cloud_bp)
app.register_blueprint(word_freq_analysis_bp)

if __name__ == '__main__':
    app.run(debug=True)
