import joblib
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier




filename1 = '/home/abrahamoaks/mysite/model/lda_hepB_model.pkl'
model1 = joblib.load(filename1)



app = Flask(__name__, template_folder='/home/abrahamoaks/mysite/templates')
##################################################################################




##################################################################################
    
@app.route('/')
def index():
    return render_template("hepatitis.html")


@app.route("/hepatitis")
def liver():
    return render_template("hepatitis.html")

##################################################################################

@app.route('/predicthepatitis', methods=['POST'])
def predicthepatitis():
    if request.method == 'POST':
        # Get form inputs
        age = float(request.form['age'])
        sex = float(request.form['sex'])
        steroid = float(request.form['steroid'])
        antivirals = float(request.form['antivirals'])
        sgot = float(request.form['sgot'])
        bilirubin = float(request.form['bilirubin'])
        alk_phosphate = float(request.form['alk_phosphate'])
        albumin = float(request.form['albumin'])
        spiders = float(request.form['spiders'])
        histology = float(request.form['histology'])
        fatigue = float(request.form['fatigue'])

        # Create a NumPy array with the input data
        data = np.array([[age, sex, steroid, antivirals, sgot, bilirubin, alk_phosphate, albumin, spiders, histology, fatigue]])
        
        # Make prediction
        my_prediction = model1.predict(data)
        
        # Convert prediction to text
        prediction_text = ""
        if my_prediction == 1:
            prediction_text = "Patient Dies"
        else:
            prediction_text = "Patient Lives"


        return render_template('hepatitis_result.html', prediction_text=prediction_text)

##################################################################################

if __name__ == "__main__":
    app.run(debug=True)
