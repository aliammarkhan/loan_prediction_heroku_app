from flask import Flask, render_template, request
import requests
from joblib import dump, load
import numpy as np
import sklearn


#loading model
model =load('model.pkl')
app = Flask(__name__)

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')



@app.route("/predict", methods=['POST'])
def predict():
    #getting values from the html form
    if request.method == 'POST':
        Gender = int(request.form['Gender'])
        Married = int(request.form['Married'])
        Dependents =int(request.form['Dependents'])
        Education = int(request.form['Education'])
        Self_Employed = int(request.form['Self_Employed'])
        ApplicantIncome = int(float(request.form['ApplicantIncome']))
        CoapplicantIncome = int(float(request.form['CoapplicantIncome']))
        LoanAmount = int(float(request.form['LoanAmount']))
        Loan_Amount_Term = float(request.form['Loan_Amount_Term'])
        Credit_History = int(request.form['Credit_History'])
        Property_Area = int(request.form['Property_Area'])
        
        values = np.array([[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]])

        #predicting from model
        prediction = model.predict(values)

        if prediction[0] == 1:
            return render_template('index.html',prediction_text="Your loan is approved")
        else:
            return render_template('index.html',prediction_text="Your loan cannot be approved at this time")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
