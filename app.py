import streamlit as st
import os
from PIL import Image
from model import get_caption_model, generate_caption


@st.cache(allow_output_mutation=True)
def get_model():
    return get_caption_model()


caption_model = get_model()

st.title("Image Caption Generator")
uploaded_file = st.file_uploader("Upload an Image")

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img)
    img.save("image.jpg")
    pred_caption = generate_caption("image.jpg", caption_model)
    st.write(pred_caption)
    os.remove("image.jpg")
