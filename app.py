import requests
import streamlit as st
import time
import json
import boto3
import os

def predict(filename):
    API_URL = 'https://6sirzw2h54.execute-api.us-east-2.amazonaws.com/production/predict-pneumonia'
    
    payload = filename
    headers = {
        'Content-Type': 'application/x-image'
    }
    response = requests.request('POST', API_URL, headers = headers, data = payload)
    return response.text


if __name__ == "__main__":
    st.title("Hot Dog Or Not Hot Dog")
    file = st.file_uploader("Upload an image")

    if file is not None:
        st.image(file)
        st.header(predict(file))


