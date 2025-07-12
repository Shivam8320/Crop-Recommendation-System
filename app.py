import streamlit as st
import pickle
import numpy as np
import base64

# Set background image
def set_bg(image_path):
    with open(image_path, "rb") as f:
        img = f.read()
    b64 = base64.b64encode(img).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{b64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;           
        }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

set_bg("bg.jpg")

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("model_scaler.pkl", "rb"))

crop_dict = {
    1: 'rice', 2: 'maize', 3: 'jute', 4: 'cotton', 5: 'coconut', 6: 'papaya',
    7: 'orange', 8: 'apple', 9: 'muskmelon', 10: 'watermelon', 11: 'grapes',
    12: 'mango', 13: 'banana', 14: 'pomegranate', 15: 'lentil', 16: 'blackgram',
    17: 'mungbean', 18: 'mothbeans', 19: 'pigeonpeas', 20: 'kidneybeans',
    21: 'chickpea', 22: 'coffee'
}

st.markdown("<h1 style='text-align: center; white-space: nowrap; color: white;'>🌾 Crop Recommendation System 🌾</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>Enter soil & weather details to get best crop suggestion.</p>", unsafe_allow_html=True)

# Inputs inside visual card
N = st.number_input("Nitrogen (N)", 0.0, 150.0, 50.0)
P = st.number_input("Phosphorus (P)", 0.0, 150.0, 50.0)
K = st.number_input("Potassium (K)", 0.0, 150.0, 50.0)
temperature = st.number_input("Temperature (°C)", 0.0, 50.0, 25.0)
humidity = st.number_input("Humidity (%)", 0.0, 100.0, 70.0)
ph = st.number_input("pH value", 0.0, 14.0, 6.5)
rainfall = st.number_input("Rainfall (mm)", 0.0, 300.0, 100.0)


# Predict button
if st.button("Recommend Crop"):
    features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    scaled = scaler.transform(features)
    pred = model.predict(scaled)[0]
    crop = crop_dict.get(int(pred), "Unknown")
    st.success(f"✅ The recommended crop to grow is: **{crop.capitalize()}**")
