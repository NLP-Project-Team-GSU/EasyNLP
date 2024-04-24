from flask import Flask

from tasks.common_checks import detect_language, check_word_count
from tasks.remove_punctuation import remove_punctuation_bp
from tasks.sentiment_analysis import sentiment_analysis_bp
from tasks.word_cloud import word_cloud_bp
from tasks.ner import ner_bp

app = Flask(__name__)


# Register common functions as context processors
@app.context_processor
def inject_common_functions():
    return dict(detect_language=detect_language, check_word_count=check_word_count)


app.register_blueprint(remove_punctuation_bp)
app.register_blueprint(sentiment_analysis_bp)
app.register_blueprint(word_cloud_bp)
app.register_blueprint(ner_bp)

if __name__ == '__main__':
    app.run(debug=True)
