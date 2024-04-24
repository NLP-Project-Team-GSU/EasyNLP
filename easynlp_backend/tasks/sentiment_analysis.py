from flask import Blueprint, jsonify, request
from textblob import TextBlob

sentiment_analysis_bp = Blueprint('sentiment_analysis', __name__)


@sentiment_analysis_bp.route('/sentiment_analysis', methods=['POST'])
def sentiment_analysis():
    text = request.json['text']
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    sentiment = "Positive" if sentiment_score > 0 else "Negative" if sentiment_score < 0 else "Neutral"
    return jsonify({'sentiment': sentiment, 'sentiment_score': sentiment_score})
