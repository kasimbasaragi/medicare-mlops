# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("medicare_model.pkl")

# Input model based on Medicare features
class MedicareInput(BaseModel):
    Average_Covered_Charges: float
    Average_Total_Payments: float
    Reimbursement_Rate: float
    Total_Discharges: float
    Total_Payment: float

@app.get("/")
def read_root():
    return {"message": "Medicare Prediction API is live"}

@app.post("/predict")
def predict(data: MedicareInput):
    input_data = np.array([[
        data.Average_Covered_Charges,
        data.Average_Total_Payments,
        data.Reimbursement_Rate,
        data.Total_Discharges,
        data.Total_Payment
    ]])
    prediction = model.predict(input_data)[0]
    return {"predicted_reimbursement_rate": prediction}

