from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://flask:secret@192.168.1.10/flaskdata?charset=utf8mb4"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(80), nullable=False)
    last = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"<{self.first} {self.last}>"

    def to_json(self):
        return {
            "id": self.id,
            "first": self.first,
            "last": self.last,
        }

@app.route("/users", methods=["GET"])
def users():
    users = User.query.all()
    return jsonify([user.to_json() for user in users])

@app.route("/user", methods=["POST"])
def add_user():
    first = request.json['first']
    last = request.json['last']

    new_user = User(first=first, last=last)
    db.session.add(new_user)
    db.session.commit()

    return new_user.to_json()

@app.route("/user/<id>", methods=["GET"])
def user(id):
    user = User.query.get(id)
    return user.to_json()



if __name__ == "__main__":
    app.run(debug=True)
