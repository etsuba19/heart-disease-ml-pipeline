# Heart Disease Prediction System 

This project implements an end-to-end machine learning pipeline for predicting heart disease risk using clinical data. The trained models are deployed as a web application using Django.

---

## Dataset
- **Source:** Kaggle – Heart Disease Dataset
- The dataset contains patient health indicators such as age, blood pressure, cholesterol, ECG results, and exercise-related features.

---

## Models Used
Two machine learning models were trained on the same dataset using a unified preprocessing pipeline:
- **Logistic Regression**
- **Decision Tree Classifier**

---

## Model Evaluation
The models were evaluated using:
- Accuracy
- Precision
- Recall
- F1-score

Logistic Regression demonstrated more stable and consistent performance, while the Decision Tree provided interpretability at the cost of slightly lower generalization.

---

## Machine Learning Pipeline
The ML pipeline includes:
- Data cleaning and preprocessing
- Categorical feature encoding
- Feature scaling
- Train-test split
- Model training and evaluation
- Model serialization using `joblib`

The training and evaluation process is documented in the `ml_pipeline/heart_disease_pipeline.ipynb` notebook.

---

## Web Application
The trained models were integrated into a Django backend that exposes REST endpoints for prediction. A simple frontend interface allows users to input clinical features and receive prediction results.

### Features
- Selectable prediction model (Logistic Regression or Decision Tree)
- Probability-based prediction output
- Clean and responsive UI

---

## Deployment
The application is deployed as a web service and can be accessed using the link below:

**Live Demo:** *(add deployment link here)*

---

## Disclaimer
This project is intended for **educational purposes only** and should not be used for medical diagnosis or treatment.

---

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Django
- Joblib
- HTML, CSS, JavaScript
