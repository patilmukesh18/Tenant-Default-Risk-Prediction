from flask import Flask, render_template, request
import joblib
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the trained model pipeline
model = joblib.load('random_forest_pipeline1.pkl')

# Define the home route
@app.route('/')
def home():
    return render_template('home.html')

# Define the index route (for the input form)
@app.route('/index')
def index():
    return render_template('index.html')  # Render the input form page


# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract data from form
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

        # Make prediction using the loaded pipeline
        prediction = model.predict(input_df)
        result = 'Default Risk: High' if prediction[0] == 1 else 'Default Risk: Low'

        return render_template('result.html', prediction=result)
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
