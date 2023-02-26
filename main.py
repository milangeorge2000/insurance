from flask import Flask, request, render_template
import pickle
import pandas as pd
import numpy as np 


app = Flask(__name__)
model1 = pickle.load(open('companies.pkl','rb'))
model2 = pickle.load(open('amount.pkl','rb'))
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/companies.html')
def companies():
    return render_template('companies.html')

@app.route('/amount.html')
def amount():
    return render_template('amount.html')

@app.route("/company_predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # get the form data
        temp_array = list()
       
        claims_processing_time = float(request.form["cpt"])
        premium_cost = float(request.form["pc"])
        deductibles = float(request.form["deductibles"])
        
        temp_array = temp_array + [deductibles,premium_cost,claims_processing_time]
        customer_service_reputation = request.form["Customer_Service_Reputation"]
        if(customer_service_reputation == "Excellent"):
            temp_array += [4]
        elif(customer_service_reputation == "Good"):
            temp_array += [3]
        elif(customer_service_reputation == "Average" ):
            temp_array+= [2]
        elif(customer_service_reputation == "Poor"):
            temp_array+= [1]
        financial_stability = request.form["Financial_Stability"]
        if(financial_stability == "A"):
            temp_array+=[5]
        elif(financial_stability == "B"):
            temp_array+=[4]
        elif(financial_stability == "C"):
            temp_array+=[3]
        elif(financial_stability == "D"):
            temp_array+=[2]
        elif(financial_stability == "E"):
            temp_array+=[1]
        print(temp_array)
        # preprocess the input data
       
        # make a prediction
        y_pred = model1.predict([temp_array])
        pred = ""
        if(y_pred[0] == 0):
            pred = "State Farm"
        elif(y_pred[0] == 1):
            pred = "Progressive"
        elif(y_pred == 2):
            pred = "USSA"
        elif(y_pred == 3):
            pred = "Geico"
        elif(y_pred == 4):
            pred = "AllState"

        # return the predicted company type
        return render_template("result.html",pred=pred)




@app.route('/amount_predict', methods=['POST'])
def amount_result():
 if request.method == "POST":
    
    temp_array = list()
    age = int(request.form['age'])
    bmi = float(request.form['bmi'])
    children = int(request.form['children'])
    temp_array += [age,bmi,children]


    gender = request.form['Gender']
    if(gender == "Male"):
        temp_array += [0,1]
    elif(gender == "Female"):
        temp_array += [1,0]


    smoker = request.form['Smoker']
    if(smoker == "Yes"):
        temp_array += [0,1]
    elif(smoker == "No" ):
        temp_array += [1,0]

    region = request.form['Region']
    if(region == "NorthEast"):
        temp_array += [1,0,0,0]
    
    elif(region == "NorthWest"):
        temp_array += [0,1,0,0]
    
    elif(region == "SouthEast"):
        temp_array += [0,0,1,0]
    
    elif(region == "SouthWest"):
        temp_array += [0,0,0,1]
    
    print(temp_array)
    
    pred =int(model2.predict([temp_array])[0])
    print(pred)
    return render_template("result.html",pred=pred)




if __name__ == "__main__":
    app.run(debug=True)
