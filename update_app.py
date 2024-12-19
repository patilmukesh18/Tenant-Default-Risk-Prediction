from flask import Flask, render_template, request
import joblib
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the trained models
tenant_default_model = joblib.load('random_forest_pipeline1.pkl')
cost_prediction_model = joblib.load('cost_predicton_pipeline.pkl')

# Define the home route
@app.route('/')
def home():
    return render_template('home.html')  # Render the homepage

# Define the tenant_default route (for the input form)
@app.route('/tenant_default')
def tenant_default():
    return render_template('tenant_default.html')  # Render the tenant default input form page

# Define the cost_price route (for the input form)
@app.route('/cost_price')
def cost_price():
    return render_template('cost_price.html')  # Render the cost prediction input form page

# Define the tenant_default prediction route (for tenant default risk prediction)
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract data from form for tenant default prediction
        input_data = {
            'Age': int(request.form['Age']),
            'Occupation': request.form['Occupation'],
            'Income_Level': int(request.form['Income_Level']),
            'Credit_Score': int(request.form['Credit_Score']),
            'Past_Default': int(request.form['Past_Default']),
            'Debt_to_Income_Ratio': float(request.form['Debt_to_Income_Ratio']),
            'Monthly_Rent': int(request.form['Monthly_Rent']),
            'Lease_Term_Months': int(request.form['Lease_Term_Months']),
            'Security_Deposit': int(request.form['Security_Deposit']),
            'Property_Type': request.form['Property_Type'],
            'Property_Size_SqFt': int(request.form['Property_Size_SqFt']),
            'Unemployment_Rate': float(request.form['Unemployment_Rate']),
            'GDP_Growth_Rate': float(request.form['GDP_Growth_Rate'])
        }

        # Convert input data to DataFrame
        input_df = pd.DataFrame([input_data])

        # Make prediction using the tenant default model
        prediction = tenant_default_model.predict(input_df)
        result = 'Default Risk: High' if prediction[0] == 1 else 'Default Risk: Low'

        return render_template('result.html', prediction=result)

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Define the cost prediction route (for project cost prediction)
@app.route('/result_cost_price', methods=['POST'])
def predict_cost():
    try:
        # Extract data from the form for cost prediction
        input_data = {
            'Project_Type': request.form['Project_Type'],
            'Total_Area_SqFt': float(request.form['Total_Area_SqFt']),
            'Number_of_Floors': int(request.form['Number_of_Floors']),
            'Material_Cost_per_SqFt': float(request.form['Material_Cost_per_SqFt']),
            'Labor_Cost_per_SqFt': float(request.form['Labor_Cost_per_SqFt']),
            'Project_Duration_Months': int(request.form['Project_Duration_Months']),
            'Location_Type': request.form['Location_Type'],
            'Transportation_Cost': float(request.form['Transportation_Cost']),
            'Inflation_Rate': float(request.form['Inflation_Rate']),
            'Complexity': request.form['Complexity'],  # Assuming Complexity is categorical
        }

        # Convert input data to DataFrame
        input_df = pd.DataFrame([input_data])

        # Make prediction using the cost prediction model
        prediction = cost_prediction_model.predict(input_df)
        result = prediction[0]

        return render_template('result_cost_price.html', prediction=result)

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)


