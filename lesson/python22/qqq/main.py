from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///f.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)

    def __repr__(self):  # __str__
        return f"<User {self.name}>"


with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return ""


if __name__ == '__main__':
    app.run(debug=True)
