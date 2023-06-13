#"C:\Users\aziba\Jupyter Notebook\ML - Group Project\"
import joblib
import streamlit as st
import pandas as pd
import numpy as np
from datetime import date, timedelta

le = joblib.load('le.h5')
model = joblib.load('model.h5')
fs = joblib.load('fs.h5')

input_ = {}

st.title('Career Fair Survey')
st.markdown('Help us help you finding your dream job! Complete this survey for your future employer reference!')

st.header('Personal Information')
input_['id'] = st.text_input('Name:')
input_['gender'] = st.radio('Gender:', ['Female', 'Male'])
input_['age'] = st.date_input('Birth Date:', min_value=date.today()-timedelta(hours=10512000), max_value=date.today())
input_['education_level'] = st.selectbox('Education level:', ['Certificate', 'Diploma', 'Bachelor', 'Master', 'PhD'])
input_['relationship_status'] = st.radio('Relationship Status:', ['Married', 'Single'])
input_['hometown'] = st.text_input('City of Origin:')
input_['time_of_service'] = st.number_input('Working Experience (Year):', min_value=0, step=1)
input_['time_since_promotion'] = st.date_input('Date Since Last Promotion:')
input_['decision_skill_possess'] = st.selectbox('Decision Skill:', ['Analytical', 'Behavioral', 'Conceptual', 'Directive'])

st.markdown('')

st.header('Job Expectation')
input_['unit'] = st.selectbox('Preferred Department:', ['Accounting and Finance', 'Human Resource Management', 'IT', 'Logistics', 'Marketing', 'Operarions', 'Production', 'Purchasing', 'Quality', 'R&D', 'Sales', 'Security'])
input_['growth_rate'] = st.slider('Growth Rate:')
input_['travel_rate'] = st.select_slider('Travel Rate:', range(0, 3))
input_['post_level'] = st.select_slider('Position Level:', range(1, 6))
input_['pay_scale'] = st.select_slider('Pay Scale:', range(1, 11))
input_['compensation_and_benefits'] = st.selectbox('Compensation and Benefit Expectation:', ['Salary Compensation', 'Salary and Commission Compensation', 'Hourly Compensation', 'Bonuses', 'Total Compensation'])
input_['work_life_balance'] = st.select_slider('Work-Life Balance:', range(1, 6))

predict = st.button('Submit')

if input_['gender'] == 'Female':
    input_['gender'] = 'F'
elif input_['gender'] == 'Male':
    input_['gender'] = 'M'

input_['age'] = date.today().year - input_['age'].year

if input_['education_level'] == 'Certificate':
    input_['education_level'] = 1
elif input_['education_level'] == 'Diploma':
    input_['education_level'] = 2
elif input_['education_level'] == 'Bachelor':
    input_['education_level'] = 3
elif input_['education_level'] == 'Master':
    input_['education_level'] = 4
elif input_['education_level'] == 'PhD':
    input_['education_level'] = 5

input_['time_since_promotion'] = date.today().year - input_['time_since_promotion'].year

if input_['compensation_and_benefits'] == 'Salary Compensation':
    input_['compensation_and_benefits'] = 'type0'
elif input_['compensation_and_benefits'] == 'Salary and Commission Compensation':
    input_['compensation_and_benefits'] = 'type1'
elif input_['compensation_and_benefits'] == 'Hourly Compensation':
    input_['compensation_and_benefits'] = 'type2'
elif input_['compensation_and_benefits'] == 'Bonuses':
    input_['compensation_and_benefits'] = 'type3'
elif input_['compensation_and_benefits'] == 'Total Compensation':
    input_['compensation_and_benefits'] = 'type4'

#st.write(input_)
    
if predict:
    input_df = pd.DataFrame()
    for c in input_:
        input_df[c] = [input_[c]]
    
    input_df = input_df[fs.columns]
    
    for c in input_df.columns:
        if c in le:
            input_df[c] = le[c].transform(input_df[c])
    
    attrition_rate = model.predict(input_df)
    
    st.write('Attrition Rate: '+str(attrition_rate*100))
