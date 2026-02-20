import streamlit as st
import joblib
import pandas as pd
import numpy as np

# model load
model = joblib.load("disease_model.joblib")

# processed dataset load (for column order)
df = pd.read_csv("processed_dataset.csv")

# symptom columns
symptom_cols = df.drop(["disease","cures","doctor","risk level"],axis=1).columns

st.title("🩺 Disease Prediction System")

st.write("Select Symptoms:")

# empty input array
input_data = []

for col in symptom_cols:
    val = st.checkbox(col)
    input_data.append(1 if val else 0)

if st.button("Predict Disease"):
    prediction = model.predict([input_data])
    st.success(f"Prediction: {prediction[0]}")