import pandas as pd
import numpy as np

# Fix random seed
np.random.seed(42)

# Setup
n_rows = 1000
plants = ['Wolfsburg', 'Hanover', 'Emden', 'Zwickau', 'Dresden']
models = ['Golf', 'Passat', 'Tiguan', 'ID.4', 'Arteon']
model_prices = {'Golf': 22000, 'Passat': 28000, 'Tiguan': 30000, 'ID.4': 35000, 'Arteon': 40000}
departments = ['Assembly', 'Paint Shop', 'Quality Control', 'Logistics', 'R&D']
shifts = ['Morning', 'Evening', 'Night']

# Generate dataset
df = pd.DataFrame({
    'employee_id': np.arange(10000, 10000 + n_rows),
    'plant': np.random.choice(plants, n_rows),
    'model': np.random.choice(models, n_rows),
    'department': np.random.choice(departments, n_rows),
    'shift': np.random.choice(shifts, n_rows),
    'units_produced': np.random.poisson(20, n_rows),
    'defects_found': np.random.binomial(5, 0.1, n_rows),
    'hours_worked': np.round(np.random.normal(8, 1.5, n_rows), 1),
    'experience_years': np.round(np.random.exponential(5, n_rows), 1),
    'is_overtime': np.random.choice([0, 1], n_rows, p=[0.8, 0.2]),
    'date': pd.to_datetime('2023-01-01') + pd.to_timedelta(np.random.randint(0, 365, n_rows), unit='D')
})

# Add price based on model
df['price'] = df['model'].map(model_prices)

# Add quantity (e.g., units sold or processed in a transaction)
df['quantity'] = np.random.randint(1, 10, n_rows)

# Optional: total_value (price * quantity)
#df['total_value'] = df['price'] * df['quantity']

# Save to CSV
df.to_csv("german_manufacturing_data.csv", index=False)