#!/usr/bin/env python
# coding: utf-8




import numpy as np 
np.bool = np.bool_
np.int = np.int_
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import string
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import f1_score, confusion_matrix, accuracy_score, classification_report
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score
from sklearn.metrics import confusion_matrix as cm, accuracy_score as ac, classification_report as report,roc_curve, roc_auc_score , recall_score , precision_score, f1_score
from sklearn.metrics import zero_one_loss
from mlxtend.evaluate import bias_variance_decomp
import pickle as pickle
import warnings
warnings.filterwarnings('ignore')
import streamlit as st 
import pickle
from pathlib import Path
from sklearn.naive_bayes import GaussianNB
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