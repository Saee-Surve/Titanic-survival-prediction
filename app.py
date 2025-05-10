import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load('titanic_model.joblib')

# Streamlit app header with dynamic title animation
st.set_page_config(page_title="Titanic Survival Prediction", page_icon="🚢", layout="centered")
st.markdown("""
    <style>
        .title {
            font-size: 48px;
            color: #ff6347;
            font-weight: bold;
            text-align: center;
            animation: fadeIn 3s ease-in-out;
        }
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
        .stButton>button {
            background-color: #ff6347;
            color: white;
            font-size: 16px;
            padding: 12px 28px;
            border-radius: 12px;
            border: none;
            transition: background-color 0.3s;
        }
        .stButton>button:hover {
            background-color: #ff4500;
        }
        .input-box {
            background-color: rgba(255, 255, 255, 0.7);
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.2);
            margin-top: 30px;
        }
        .description {
            color: #444;
            font-size: 18px;
            line-height: 1.6;
        }
        .result-survived {
            font-size: 24px;
            font-weight: bold;
            color: #32cd32;
            text-align: center;
            padding: 20px;
            border-radius: 12px;
            background-color: #eaffea;
        }
        .result-not-survived {
            font-size: 24px;
            font-weight: bold;
            color: #ff6347;
            text-align: center;
            padding: 20px;
            border-radius: 12px;
            background-color: #ffe0e0;
        }
        .footer {
            text-align: center;
            font-size: 14px;
            margin-top: 50px;
            color: #888;
        }
    </style>
""", unsafe_allow_html=True)

# Header Title with Animation
st.markdown('<div class="title">Titanic Survival Prediction</div>', unsafe_allow_html=True)

# Description and Input Field Instructions
st.markdown("""
This app uses a **logistic regression** model to predict whether a passenger survived or not on the Titanic.
Please fill in the details below to get your prediction. Below are the acceptable ranges for each input field.
Make sure to enter values accordingly for accurate predictions.

### Input Field Descriptions and Ranges:

- **Pclass**: The class of the passenger (1, 2, or 3). 1 is 1st class (wealthiest), 3 is 3rd class (poorest).
- **Sex**: Gender of the passenger, either **male** or **female**.
- **Age**: The age of the passenger. Valid range: **0 to 100** years.
- **SibSp**: Number of siblings or spouses aboard the Titanic. Valid range: **0 to 10**.
- **Parch**: Number of parents or children aboard the Titanic. Valid range: **0 to 10**.
- **Fare**: The amount the passenger paid for the ticket. Valid range: **0.0 to 500.0**.
- **Embarked**: The port where the passenger boarded the Titanic. Choose from:
    - **S**: Southampton
    - **C**: Cherbourg
    - **Q**: Queenstown
""", unsafe_allow_html=True)

# Input form for passenger data in an attractive container
with st.form(key='titanic_form', clear_on_submit=True):
    st.markdown('<div class="input-box">', unsafe_allow_html=True)
    
    st.subheader("Enter Passenger Details")

    # Pclass (Passenger Class)
    pclass = st.selectbox(
        "Pclass (Class of Passenger)",
        [1, 2, 3],
        help="Class of the passenger. Options: 1 (1st class), 2 (2nd class), 3 (3rd class)."
    )
    
    # Sex
    sex = st.selectbox(
        "Sex (Gender of Passenger)",
        ["male", "female"],
        help="Select the gender of the passenger. Options: male or female."
    )
    
    # Age
    age = st.number_input(
        "Age (Age of Passenger)",
        min_value=0,
        max_value=100,
        value=22,
        help="Age should be between 0 and 100. Enter the passenger's age in years."
    )
    
    # SibSp (Number of Siblings/Spouses Aboard)
    sibsp = st.number_input(
        "SibSp (Number of Siblings/Spouses Aboard)",
        min_value=0,
        max_value=10,
        value=1,
        help="Number of siblings or spouses aboard. Valid range: 0 to 10."
    )
    
    # Parch (Number of Parents/Children Aboard)
    parch = st.number_input(
        "Parch (Number of Parents/Children Aboard)",
        min_value=0,
        max_value=10,
        value=0,
        help="Number of parents or children aboard. Valid range: 0 to 10."
    )
    
    # Fare
    fare = st.number_input(
        "Fare (Ticket Fare)",
        min_value=0.0,
        max_value=500.0,
        value=7.25,
        step=0.01,
        help="Fare for the passenger. Valid range: 0.0 to 500.0. Enter the amount paid for the ticket."
    )
    
    # Embarked (Port of Embarkation)
    embarked = st.selectbox(
        "Embarked (Port of Embarkation)",
        ["S", "C", "Q"],
        help="Port where the passenger boarded. Options: S (Southampton), C (Cherbourg), Q (Queenstown)."
    )
    
    # Submit button
    submit_button = st.form_submit_button("Predict Survival")
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close input box

# When user submits the form, make prediction
if submit_button:
    # Prepare the input data in the same format as during training
    input_data = {
        "Pclass": [pclass],
        "Age": [age],
        "SibSp": [sibsp],
        "Parch": [parch],
        "Fare": [fare],
        "Sex_male": [1 if sex == "male" else 0],
        "Embarked_Q": [1 if embarked == "Q" else 0],
        "Embarked_S": [1 if embarked == "S" else 0],
    }
    input_df = pd.DataFrame(input_data)

    # Prediction
    prediction = model.predict(input_df)
    
    # Display result with custom styling
    if prediction == 1:
        st.markdown('<div class="result-survived">The passenger survived the Titanic disaster! 🎉</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-not-survived">The passenger did not survive the Titanic disaster. 😞</div>', unsafe_allow_html=True)
    
    # Footer with your name and GitHub link
    st.markdown("""
    ---
    This app was developed as a **Streamlit** app to predict Titanic survival chances.
    You can find the source code on [GitHub](https://github.com/Saee-Surve/Titanic-survival-prediction).
    
    Made with ❤️ by **Saee Surve**.
""")
