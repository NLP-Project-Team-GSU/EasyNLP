from flask import Blueprint, request, jsonify

lowercasing = Blueprint('lowercasing', __name__)


@lowercasing.route('/lowercasing', methods=['POST'])
def lowercase_text():
    text = request.json.get('text')
    lowercased_text = text.lower()
    return jsonify(lowercased_text)
