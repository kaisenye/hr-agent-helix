from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:password@localhost/helix"
db = SQLAlchemy(app)

def init_db():
    db.create_all()

if __name__ == "__main__":
    init_db()
