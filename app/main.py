from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

movies = joblib.load("movies.pkl")
vectorizer = joblib.load("vectorizer.pkl")
similarity = joblib.load("similarity.pkl")

app = FastAPI()

class InputData(BaseModel):
    amount: float
    time: float
    
def prepare_input(, ):
    input_data = default_input.copy()
    
    input_data['Amount'] = amount
    input_data['Time'] = time
    
    return pd.DataFrame([input_data])
    
@app.post("/predict")
def predict(data: InputData):
    input_df = prepare_input(data.amount, data.time)

    input_df[['Amount','Time']] = vectorizer.transform(input_df[['Amount','Time']])
    input_df[['Amount','Time']] = similarity.transform(input_df[['Amount','Time']])
    
    prob = model.predict_proba(input_df)[0][1]
    
    return {
        "fraud_probability": float(prob),
        "is_fraud": prob > 0.5
}
