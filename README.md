# 🎓 Student Performance Prediction

A Machine Learning project that predicts a student's final grade (G3) based on academic, demographic, social, and behavioral features.

## 🚀 Live Demo

## 🚀 Live Demo

👉 [Try the Student Performance Prediction App](https://studentpreformanceprediction-bxjysntatgzrif2lhuf7vg.streamlit.app/)

## 📌 Project Overview

This project uses the UCI Student Performance dataset to predict the final student grade.

The project covers:

- Data Loading
- Exploratory Data Analysis
- Data Preprocessing
- Numerical Feature Scaling
- Categorical Feature Encoding
- Train-Test Split
- Machine Learning Model Training
- Model Comparison
- Best Model Selection
- Model Serialization
- Streamlit Deployment

## 📊 Dataset

Dataset: UCI Student Performance Dataset

Target Variable:

- G3 — Final Grade

The target variable ranges from 0 to 20.

## 🤖 Machine Learning Models

The following regression models were compared:

1. Linear Regression
2. Ridge Regression
3. Lasso Regression
4. Random Forest Regressor
5. Gradient Boosting Regressor

## 🏆 Model Performance

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 1.645 | 2.378 | 0.724 |
| Ridge Regression | 1.639 | 2.372 | 0.726 |
| Lasso Regression | 1.573 | 2.317 | 0.738 |
| Random Forest | 1.201 | 2.015 | 0.802 |
| Gradient Boosting | 1.153 | 1.983 | 0.808 |

### Best Model

**Gradient Boosting Regressor**

R² Score: **0.808**

RMSE: **1.983**

MAE: **1.153**

## 🛠️ Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Matplotlib
- Seaborn

## 📁 Project Structure

```text
student-performance-prediction/
│
├── app.py
├── student_model.pkl
├── requirements.txt
├── Student_Performance_Prediction.ipynb
└── README.md
