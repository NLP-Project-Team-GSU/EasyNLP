from flask import Blueprint, jsonify, request
from transformers import BertForSequenceClassification, BertTokenizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import torch

sentiment_analysis = Blueprint('sentiment_analysis', __name__)

# Load the pre-trained BERT model and tokenizer
model_name = "bert-base-uncased"
model = BertForSequenceClassification.from_pretrained(model_name)
tokenizer = BertTokenizer.from_pretrained(model_name)

# Set the device to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Function to convert sentiment score to sentiment label
def get_sentiment(sentiment_score):
    return "Positive" if sentiment_score[1] > sentiment_score[0] else "Negative"

@sentiment_analysis.route('/sentiment_analysis', methods=['POST'])
def sentiment_analysis():
    text = request.json['text']
    # Tokenize the text
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    inputs = inputs.to(device)
    # Forward pass through the model
    outputs = model(**inputs)
    # Get the predicted sentiment label
    sentiment_score = torch.softmax(outputs.logits, dim=1).tolist()[0]
    predicted_sentiment = get_sentiment(sentiment_score)

    # Calculate evaluation metrics
    ground_truth_sentiment = request.json.get('ground_truth_sentiment')
    accuracy = accuracy_score([ground_truth_sentiment], [predicted_sentiment])
    precision = precision_score([ground_truth_sentiment], [predicted_sentiment], pos_label="Positive")
    recall = recall_score([ground_truth_sentiment], [predicted_sentiment], pos_label="Positive")
    f1 = f1_score([ground_truth_sentiment], [predicted_sentiment], pos_label="Positive")

    return jsonify({'predicted_sentiment': predicted_sentiment,
                    'sentiment_score': sentiment_score[1],
                    'accuracy': accuracy,
                    'precision': precision,
                    'recall': recall,
                    'f1': f1})

