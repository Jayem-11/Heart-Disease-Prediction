import streamlit as st
import numpy as np # for numerical calculation
import pickle # Pickle is used for serializing and de-serializing a Python object structure
import requests
from sklearn.ensemble import RandomForestClassifier

st.write("""

# Heart Disease Prediction

""")

#Gender

st.write("""

## Gender

""")

input_gender = st.radio('Enter your Gender',['Male','Female'],index = 0)
gender_dict = {'Male': 1, 'Female': 0}
gender_value = gender_dict.get(input_gender)

# age

st.write("""
## Age
""")

input_age = st.slider('Select your age', value=42, min_value=1, max_value=150, step=1) 

# Current smoker

st.write("""

## Current Smoker

""")

input_smoker = st.radio('Are you a smoker',['Yes','No'],index = 0)
smoker_dict = {'Yes': 1, 'No': 0}
smoker_value = smoker_dict.get(input_smoker)

# Blood Pressure

st.write("""

## Blood Pressure

""")

blood_pressure = st.radio('Have you been on Blood Pressure medication?',['Yes','No'],index = 0)
pressure_dict = {'Yes': 1, 'No': 0}
pressure_value = pressure_dict.get(blood_pressure)


# cigsPerDay
st.write("""

## Cigarettes per day

""")

cig_no = st.slider('Number of cigarettes per day', value=15, min_value=0, max_value=50, step=1) 

# prevalentStroke
st.write("""

## Stroke

""")

stroke = st.radio('Have you ever had a stroke ?',['Yes','No'],index = 0)
stroke_dict = {'Yes': 1, 'No': 0}
stroke_value = stroke_dict.get(stroke)

# prevalentHyp
st.write("""

## Hypertensive

""")

hyp = st.radio('Do you have hypertension?',['Yes','No'],index = 0)
hyp_dict = {'Yes': 1, 'No': 0}
hyp_value = hyp_dict.get(hyp)

# diabetes 
st.write("""

## Diabetes

""")

diabetes = st.radio('Do you have diabetes?',['Yes','No'],index = 0)
diab_dict = {'Yes': 1, 'No': 0}
diab_value = diab_dict.get(diabetes)

# totChol
st.write("""

## Cholestrol level

""")

chol_lev = np.float(st.text_input('Enter your cholestrol level',0))

# sysBP
st.write("""

## Systolic Blood Pressure

""")

Sbp_lev = np.float(st.text_input('Enter your systolic blood pressure level level',0))

# diaBP
st.write("""

## Diastolic Blood Pressure

""")

Dbp_lev = np.float(st.text_input('Enter your diastolic blood pressure level',0))

# BMI
st.write("""

## Body Mass Index


""")
BMI = np.float(st.text_input('Enter your Body Mass Index',0))

# heartRate 

st.write("""

## Heart Rate

""")

H_rate = np.float(st.text_input('Enter your heart rate level',0))

# glucose

st.write("""

## Glucose level

""")

glucose = st.slider('Glucose level', value=100, min_value=1, max_value=200, step=1) 

st.markdown('##')
st.markdown('##')
# Button
predict_bt = st.button('Predict')

# ===========================================================================================================================

# list of all input variables

input_data = np.array([[   gender_value,
                                input_age,
                                smoker_value,
                                cig_no,
                                pressure_value,
                                stroke_value,
                                hyp_value,
                                diab_value,
                                chol_lev,
                                Sbp_lev,
                                Dbp_lev,
                                BMI,
                                H_rate,
                                glucose
                        ]])

# load the model
model =  pickle.load(open('finalized_model.sav', 'rb'))

def make_predictions():
    #predict
    return model.predict(input_data)


#Animation function
@st.experimental_memo
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


if predict_bt:

    result = make_predictions()

    if result[0] == 0:
        st.success('## Low risk of getting Cardiovascular diseases')
        st.balloons()
    elif result[0] == 1:
        st.error('## High risk of getting Cardiovascular disease')
