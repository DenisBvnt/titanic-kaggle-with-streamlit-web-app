# IMPORTING LIBS AND MODEL
import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open('titanic_model_svm.sav', 'rb'))


# DATA INPUT
st.image('imgs/titanic.jpg')
st.title("Titanic - Prediction of survival")
name = st.text_input('Name')
last_name = st.text_input('Last Name')
title = st.selectbox('Title', ('Mrs', 'Miss', 'Master', 'Mr', 'Other'))
sex = st.radio("Sex", ('Male', 'Female'))
age = st.slider('Age', 0.0, 130.0, 25.0)
embarked = st.selectbox('Embarked in', ('Cherbourg', 'Queenstown', 'Southampton'))
psg_class = st.selectbox('Class', (1,2,3))
cabin = st.text_input('Cabin')
ticket = st.text_input('Ticket')
fare = st.slider('Fare', 0.0, 513.0, 15.0)
sibsp = st.number_input("Number of siblings/spouses aboard the Titanic", value=0, min_value=0, step=1)
parch = st.number_input("Number of parents/children aboard the Titanic", value=0, min_value=0, step=1)

# DATA TREATMENT
sex = 1 if sex == "Male" else 0
embarked = 0 if embarked == "Cherbourg" else 2 if embarked == "Southampton" else 1
isAlone = 1 if (sibsp + parch) == 0 else 0

if title == "Mr":
    title = 2
elif title == "Mrs":
    title = 3
elif title == "Miss":
    title = 1
elif title == "Master":
    title = 0
else:
    title = 4
    
if fare > 31.0:
    fare = 3
elif fare > 14.454:
    fare = 2
elif fare > 7.91:
    fare = 1
else:
    fare = 0

if age > 64.0:
    age = 4
elif age > 48.0:
    age = 3
elif age > 32.0:
    age = 2
elif age > 16.0:
    age = 1
else:
    age = 0


# PREDICTION
btn_predict = st.button("Predict")
if btn_predict:
    result = model.predict([[psg_class,sex,embarked,age,fare,title,isAlone]])
    st.subheader("The passenger is... ")
    result = "Survived" if result == 1 else "Died"
    st.write(result)