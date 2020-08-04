import streamlit as st
import numpy as np
import pandas as pd
import pickle

model=pickle.load(open('model.pkl', 'rb'))

@st.cache
def load_data():
    data = pd.read_csv('diabetes.csv')
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    # data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


def predict_diabetes(pregnancy, glucose, bp, skin_thickness, insulin, bmi, dpf, age):
	prediction=model.predict([[pregnancy, glucose, bp, skin_thickness, insulin, bmi, dpf, age]])
	if prediction==1:
		return "<h4 style='color: red;'>You suffer from diabetes!</h4>"
	else:
		return "<h4 style='color: green'>You do not have diabetes!</h4>"


def main():
	st.markdown('<center><h2>Diabetes Prediction</h2></center>', unsafe_allow_html=True)

	pregnancy=st.text_input('Pregnancies')
	glucose=st.text_input('Glucose')
	bp=st.text_input('Blood Pressure')
	skin_thickness=st.text_input('Skin Thickness')
	insulin=st.text_input('Insulin')
	bmi=st.text_input('BMI (Body Mass Index)')
	dpf=st.text_input('Diabetes Pedigree Function')
	age=st.text_input('Age')

	if st.button('Predict'):
		st.markdown(predict_diabetes(pregnancy, glucose, bp, skin_thickness, insulin, bmi, dpf, age), unsafe_allow_html=True)


if __name__=='__main__':
	main()