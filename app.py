import requests
import streamlit as st
from streamlit.components.v1 import html
from PIL import Image



def predict(filename):
    API_URL = "https://img.freepik.com/premium-vector/hotdog-pattern-background-food-vector-illustration_463676-5.jpg?w=1380"
    
    payload = filename
    headers = {
        'Content-Type': 'application/x-image'
    }
    response = requests.request('POST', API_URL, headers = headers, data = payload)
    return response.text



if __name__ == "__main__":

    with open('style.css') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

    file = st.file_uploader("Upload an image")

    if file is not None:
        col1, col2 = st.columns(2)
        col1.image(file, use_column_width = None)
        col2.metric("Hot Dog 🌭", 2, 4)
        col2.metric("Not Hot Dog 🥸", 2, 4)
        col2.write("I don't know what that is 🥸. It's not a hot dog")
        st.header(predict(file))


