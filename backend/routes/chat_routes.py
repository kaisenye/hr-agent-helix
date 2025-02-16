from flask import Blueprint, request, jsonify
from services.chat_service import chat_response

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    history = data.get("history", [])
    
    response, updated_history = chat_response(user_message, history)
    return jsonify({
        "response": response,
        "history": updated_history
    })
