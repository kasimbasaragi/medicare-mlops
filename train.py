# train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset from GitHub
url = "https://raw.githubusercontent.com/plotly/datasets/master/medicare.csv"
df = pd.read_csv(url)

# Debug: print all columns
print("✅ Columns:", df.columns.tolist())

# Step 1: Strip column names of leading/trailing spaces
df.columns = df.columns.str.strip()

# Step 2: Clean currency and numeric columns (remove commas and $)
cols_to_clean = [
    'Average Covered Charges',
    'Average Total Payments',
    'Total Discharges',
    'Total Payment'
]

for col in cols_to_clean:
    df[col] = df[col].astype(str) \
                     .replace('[\$,]', '', regex=True) \
                     .str.replace(',', '') \
                     .astype(float)

# Step 3: Convert target column to float
df['Reimbursement Rate'] = df['Reimbursement Rate'].astype(float)

# Step 4: Select features and target
X = df[[
    'Average Covered Charges',
    'Average Total Payments',
    'Reimbursement Rate',
    'Total Discharges',
    'Total Payment'
]]

y = df['Reimbursement Rate']  # Regression target

# Step 5: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Train model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Step 7: Save model
joblib.dump(model, "medicare_model.pkl")
print("✅ Model saved as medicare_model.pkl")

