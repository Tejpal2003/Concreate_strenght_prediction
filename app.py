from flask import Flask , request , app , render_template 
from flask import Response
import pickle
import numpy as np
import pandas as pd


application = Flask(__name__)
app=application


# scaler=pickle.load(open('Model/standardScalar.pkl','rb'))
model=pickle.load(open("Model/Prediction.pkl",'rb'))


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/predictdat",methods=['GET','POST'])
def predict_datapoint():
    result=""
    if request.method=='POST':
        Cement=int(request.form.get('Cement'))
        Blast_Furnace_Slag=float(request.form.get('Blast Furnace Slag'))
        Fly_Ash=float(request.form.get('Fly Ash'))
        Water=float(request.form.get('Water'))
        Superplasticizer=float(request.form.get('Superplasticizer'))
        Coarse_Aggregate=float(request.form.get('Coarse Aggregate'))
        Fine_Aggregate=float(request.form.get('Fine Aggregate'))
        Age=float(request.form.get('Age'))

        new_data=[[Cement,Blast_Furnace_Slag,Fly_Ash,Water,Superplasticizer,Coarse_Aggregate,Fine_Aggregate,Age]]
        prediction=model.predict(new_data)

        result = "%.2f" % round(prediction[0], 2)

        return render_template('index.html' ,result = result)

    # else:
    #     return render_template('index.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/home')
def home ():
    return render_template('index.html')

@app.route('/chatbot')
def chatbot ():
    return render_template('chatbot.html')

if __name__=="__main__":
    app.run(host="0.0.0.0")
