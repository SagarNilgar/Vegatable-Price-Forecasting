from flask import Flask, jsonify, render_template, request
import joblib
import os
import numpy as np

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route('/predict',methods=['POST','GET'])
def result():
    
    
    state= float(request.form['state'])
    district=float(request.form['district'])
    day= float(request.form['day'])
    month= float(request.form['month'])

    X= np.array([[ state,district,day,month]])
    
    scaler_path= r'D:\VIT\Sem 5 (3 yr)\vegatble_forcatsing\Vegatable-Price-Forecasting\models\sc1.sav'
    
    sc=joblib.load(scaler_path)

    X_std= sc.transform(X)

    model_path=r'D:\VIT\Sem 5 (3 yr)\vegatble_forcatsing\Vegatable-Price-Forecasting\models\RF.sav'

    model= joblib.load(model_path)

    Y_pred=model.predict(X_std)

    return jsonify({'Prediction': float(Y_pred)})
    





if __name__ == "__main__":
    app.run(debug=True, port=9457)