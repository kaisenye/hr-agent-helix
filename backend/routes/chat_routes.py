from flask import Blueprint, request, jsonify
from services.chat_service import chat_response
from flask import current_app as app

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/", methods=["POST"])
def chat():
    app.logger.info('Chat endpoint called')  # Info level logging
    
    try:
        data = request.json
        user_message = data.get("message", "")
        history = data.get("history", [])
        
        app.logger.debug(f'Received message: {user_message}')  # Debug level logging
        app.logger.debug(f'History length: {len(history)}')
        
        response, updated_history = chat_response(user_message, history)
        
        app.logger.info('Chat response generated successfully')
        return jsonify({
            "response": response,
            "history": updated_history
        })
    except Exception as e:
        app.logger.error(f'Error in chat endpoint: {str(e)}')  # Error level logging
        raise
