# Titanic Survival Prediction Web Application

This project features a machine learning-powered web application developed using a **Logistic Regression** model to predict whether a passenger would have survived the Titanic disaster. It takes into account various passenger attributes and provides an accessible tool for educational and analytical purposes.

---

### 🎯 Objective

The primary goal of this application is to provide an intuitive and interactive platform that leverages predictive modeling to estimate the survival chances of a Titanic passenger based on demographic and travel-related details. The application is user-friendly, responsive, and suitable for demonstrations and academic learning.

---

### 🌐 Live Demo

Access the deployed application here:  
🔗 [Titanic Survival Prediction App – Streamlit](#) *('https://titanic-survival-prediction-saee-surve.streamlit.app/')*

---

### 🧪 Model Overview

- **Algorithm Used**: Logistic Regression  
- **Accuracy Achieved**: **81.00%** on test data  
- **Input Features**: 8 passenger-related features  
- **Model File**: Includes a trained model serialized using `joblib` (`titanic_model.joblib`)

---

### 📊 Dataset

- **Source**: Kaggle  
- **Dataset Name**: Titanic Dataset  
- **Link**: [https://www.kaggle.com/datasets/yasserh/titanic-dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset)

The dataset includes the following features:
- **Pclass**: Passenger class (1 = 1st, 2 = 2nd, 3 = 3rd)  
- **Sex**: Gender (male, female)  
- **Age**: Age in years  
- **SibSp**: Number of siblings/spouses aboard  
- **Parch**: Number of parents/children aboard  
- **Fare**: Ticket fare  
- **Embarked**: Port of embarkation (S = Southampton, C = Cherbourg, Q = Queenstown)

---

### 🛠️ Tech Stack

- **Frontend & Deployment**: Streamlit  
- **Machine Learning**: Scikit-learn (Logistic Regression, preprocessing)  
- **Programming Language**: Python  
- **Data Handling**: Pandas, NumPy  
- **Model Serialization**: Joblib

---

### 📁 Repository Contents

- `app.py` – Streamlit web application  
- `titanic_model.joblib` – Trained Logistic Regression model  
- `titanic.csv` – Titanic dataset (original or preprocessed version)  
- `requirements.txt` – Python dependencies required for deployment

---

### 📌 How It Works

1. The user enters details like class, sex, age, ticket fare, and embarkation point.  
2. The input is preprocessed to match the training data format.  
3. The trained logistic regression model predicts the survival outcome.  
4. The result is displayed in a **green block** (Survived) or **red block** (Not Survived) with intuitive messages.

---

### ✔️ Advantages

- Clean and interactive UI for smooth user experience  
- Real-time predictions with high responsiveness  
- Based on historical data from a globally known dataset  
- Demonstrates a practical application of logistic regression

---

### ⚠️ Disclaimer

This project is intended for **educational and demonstration** purposes only. It should not be interpreted as an official survival predictor or decision-making tool.
