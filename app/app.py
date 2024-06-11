import streamlit as st
import pandas as pd
import joblib
import xgboost as xgb

# Load the model pipeline
model = joblib.load('model/model_pipeline.joblib')

# Streamlit app layout
st.title('Agronomic Decision Support System to Predict Optimal Fertilizer Amount')

# Create three columns
col1, col2, col3 = st.columns(3)

# Create three columns with equal width
col1, col2, col3 = st.columns([1, 1, 1])

# Soil Conditions
with col1:
    st.subheader('Soil Condition')
    soil_color = st.selectbox('Soil Color', ['light brown', 'dark brown', 'reddish'])
    soil_ph = st.slider('Soil pH', 1.0, 10.0, 6.5)
    soil_n = st.slider('Soil Nitrogen (ppm)', 0, 100, 30)
    soil_p = st.slider('Soil Phosphorus (ppm)', 0, 100, 40)

# Weather Conditions
with col2:
    st.subheader('Weather Condition')
    temp = st.slider('Temperature (°C)', 15, 50, 25)
    rainfall = st.slider('Rainfall (mm)', 0, 300, 100)
    forecast_temp = st.slider('Forecasted Temperature (°C)', 15, 50, 25)
    forecast_rainfall = st.slider('Forecasted Rainfall (mm)', 0, 300, 100)

# Crop Conditions
with col3:
    st.subheader('Crop Condition')
    crop_type = st.selectbox('Crop Type', ['wheat', 'corn', 'rice'])
    plant_health = st.selectbox('Plant Health', ['healthy', 'yellowing', 'wilting'])


# Make prediction
if st.button('Predict'):

    input_data = pd.DataFrame([{
        'soil_color': soil_color,
        'soil_ph': soil_ph,
        'soil_n': soil_n,
        'soil_p': soil_p,
        'temp': temp,
        'rainfall': rainfall,
        'forecast_temp': forecast_temp,
        'forecast_rainfall': forecast_rainfall,
        'crop_type': crop_type,
        'plant_health': plant_health
    }])
    
    prediction = model.predict(input_data)[0]

    st.success(f'Optimal Fertilizer Amount: {prediction:.2f} kg/ha')
