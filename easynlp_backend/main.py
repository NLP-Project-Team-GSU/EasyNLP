from flask import Flask
from tasks.remove_punctuation import remove_punctuation_bp
from tasks.sentiment_analysis import sentiment_analysis_bp
from tasks.word_cloud import word_cloud_bp
from tasks.ner import ner_bp

app = Flask(__name__)

app.register_blueprint(remove_punctuation_bp)
app.register_blueprint(sentiment_analysis_bp)
app.register_blueprint(word_cloud_bp)
app.register_blueprint(ner_bp)

if __name__ == '__main__':
    app.run(debug=True)