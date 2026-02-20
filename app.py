from fastapi import FastAPI
import joblib
import numpy as np

# FastAPI app create
app = FastAPI()

# Model load
model = joblib.load("disease_model.joblib")

# Home route
@app.get("/")
def home():
    return {"message": "Disease Prediction API is Running"}

# Prediction route
@app.post("/predict")
def predict_disease(fever: int, cough: int, fatigue: int, nausea: int, vomiting: int, chest_pain: int):
    
    # input array
    input_data = np.array([[fever, cough, fatigue, nausea, vomiting, chest_pain]])
    
    # prediction
    prediction = model.predict(input_data)

    return {
        "prediction": int(prediction[0])
    }