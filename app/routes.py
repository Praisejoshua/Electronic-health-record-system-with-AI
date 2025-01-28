from app import app, render_template
from flask import  url_for, redirect, request, flash
from app.models import Patient, Doctor, Medications, Rooms, Prediction
from app import db
import joblib
from app.forms import PatientForm, DoctorForm, MedicationForm, RoomForm, HeartFailureForm
@app.route("/")
@app.route("/health")
def health():
    return render_template("health.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# sections
@app.route("/patients", methods =["GET", "POST"])
def patients():
    form = PatientForm()
    patient = Patient.query.all() #fetch data queries

    if form.validate_on_submit():
        patient_creates = Patient(
            first_name = form.firstname.data,
            last_name = form.lastname.data,
            insurance = form.insurance.data,
            address = form.address.data,
            phone_number = form.phone_number.data
        )
        db.session.add(patient_creates)
        db.session.commit()

        # retrieve data
        patient = Patient.query.all() #fetch data queries after a new record has been added

        return redirect(url_for('patients'))
    return render_template("patients.html", form = form, patient = patient)


# Edit Route
@app.route("/edit_patient/<int:patient_id>", methods=["GET", "POST"])
def edit_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    form = PatientForm(obj=patient)  # Pre-populate the form with the doctor's data


    if form.validate_on_submit():
        patient.first_name = form.firstname.data
        patient.last_name = form.lastname.data
        patient.insurance = form.insurance.data
        patient.address = form.address.data
        patient.phone_number = form.phone_number.data
        db.session.commit()  # Commit the changes to the database

        # Redirect back to the doctors page after saving the changes
        return redirect(url_for('patients'))

    return render_template("patients.html", form=form, patient=patient)


# delete patient
@app.route("/delete_patient/<int:patient_id>", methods=["POST"])
def delete_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    db.session.delete(patient)
    db.session.commit()
    flash(f"Patient {patient.first_name} {patient.last_name} has been deleted successfully.", "success")
    return redirect(url_for('patients'))



@app.route("/doctors", methods=["GET", "POST"])
def doctors():
    form = DoctorForm()
    doctor = Doctor.query.all()  # Fetch all doctor records

    if form.validate_on_submit():
        doctor_create = Doctor(
            first_name=form.firstname.data,
            last_name=form.lastname.data,
            address=form.address.data
        )
        db.session.add(doctor_create)
        db.session.commit()

        # Fetch updated doctor list after a new record is added
        doctor = Doctor.query.all()

        # Redirect to prevent form resubmission on refresh
        return redirect(url_for('doctors'))

    return render_template("doctors.html", form=form, doctor=doctor)


# Edit Route
@app.route("/edit_doctor/<int:doctor_id>", methods=["GET", "POST"])
def edit_doctor(doctor_id):
    doctor = Doctor.query.get_or_404(doctor_id)
    form = DoctorForm(obj=doctor)  # Pre-populate the form with the doctor's data

    print(f"Doctor data: {doctor.first_name}, {doctor.last_name}, {doctor.address}")  # Debugging line

    if form.validate_on_submit():
        doctor.first_name = form.firstname.data
        doctor.last_name = form.lastname.data
        doctor.address = form.address.data
        db.session.commit()  # Commit the changes to the database

        # Redirect back to the doctors page after saving the changes
        return redirect(url_for('doctors'))

    return render_template("doctors.html", form=form, doctor=doctor)


# delete route
@app.route("/delete_doctor/<int:doctor_id>", methods=["POST"])
def delete_doctor(doctor_id):
    doctor = Doctor.query.get_or_404(doctor_id)
    db.session.delete(doctor)
    db.session.commit()
    flash(f"Doctor {doctor.first_name} {doctor.last_name} has been deleted successfully.", "success")
    return redirect(url_for('doctors'))


@app.route("/medications", methods = ["GET", "POST"])
def medications():
    form = MedicationForm()
    medication = Medications.query.all() #fetch data queries
    if form.validate_on_submit():
        medication_create = Medications(
            name = form.name.data,
            brand = form.brand.data,
            description = form.description.data
        )
        db.session.add(medication_create)
        db.session.commit()
        # retrieve data
        medication = Medications.query.all() #fetch data queries after a new record has been added

        return redirect(url_for("medications"))
    return render_template("medications.html", form = form, medication = medication)


@app.route("/edit_medication/<int:medication_id>", methods=["GET", "POST"])
def edit_medication(medication_id):
    medication = Medications.query.get_or_404(medication_id)  # Fetch the medication by its ID
    form = MedicationForm(obj=medication)  # Pre-populate the form with medication data

    if form.validate_on_submit():
        # Update medication details with the form data
        medication.name = form.name.data
        medication.brand = form.brand.data
        medication.description = form.description.data
        db.session.commit()  # Commit changes to the database
        flash("Medication details updated successfully.", "success")
        return redirect(url_for("medications"))  # Redirect to the medications page

    return render_template("medications.html", form=form, medication=medication)


# delete route
@app.route("/delete_medication/<int:medication_id>", methods=["POST"])
def delete_medication(medication_id):
    medication = Medications.query.get_or_404(medication_id)
    db.session.delete(medication)
    db.session.commit()
    # flash(f"Doctor {medication.first_name} {doctor.last_name} has been deleted successfully.", "success")
    return redirect(url_for('medications'))


@app.route("/rooms", methods = ["GET", 'POST'])
def rooms():
    form = RoomForm()
    room = Rooms.query.all() #fetch data queries
    if form.validate_on_submit():
        room_create = Rooms(
            room_type = form.room_type.data,
            available = form.available.data
        )
        db.session.add(room_create)
        db.session.commit()
        # retrieve data
        room = Rooms.query.all() #fetch data queries after a new record has been added
        return redirect(url_for('rooms'))
    return render_template("rooms.html", form = form, room = room)

# delete route
@app.route("/delete_room/<int:room_id>", methods=["POST"])
def delete_room(room_id):
    room = Rooms.query.get_or_404(room_id)
    db.session.delete(room)
    db.session.commit()
    # flash(f"Doctor {medication.first_name} {doctor.last_name} has been deleted successfully.", "success")
    return redirect(url_for('rooms'))


@app.route("/edit_room/<int:room_id>", methods=["GET", "POST"])
def edit_room(room_id):
    room = Rooms.query.get_or_404(room_id)  # Fetch the room by its ID
    form = RoomForm(obj=room)  # Pre-populate the form with room data

    if form.validate_on_submit():
        # Update room details
        room.room_type = form.room_type.data
        room.available = form.available.data
        db.session.commit()  # Commit changes to the database
        flash("Room details updated successfully.", "success")
        return redirect(url_for("rooms"))  # Redirect to the rooms page

    return render_template("rooms.html", form=form, room=room)


from app.models import load_model
model = load_model()

@app.route("/register", methods=["GET", "POST"])
def register():
    form = HeartFailureForm()

    if form.validate_on_submit():
        input_features = [
            float(form.anaemia.data),
            float(form.creatinine_phosphokinase.data),
            float(form.diabetes.data),
            float(form.ejection_fraction.data),
            float(form.high_blood_pressure.data),
            float(form.platelets.data),
            float(form.serum_creatinine.data),
            float(form.serum_sodium.data),
            float(form.sex.data),
            float(form.smoking.data),
        ]
        
        predicted_age = model.predict([input_features])[0]

        # Save to the database
        new_prediction = Prediction(
            anaemia=form.anaemia.data,
            creatinine_phosphokinase=form.creatinine_phosphokinase.data,
            diabetes=form.diabetes.data,
            ejection_fraction=form.ejection_fraction.data,
            high_blood_pressure=form.high_blood_pressure.data,
            platelets=form.platelets.data,
            serum_creatinine=form.serum_creatinine.data,
            serum_sodium=form.serum_sodium.data,
            sex=form.sex.data,
            smoking=form.smoking.data,
            predicted_age=predicted_age
        )
        db.session.add(new_prediction)
        db.session.commit()
        new_prediction = Prediction(
            anaemia=form.anaemia.data,
            creatinine_phosphokinase=form.creatinine_phosphokinase.data,
            diabetes=form.diabetes.data,
            ejection_fraction=form.ejection_fraction.data,
            high_blood_pressure=form.high_blood_pressure.data,
            platelets=form.platelets.data,
            serum_creatinine=form.serum_creatinine.data,
            serum_sodium=form.serum_sodium.data,
            sex=form.sex.data,
            smoking=form.smoking.data,
            predicted_age=predicted_age
        )
        db.session.add(new_prediction)
        db.session.commit()
        result = f"The Predicted potential age for a heart attack is {predicted_age:.1f} years"
        flash(result, 'success')  # Flash the result with a success category

    return render_template("register.html", form=form)


@app.route("/Analysis")
def predictions():
    all_predictions = Prediction.query.all()
    return render_template("analysis.html", predictions=all_predictions)



