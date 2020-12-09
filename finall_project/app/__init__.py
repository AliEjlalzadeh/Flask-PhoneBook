from flask import Flask,redirect
from app.packages import phone_book
from .init import db


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pbDB.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "sfgHGhg!34khlj*d#ert"
    db.init_app(app)
    @app.route("/")
    def say_hello():
        return redirect("/index")
    app.register_blueprint(phone_book.bp)
    return app
