#!/usr/bin/env python
# coding: utf-8




import numpy as np 

import pandas as pd 



import streamlit as st 
import pickle
from sklearn import svm
from pickle import dump
from pickle import load

st.title(':black[Bankruptcy-Detection]')

st.sidebar.header('User Input Parameters')

def user_input_features():
    return features
df = user_input_features()
st.subheader('User Input parameters')
st.write(df)

# load the model from disk
model = load(open("test.pkl", 'rb'))
prediction = model.predict(df)
st.subheader('Predicted Result')
st.subheader('Detected As')

st.write('Yes' if prediction ==1.0 else 'No')
st.subheader('This Means')
st.write('Bankruptcy Detected' if prediction ==1.0 else 'Non-Bankruptcy Detected')


# In[ ]:
