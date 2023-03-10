import requests
import streamlit as st
import codecs
from streamlit.components.v1 import html
from PIL import Image
from bs4 import BeautifulSoup




def predict(filename):
    API_URL = "https://hc6spzm2vl.execute-api.us-east-2.amazonaws.com/production/predict-hotdog"
    
    payload = filename
    headers = {
        'Content-Type': 'application/x-image'
    }
    response = requests.request('POST', API_URL, headers = headers, data = payload)
    return response.text



if __name__ == "__main__":

    with open('./src/style.css') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
    

    file = st.file_uploader("Upload an image")
    
    
    if file is not None:
        prediction = predict(file).strip('\"')
        col1, col2 = st.columns(2)
        image = Image.open(file)
        image = image.resize((1000,1000))
        col1.image(image, use_column_width = None)
        print(prediction)
        if prediction == "Hotdog":
            image = Image.open('./images/check_emoji.png')
            col2.image(image, use_column_width = None)
            #st.write(prediction)
        else:
            image = Image.open('./images/x_emoji.png')
            col2.image(image, use_column_width = None)
            #st.write(prediction)


