import pandas as pd
import numpy as np

# Function to generate random data
def generate_tenant_data(num_records=5000):
    np.random.seed(42)
    
    # Generate data
    tenant_ids = np.arange(1, num_records + 1)
    ages = np.random.randint(18, 65, size=num_records)
    occupations = np.random.choice(["Full-time", "Part-time", "Freelancer", "Self-employed", "Unemployed"], size=num_records)
    income_levels = np.random.randint(20000, 150000, size=num_records)
    credit_scores = np.random.randint(300, 850, size=num_records)
    past_defaults = np.random.choice([0, 1], size=num_records, p=[0.9, 0.1])  # 10% chance of past defaults
    debt_to_income_ratios = np.round(np.random.uniform(0.1, 0.5, size=num_records), 2)
    monthly_rents = np.random.randint(500, 5000, size=num_records)
    lease_terms = np.random.choice([6, 12, 24, 36], size=num_records)
    security_deposits = monthly_rents * np.random.choice([1, 2], size=num_records)  # 1-2 months of rent
    property_types = np.random.choice(["Residential", "Commercial"], size=num_records)
    property_sizes = np.random.randint(500, 5000, size=num_records)  # Property size in sq. ft
    unemployment_rates = np.round(np.random.uniform(3.0, 10.0, size=num_records), 2)
    gdp_growth_rates = np.round(np.random.uniform(1.0, 5.0, size=num_records), 2)
    
    # Calculate default risk based on some conditions
    default_risk = [
        1 if (credit_score < 600 or debt_to_income_ratio > 0.4 or past_default == 1) else 0
        for credit_score, debt_to_income_ratio, past_default in zip(credit_scores, debt_to_income_ratios, past_defaults)
    ]
    
    # Create DataFrame
    data = {
        "Tenant_ID": tenant_ids,
        "Age": ages,
        "Occupation": occupations,
        "Income_Level": income_levels,
        "Credit_Score": credit_scores,
        "Past_Default": past_defaults,
        "Debt_to_Income_Ratio": debt_to_income_ratios,
        "Monthly_Rent": monthly_rents,
        "Lease_Term_Months": lease_terms,
        "Security_Deposit": security_deposits,
        "Property_Type": property_types,
        "Property_Size_SqFt": property_sizes,
        "Unemployment_Rate": unemployment_rates,
        "GDP_Growth_Rate": gdp_growth_rates,
        "Default_Risk": default_risk,
    }
    
    return pd.DataFrame(data)

# Generate dataset
num_records = 5000
dataset = generate_tenant_data(num_records)

# Save to CSV
dataset.to_csv("tenant_default_risk_dataset.csv", index=False)
print(f"Dataset with {num_records} records saved to 'tenant_default_risk_dataset.csv'.")
