import os

class Config:
    # Security settings
    SECRET_KEY = os.getenv("SECRET_KEY", None)  # Remove default for security
    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set in environment variables")
    
    # API keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)
    if not OPENAI_API_KEY:
        raise ValueError("No OPENAI_API_KEY set in environment variables")
    
    # Database settings
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///helix.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
