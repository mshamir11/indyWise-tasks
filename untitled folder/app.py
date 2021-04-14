# import os
import cv2
from PIL import Image
import tensorflow as tf
import numpy as np
import streamlit as st
import requests

## CONFIG

MODEL_FILE = 'model.h5'


st.title('Car and Truck Classifier')
st.text('Provide URL of image for classification')
def load_model(model_path):
  model = tf.keras.models.load_model(model_path)
  return model

with st.spinner('Loading Model into Memory.........'):
  model=load_model(MODEL_FILE)


classes = ['car','truck']

def image_resize(image):
  resized_image = cv2.resize(np.asarray(image)/255.0, (224, 224), 
                          interpolation=cv2.INTER_NEAREST)
  
  return resized_image

def decode_image(image):
 
  img = image_resize(image)
  return np.expand_dims(img,axis=0)

url =st.text_input('Enter Image URL to classify..')


st.header("OR")
st.text('Upload an image')

uploaded_file = st.file_uploader("Choose an image...")

if uploaded_file is not None:
    content = Image.open(uploaded_file)
    st.image(content, caption='Uploaded Image.', use_column_width=True)

    with st.spinner('Classifying'):
      label = np.argmax(model.predict(decode_image(content)),axis=1)
      st.header(f"The image is of a {classes[label[0]]}")


if url:
  content = Image.open(requests.get(url, stream=True).raw)
  st.image(content,use_column_width=True)
  


  with st.spinner('Classifying'):
    label = np.argmax(model.predict(decode_image(content)),axis=1)
    st.header(f"The image is of a {classes[label[0]]}")

  
