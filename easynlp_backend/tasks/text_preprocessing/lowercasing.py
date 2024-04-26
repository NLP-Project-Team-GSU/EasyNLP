from flask import Blueprint, request, jsonify

lowercasing_bp = Blueprint('lowercasing_bp', __name__)


@lowercasing_bp.route('/lowercasing', methods=['POST'])
def lowercase_text():
    text = request.json.get('text')
    lowercased_text = text.lower()
    return jsonify({'lowercased_text': lowercased_text})
