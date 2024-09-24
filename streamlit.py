import streamlit as st
import requests
import json
# from textSummarizer.pipeline.prediction import PredictionPipeline
import sys

st.title("Dialogue Summarization application")

input_text = st.text_area('Dialogue to be summarized')

st.write("Select the max word for summarized output using the slider:")
min_words = st.slider("Min words", 0, 400, 5)
max_words = st.slider("Max words", 0, 500, 5)

# gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": max_words}
# inputs = {"max_words": max_words, "input_text": input_text}

# def summarize(text, min_length, max_length):
#     try:

#         obj = PredictionPipeline()
#         print(f"min_length: {min_length}")
#         print(f"max_length: {max_length}")
#         text = obj.predict(text, min_length, max_length)
#         return text
#     except Exception as e:
#         raise e
data = {'input_text': input_text, 'min_length':min_words, 'max_length':max_words}
if st.button('Summarize'):

    # res = summarize(input_text, max_words)
    res = requests.post('http://localhost:8080/predict', json=data)
    st.subheader(f"Summary: {res.text}")
    # st.subheader(f"Summarization: {res.text}")
