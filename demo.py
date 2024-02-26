
import numpy as np
from joblib import load
import streamlit as st
import sys
sys.path.append(r'C:/Users/MSI/OneDrive/Python/Recommended Topic Hashtaq/Recommend-Topic-Hashtags/data_preprocessing')
from data_preprocessing import preprocessing
import pandas as pd

model_load= load('trained_.joblib')
scaler_load = load('scaler.joblib')
Classes = ['#Q&A', '#cv', '#data', '#deep_learning', '#machine_learning', '#math', '#nlp', '#python', '#sharing']


st.title(":blue[HASHTAG RECOMMENDATION]")    
st.subheader(":green[Python, Data Science, Machine Learning, Deep Learning]")
post = st.text_area('Nội dung bài đăng 👉', height=200)
option = st.selectbox(
   "Chọn Model",
   ("SVM"),
   index=None,
   placeholder="Chọn model . . .",
)


def predict_label(array):
    
    selected_classes_indices = np.where(array == 1)[1]
    selected_classes = [Classes[index] for index in selected_classes_indices]
    return selected_classes
    
if post:
    if option == 'SVM':
        post = preprocessing(post)
        post_scaled = scaler_load.transform([post])
        predict = model_load.predict(post_scaled)
        st.write('Hashtag recommendation : ')
        for item in range(len(predict_label(predict))):
            st.write(item+1  , predict_label(predict)[item])
    else:
       st.write('Vui lòng chọn model ')