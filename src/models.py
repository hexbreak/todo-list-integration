from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50), unique=False, nullable=False)
    label = db.Column(db.String(250), unique=False, nullable=False)
    done = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
            return '<TodoList %r>'

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user,
            "label": self.label,
            "done": self.done
        }
