# Tenant Default Risk Prediction 

## Project Overview

This project aims to build a predictive model that helps developers and property managers assess the risk of tenants defaulting on their rent or lease payments. By analyzing various factors such as tenant demographics, lease details, credit history, property information, and external economic conditions, the model predicts the likelihood of a tenant defaulting, enabling developers to make informed financial decisions.

## Objective

The goal is to predict the likelihood of tenant default on rent payments, which allows developers to evaluate risks and plan financial strategies to mitigate potential losses.

## Problem Statement

Tenants defaulting on rent payments can severely affect cash flow and profitability for developers and property managers. A predictive model based on historical and demographic data can assist in identifying high-risk tenants and provide actionable insights for managing tenant portfolios effectively.

## Key Features for the Model

The model will use the following key features:

### Tenant Demographics:
- Age
- Occupation (Full-time, Part-time, Freelance, Self-employed, Unemployed)
- Income level
- Employment type (Full-time, freelance, self-employed)

### Lease Details:
- Monthly rent amount
- Lease term duration
- Security deposit amount

### Credit and Financial History:
- Credit score
- Past default history (yes/no)
- Debt-to-income ratio

### Property Details:
- Property location and type (Residential/Commercial)
- Property size (in sq. ft)

### External Factors:
- Local unemployment rate
- Economic conditions (GDP growth, inflation)

## Steps to Develop the Model

### 1. Data Collection
- Gather tenant and lease data from rental management software.
- Integrate external economic data such as unemployment rates and inflation.

### 2. Feature Engineering
- Calculate derived features like rent-to-income ratio.
- Categorize credit scores into risk buckets.

### 3. Model Development
- Train various models such as Logistic Regression, Decision Trees, and Gradient Boosting.
- Use historical data from tenants marked as defaulters or non-defaulters.

### 4. Deployment
- Develop a web-based interface where developers can input tenant details and receive a risk assessment score.

### 5. Integration
- Provide recommendations, such as increasing security deposits for high-risk tenants.

## Predicted Outcomes

The model will provide the following predictions and insights:

- **Default Risk Score**: Probability of tenant defaulting.
- **Actionable Insights**: Suggested policies (e.g., requiring co-signers or reducing lease terms).
- **Portfolio Risk Analysis**: Aggregated risk analysis for a group of tenants within a property.

## Technologies Used

- **Python**: For data manipulation and model development
- **Pandas & NumPy**: For data manipulation and analysis
- **Scikit-learn**: For building and training machine learning models
- **Flask/Django**: For creating a web interface (optional)
- **Matplotlib/Seaborn**: For data visualization (optional)

## Dataset Description

A synthetic dataset has been generated to simulate tenant information, which includes 1,000 rows of data with the following columns:

- **Tenant_ID**: Unique identifier for each tenant.
- **Age**: Age of the tenant.
- **Occupation**: Type of employment (Full-time, Self-employed, etc.).
- **Income_Level**: Annual income of the tenant.
- **Credit_Score**: Tenant’s credit score.
- **Past_Default**: Whether the tenant has a history of defaults (0 = No, 1 = Yes).
- **Debt_to_Income_Ratio**: Debt-to-income ratio.
- **Monthly_Rent**: Monthly rent amount.
- **Lease_Term_Months**: Duration of the lease in months.
- **Security_Deposit**: Amount of security deposit.
- **Property_Type**: Type of property (Residential or Commercial).
- **Property_Size_SqFt**: Size of the property in square feet.
- **Unemployment_Rate**: Local unemployment rate.
- **GDP_Growth_Rate**: Local GDP growth rate.
- **Default_Risk**: Target variable indicating whether the tenant defaulted on rent (0 = No, 1 = Yes).

## How to Use the Code

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/tenant-default-risk-prediction.git
    cd tenant-default-risk-prediction
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Generate a synthetic dataset:
    - Run the script `generate_tenant_data.py` to create the dataset. The dataset will be saved as `tenant_default_risk_dataset.csv`.

4. Train the model:
    - Run `train_model.py` to train the predictive model using the generated dataset.

5. Deploy the model:
    - If you're interested in deploying the model, use `deploy_model.py` to create a web-based interface for risk prediction.

## Future Enhancements

- Integrating real-world economic data for improved predictions.
- Enhancing the model with additional features such as tenant behavior analysis and external factors.
- Implementing a more robust model with cross-validation techniques.


