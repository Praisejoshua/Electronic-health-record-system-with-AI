from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired,  NumberRange, InputRequired
from wtforms import SelectField



class PatientForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    insurance = StringField('Insurance', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    submit = SubmitField('Submit')

class DoctorForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Submit')

class MedicationForm(FlaskForm):
    name = StringField('Medication Name', validators=[DataRequired()])
    brand = StringField('Brand', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RoomForm(FlaskForm):
    room_type = StringField('Room Type', validators=[DataRequired()])
    available = SelectField(
        'Available',
        choices=[('yes', 'Yes'), ('no', 'No')],
        validators=[DataRequired()]
    )
    submit = SubmitField('Submit')


class HeartFailureForm(FlaskForm):
    anaemia = IntegerField('Anaemia (0 = No, 1 = Yes):', validators=[InputRequired(), NumberRange(min=0, max=1)])
    creatinine_phosphokinase = FloatField('Creatinine Phosphokinase (U/L):', validators=[InputRequired()])
    diabetes = IntegerField('Diabetes (0 = No, 1 = Yes):', validators=[InputRequired(), NumberRange(min=0, max=1)])
    ejection_fraction = FloatField('Ejection Fraction (%):', validators=[InputRequired(), NumberRange(min=0, max=100)])
    high_blood_pressure = IntegerField('High Blood Pressure (0 = No, 1 = Yes):', validators=[InputRequired(), NumberRange(min=0, max=1)])
    platelets = FloatField('Platelets (k/μL):', validators=[InputRequired(), NumberRange(min=0)])
    serum_creatinine = FloatField('Serum Creatinine (mg/dL):', validators=[InputRequired(), NumberRange(min=0)])
    serum_sodium = FloatField('Serum Sodium (mmol/L):', validators=[InputRequired(), NumberRange(min=0)])
    sex = IntegerField('Sex (0 = Female, 1 = Male):', validators=[InputRequired(), NumberRange(min=0, max=1)])
    smoking = IntegerField('Smoking (0 = No, 1 = Yes):', validators=[InputRequired(), NumberRange(min=0, max=1)])
    submit = SubmitField('Predict')
