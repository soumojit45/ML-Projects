import streamlit as st
import pandas as pd
import pickle

# ---------- Page Setup ----------
st.set_page_config(page_title="Car Price Predictor", page_icon="🚗", layout="centered")
st.title("🚘 Car Price Prediction App")
st.write("Enter the car specifications below to predict its price.")
# ---------- Load Trained Model ----------
model = pickle.load(open('CarModel.pkl', 'rb'))

# ---------- User Input Section ----------
st.subheader("Enter Car Details:")

symboling = st.number_input("Symboling", min_value=-3, max_value=3, value=0)
carbody = st.selectbox("Car Body", ["convertible", "hatchback", "sedan", "wagon", "hardtop"])
enginelocation = st.selectbox("Engine Location", ["front", "rear"])
carwidth = st.number_input("Car Width (in inches)", min_value=50.0, max_value=75.0, value=64.0)
enginesize = st.number_input("Engine Size (cc)", min_value=50, max_value=400, value=130)
stroke = st.number_input("Stroke", min_value=2.0, max_value=5.0, value=3.0)
compressionratio = st.number_input("Compression Ratio", min_value=7.0, max_value=25.0, value=9.0)
peakrpm = st.number_input("Peak RPM", min_value=4000, max_value=7000, value=5000)

# ---------- Prepare Input for Prediction ----------
# You must encode categorical values the same way as during training
carbody_map = {'convertible': 0, 'hatchback': 1, 'sedan': 2, 'wagon': 3, 'hardtop': 4}
enginelocation_map = {'front': 0, 'rear': 1}

input_data = pd.DataFrame([[
    symboling,
    carbody_map[carbody],
    enginelocation_map[enginelocation],
    carwidth,
    enginesize,
    stroke,
    compressionratio,
    peakrpm
]], columns=['symboling', 'carbody', 'enginelocation', 'carwidth', 'enginesize', 'stroke', 'compressionratio', 'peakrpm'])

# ---------- Prediction ----------
if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Predicted Car Price: ${prediction:,.2f}")
