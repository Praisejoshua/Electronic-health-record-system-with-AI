from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SECRET_KEY"] = "This is a secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///EHRS.db'
app.config['SECRET_KEY'] = '49d36def5362858955171b33'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'connect_args': {'check_same_thread': False}  # Allow multi-threaded access to SQLite
}

db = SQLAlchemy(app)

