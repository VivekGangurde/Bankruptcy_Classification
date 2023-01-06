#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import streamlit as st
import numpy as np
import pickle
from sklearn.naive_bayes import GaussianNB
from pickle import dump
from pickle import load


st.title(':black[Bankruptcy-Detection]')

st.sidebar.header('User Input Parameters')

def user_input_features():
    Industrial = st.sidebar.selectbox('Industrial',('1.0','0.5','0.0'))
    Management = st.sidebar.selectbox('Management',('1.0','0.5','0.0'))
    Financial = st.sidebar.selectbox('Financial',('1.0','0.5','0.0'))
    Credibility	= st.sidebar.selectbox('Credibility',('1.0','0.5','0.0'))
    Competitive = st.sidebar.selectbox('Competitive',('1.0','0.5','0.0'))
    Operational = st.sidebar.selectbox('Operational',('1.0','0.5','0.0'))
    data = {'Management':Management,
            ' Financial': Financial,
            'Credibility':Credibility,
            'Competitive':Competitive,
            'Industrial':Industrial,
            'Operational':Operational}
    features = pd.DataFrame(data, index=[0])
    return features
df = user_input_features()
st.subheader('User Input parameters')
st.write(df)

# load the model from disk
model = load(open("bank_cl.pkl", 'rb'))
prediction = model.predict(df)
st.subheader('Predicted Result')
st.subheader('Detected As')

st.write('Yes' if prediction ==1.0 else 'No')
st.subheader('This Means')
st.write('Bankruptcy Detected' if prediction ==1.0 else 'Non-Bankruptcy Detected')


# In[ ]:




