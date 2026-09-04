
import streamlit as st
import pandas as pd
import joblib

# Load trained model
loaded_model = joblib.load("/content/student_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Performance Prediction")
st.write("Enter student information to predict the final grade (G3).")

# -----------------------------
# Student Inputs
# -----------------------------

school = st.selectbox("School", ["GP", "MS"])

sex = st.selectbox("Sex", ["F", "M"])

age = st.number_input(
    "Age",
    min_value=15,
    max_value=25,
    value=17
)

address = st.selectbox("Address", ["U", "R"])

famsize = st.selectbox("Family Size", ["LE3", "GT3"])

Pstatus = st.selectbox("Parent Status", ["T", "A"])

Medu = st.selectbox("Mother Education", [0, 1, 2, 3, 4])

Fedu = st.selectbox("Father Education", [0, 1, 2, 3, 4])

Mjob = st.selectbox(
    "Mother Job",
    ["teacher", "health", "services", "at_home", "other"]
)

Fjob = st.selectbox(
    "Father Job",
    ["teacher", "health", "services", "at_home", "other"]
)

reason = st.selectbox(
    "Reason for Choosing School",
    ["home", "reputation", "course", "other"]
)

guardian = st.selectbox(
    "Guardian",
    ["mother", "father", "other"]
)

traveltime = st.selectbox(
    "Travel Time",
    [1, 2, 3, 4]
)

studytime = st.selectbox(
    "Study Time",
    [1, 2, 3, 4]
)

failures = st.selectbox(
    "Past Failures",
    [0, 1, 2, 3]
)

schoolsup = st.selectbox(
    "School Support",
    ["yes", "no"]
)

famsup = st.selectbox(
    "Family Support",
    ["yes", "no"]
)

paid = st.selectbox(
    "Extra Paid Classes",
    ["yes", "no"]
)

activities = st.selectbox(
    "Extra Activities",
    ["yes", "no"]
)

nursery = st.selectbox(
    "Attended Nursery",
    ["yes", "no"]
)

higher = st.selectbox(
    "Wants Higher Education",
    ["yes", "no"]
)

internet = st.selectbox(
    "Internet Access",
    ["yes", "no"]
)

romantic = st.selectbox(
    "Romantic Relationship",
    ["yes", "no"]
)

famrel = st.selectbox(
    "Family Relationship Quality",
    [1, 2, 3, 4, 5]
)

freetime = st.selectbox(
    "Free Time",
    [1, 2, 3, 4, 5]
)

goout = st.selectbox(
    "Going Out",
    [1, 2, 3, 4, 5]
)

Dalc = st.selectbox(
    "Workday Alcohol Consumption",
    [1, 2, 3, 4, 5]
)

Walc = st.selectbox(
    "Weekend Alcohol Consumption",
    [1, 2, 3, 4, 5]
)

health = st.selectbox(
    "Health Status",
    [1, 2, 3, 4, 5]
)

absences = st.number_input(
    "Absences",
    min_value=0,
    max_value=100,
    value=5
)

G1 = st.number_input(
    "First Period Grade (G1)",
    min_value=0,
    max_value=20,
    value=10
)

G2 = st.number_input(
    "Second Period Grade (G2)",
    min_value=0,
    max_value=20,
    value=10
)

# -----------------------------
# Create Input DataFrame
# -----------------------------

input_data = pd.DataFrame({
    "school": [school],
    "sex": [sex],
    "age": [age],
    "address": [address],
    "famsize": [famsize],
    "Pstatus": [Pstatus],
    "Medu": [Medu],
    "Fedu": [Fedu],
    "Mjob": [Mjob],
    "Fjob": [Fjob],
    "reason": [reason],
    "guardian": [guardian],
    "traveltime": [traveltime],
    "studytime": [studytime],
    "failures": [failures],
    "schoolsup": [schoolsup],
    "famsup": [famsup],
    "paid": [paid],
    "activities": [activities],
    "nursery": [nursery],
    "higher": [higher],
    "internet": [internet],
    "romantic": [romantic],
    "famrel": [famrel],
    "freetime": [freetime],
    "goout": [goout],
    "Dalc": [Dalc],
    "Walc": [Walc],
    "health": [health],
    "absences": [absences],
    "G1": [G1],
    "G2": [G2]
})

# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict Performance"):

    prediction = loaded_model.predict(input_data)

    st.success(
        f"Predicted Final Grade: {prediction[0]:.2f}"
    )
