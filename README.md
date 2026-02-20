# 🧠 Disease Prediction ML App (Dockerized)

A machine learning based disease prediction system built using Python.
The application provides a FastAPI backend for prediction APIs and a Streamlit UI for interactive usage.
The project is containerized using Docker to simulate real-world deployment workflows.

---

## 🚀 Project Overview

This project predicts possible diseases based on user symptoms using a trained Machine Learning model.
It demonstrates an end-to-end deployment-ready architecture including:

* Model training & inference
* REST API using FastAPI
* Streamlit-based UI
* Docker containerization
* Production-style folder structure

The main goal of this project is to showcase practical skills in **ML deployment, cloud-ready infrastructure, and monitoring-friendly architecture**.

---

## 🛠️ Tech Stack

* **Python**
* **Scikit-learn**
* **FastAPI**
* **Streamlit**
* **Docker**
* Pandas, NumPy, Joblib

---

## 📂 Project Structure

```
project/
 ├── app/                # FastAPI & Streamlit application code
 ├── models/             # Saved ML models (encoder, scaler, classifier)
 ├── data/               # Sample datasets
 ├── Dockerfile          # Container configuration
 ├── requirements.txt    # Dependencies
 ├── README.md
 └── .gitignore
```

---

## ⚙️ How It Works

1. User enters symptoms from the Streamlit UI.
2. Request goes to FastAPI backend.
3. ML model processes input and predicts disease.
4. Result is returned to UI.

---

## 🐳 Docker Setup

Build Docker image:

```
docker build -t disease-prediction-app .
```

Run container:

```
docker run -p 8000:8000 disease-prediction-app
```

---

## ▶️ Run Locally (Without Docker)

Install dependencies:

```
pip install -r requirements.txt
```

Start FastAPI server:

```
uvicorn app.main:app --reload
```

Run Streamlit UI:

```
streamlit run app/main_app.py
```

---

## 💡 Key Features

* End-to-end ML deployment workflow
* Dockerized architecture
* REST API integration
* Cloud infrastructure ready structure
* Beginner-friendly yet production-inspired design

---

## 🎯 Purpose

This project is part of my learning journey toward Cloud Infrastructure and DevOps-focused roles, demonstrating how Machine Learning systems can be structured, containerized, and prepared for scalable deployment.

---

## 📌 Future Improvements

* Cloud deployment (AWS / EC2)
* Monitoring & logging integration
* CI/CD pipeline setup
* Model versioning

---

## 👨‍💻 Author

**Rovil Katariya**
