from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)
pickle_in=open('classifier_park.pkl','rb')
classifier=pickle.load(pickle_in)

@app.route('/predict')
def prediction_top25():
    
    """Parking_Predictions
    
    ---
    parameters:
        - name: Issue_time
          in: query
          type: number
          required: false
        - name: Marked_Time
          in: query
          type: number
          required: false
        - name: Plate_Expiry_Date
          in: query
          type: number
          required: false
        - name: Agency
          in: query
          type: number
          required: false
        - name: Fine_amount
          in: query
          type: number
          required: ture
        
    responses:
        200:
            description: The output values
    """
    Issue_Time=request.args.get('Issue_Time')
    Marked_Time=request.args.get('Marked_Time')
    Plate_Expiry_Date=request.args.get('Plate_Expiry_Date')
    Agency=request.args.get('Agency')
    Fine_Amount=request.args.get('Fine_Amount')
    
    Prediction=classifier.predict([[Issue_Time,('Marked_Time'),Plate_Expiry_Date,Agency,Fine_Amount]])
    Probability=classifier.predict_proba([[Issue_Time,'Marked_Time',Plate_Expiry_Date,Agency,Fine_Amount]])
    return "Prediction Value"+str(Prediction)+str(Probability)
    
@app.route('/predict_file',methods=["POST"])
def prediction_top_25_file():
    """Parking Prediction file
    ---
    parameters:
        - name: file
          in: formData
          type: file
          required: true
    responses:
        200:
            description: The output values
    """
    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction=classifier.predict(df_test)
    returnstr(list(prediction))

if __name__=='__main__':
    app.run()
