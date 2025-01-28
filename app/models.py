from app import db
from sqlalchemy import Enum

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    insurance = db.Column(db.Integer(), nullable=False)
    address = db.Column(db.String(20), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(20), nullable=False)

class Medications(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(1050), nullable=False)

class Rooms(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    room_type = db.Column(db.String(50), nullable=False)
    available = db.Column(db.String(50), nullable=False)

import joblib
# load model
def load_model():
    model_path = 'app/models/model.joblib'
    with open(model_path, 'rb') as f:
        model = joblib.load(f)
    return model

class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    anaemia = db.Column(db.Integer, nullable=False)
    creatinine_phosphokinase = db.Column(db.Float, nullable=False)
    diabetes = db.Column(db.Integer, nullable=False)
    ejection_fraction = db.Column(db.Float, nullable=False)
    high_blood_pressure = db.Column(db.Integer, nullable=False)
    platelets = db.Column(db.Float, nullable=False)
    serum_creatinine = db.Column(db.Float, nullable=False)
    serum_sodium = db.Column(db.Float, nullable=False)
    sex = db.Column(db.Integer, nullable=False)
    smoking = db.Column(db.Integer, nullable=False)
    predicted_age = db.Column(db.Float, nullable=False)