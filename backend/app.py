from flask import Flask, make_response, request
from flask_cors import CORS
from routes.chat_routes import chat_bp
from routes.sequence_routes import sequence_bp
from database.db_init import db
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)
app.logger.setLevel(logging.DEBUG)  # Set Flask app logger level

# Configure CORS with all necessary headers and methods
CORS(app, 
    resources={r"/*": {
        "origins": "*",  # Allow all origins
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
        "expose_headers": ["Content-Type", "Authorization"],
        "supports_credentials": False  # Must be False when using "*" for origins
    }}
)

# Add before_request handler to log all requests
@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', request.get_data())

# Add before_request handler to properly handle OPTIONS requests
@app.before_request
def before_request():
    if request.method == "OPTIONS":
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
        response.headers.add("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
        return response

# Database Config
app.config.from_object("config")

# Register Blueprints - ensure routes don't have trailing slashes
app.register_blueprint(chat_bp, url_prefix="/chat")
app.register_blueprint(sequence_bp, url_prefix="/sequence")

# Disable strict slashes to handle both /chat and /chat/ URLs
app.url_map.strict_slashes = False

if __name__ == "__main__":
    app.run(debug=True)
