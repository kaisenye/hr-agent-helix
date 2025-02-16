from flask import Blueprint, request, jsonify
from services.sequence_service import save_sequence, get_sequence

sequence_bp = Blueprint("sequence", __name__)

@sequence_bp.route("/", methods=["POST"])
def save():
    data = request.json
    user_id = data.get("user_id", "default")
    sequence = data.get("sequence", "")
    save_sequence(user_id, sequence)
    return jsonify({"message": "Sequence saved successfully."})

@sequence_bp.route("/", methods=["GET"])
def load():
    user_id = request.args.get("user_id", "default")
    sequence = get_sequence(user_id)
    return jsonify({"sequence": sequence})
