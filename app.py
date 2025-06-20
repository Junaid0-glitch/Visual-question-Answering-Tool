import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from transformers import ViltProcessor, ViltForQuestionAnswering
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("HUGGINGFACE_TOKEN")

if not token:
    raise ValueError("HUGGINGFACE_TOKEN not found in environment")


st.set_page_config(layout="wide", page_title="VQA")

processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa", use_auth_token=token)
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa", use_auth_token=token)

def get_answer(image, text):
    try:
        img = Image.open(BytesIO(image)).convert("RGB")
        encoding = processor(img, text, return_tensors="pt")
        outputs = model(**encoding)
        logits = outputs.logits
        idx = logits.argmax(-1).item()
        answer = model.config.id2label[idx]
        return answer
    
    except Exception as e:
        return str(e)

st.title("Visual Question Answering Tool")
st.write("Upload an image and Ask the question about the image.")

col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
    if uploaded_file:
        st.image(uploaded_file, use_column_width=False)

with col2:
    question = st.text_input("Question")
    
    if st.button("Ask Question"):
        if uploaded_file and question:
            image = Image.open(uploaded_file)
            image_byte_array = BytesIO()
            image.save(image_byte_array, format='jpeg')
            image_bytes = image_byte_array.getvalue()

            answer = get_answer(image_bytes, question)
            st.info("Your question: "+ question)
            st.success("Answer: " + answer)
        else:
            st.warning("Please upload an image and enter a question.")