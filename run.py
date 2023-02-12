#pip install streamlit
import streamlit as st

# to run
# streamlit run run.py

def calculate_bmi(height, weight):
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal weight"
    elif bmi >= 25 and bmi < 30:
        return "Overweight"
    else:
        return "Obese"

st.title("BMI Calculator")

height = st.number_input("Enter your height in meters:")
weight = st.number_input("Enter your weight in kilograms:")

if st.button("Calculate"):
    bmi = calculate_bmi(height, weight)
    bmi_cat = bmi_category(bmi)
    result = "Your BMI is: " + str(bmi) + "\n" + "Your BMI category is: " + bmi_cat
    st.success(result)
