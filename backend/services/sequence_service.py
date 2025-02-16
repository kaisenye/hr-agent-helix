from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Sequence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)

def save_sequence(user_id, sequence_text):
    """Save or update a user's sequence in the database."""
    try:
        existing_sequence = Sequence.query.filter_by(user_id=user_id).first()
        if existing_sequence:
            existing_sequence.content = sequence_text
        else:
            new_sequence = Sequence(user_id=user_id, content=sequence_text)
            db.session.add(new_sequence)
        db.session.commit()
        print(f"Sequence saved for user {user_id}.")
        return {"message": "Sequence saved successfully."}
    except Exception as e:
        db.session.rollback()
        print(f"Error saving sequence: {e}")
        return {"error": "Failed to save sequence."}

def get_sequence(user_id):
    """Retrieve a user's saved sequence."""
    try:
        sequence = Sequence.query.filter_by(user_id=user_id).first()
        if sequence:
            return {"sequence": sequence.content}
        else:
            return {"message": "No sequence found."}
    except Exception as e:
        print(f"Error retrieving sequence: {e}")
        return {"error": "Failed to retrieve sequence."}

def update_sequence(user_id, new_text):
    """Update an existing sequence."""
    try:
        sequence = Sequence.query.filter_by(user_id=user_id).first()
        if sequence:
            sequence.content = new_text
            db.session.commit()
            print(f"Sequence updated for user {user_id}.")
            return {"message": "Sequence updated successfully.", "updated_sequence": sequence.content}
        return {"message": "No sequence found to update."}
    except Exception as e:
        db.session.rollback()
        print(f"Error updating sequence: {e}")
        return {"error": "Failed to update sequence."}
