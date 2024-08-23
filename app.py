
'''
from flask import Flask, request, render_template, jsonify
import numpy as np
import pandas as pd
import logging
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline



# Initialize Flask application
application = Flask(__name__)
app = application

# Configure logging
logging.basicConfig(level=logging.INFO)

# Route for the home page
@app.route('/')
def index():
    return render_template('home.html')

# Route for predicting data
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            # Extract data from the form
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),
                writing_score=float(request.form.get('writing_score'))
            )
            
            # Convert to DataFrame
            pred_df = data.get_data_as_data_frame()
            logging.info(f"Prediction DataFrame: {pred_df}")

            # Create a prediction pipeline and get results
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            logging.info(f"Prediction results: {results}")

            return render_template('home.html', results=results[0])
        
        except Exception as e:
            logging.error(f"Error during prediction: {e}", exc_info=True)
            return render_template('home.html', error=str(e))

# Main entry point
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
'''


# STREAMLIT APP DEPLOYMENT
import streamlit as st
import pandas as pd
import logging
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Configure logging
logging.basicConfig(level=logging.INFO)

# Streamlit app title and layout
st.set_page_config(page_title="Student Performance Prediction", page_icon="📊", layout="wide")
st.markdown("""
    <style>
        /* Main background color */
        body {
            background-color: #f0f2f6;
        }

        /* Title styling */
        .title {
            font-family: 'Arial Black', sans-serif;
            color: #4e73df;
            text-align: center;
            padding: 20px;
        }

        /* Sidebar styling */
        .css-1v3fvcr {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
        }

        /* Button styling */
        .stButton > button {
            background-color: #4e73df;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #2e59d9;
            color: #ffffff;
        }

        /* Footer text */
        .footer {
            font-size: 14px;
            text-align: center;
            padding: 10px;
            margin-top: 20px;
            color: #888888;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown("<h1 class='title'>Student Performance Prediction App 📊</h1>", unsafe_allow_html=True)
st.subheader("An interactive app to predict student performance based on multiple factors.")

# Sidebar for user input
st.sidebar.header("Input Features")

# Function to gather input features
def user_input_features():
    gender = st.sidebar.selectbox('Gender', options=['male', 'female'])
    race_ethnicity = st.sidebar.selectbox('Race/Ethnicity', options=['group A', 'group B', 'group C', 'group D', 'group E'])
    parental_level_of_education = st.sidebar.selectbox('Parental Level of Education', options=[
        'some high school', 'high school', 'some college', 
        'associate\'s degree', 'bachelor\'s degree', 'master\'s degree'
    ])
    lunch = st.sidebar.selectbox('Lunch Type', options=['standard', 'free/reduced'])
    test_preparation_course = st.sidebar.selectbox('Test Preparation Course', options=['none', 'completed'])
    reading_score = st.sidebar.number_input('Reading Score', min_value=0, max_value=100, value=50)
    writing_score = st.sidebar.number_input('Writing Score', min_value=0, max_value=100, value=50)
    
    # Store inputs in a dictionary and return as a DataFrame
    data = {
        'gender': gender,
        'race_ethnicity': race_ethnicity,
        'parental_level_of_education': parental_level_of_education,
        'lunch': lunch,
        'test_preparation_course': test_preparation_course,
        'reading_score': reading_score,
        'writing_score': writing_score
    }
    features = pd.DataFrame(data, index=[0])
    return features

# Get user input
input_df = user_input_features()

# Display the user input for confirmation
st.write("### Input Data", input_df)

# Prediction logic
if st.button("Predict"):
    try:
        # Convert input DataFrame to a format suitable for prediction
        custom_data = CustomData(
            gender=input_df['gender'][0],
            race_ethnicity=input_df['race_ethnicity'][0],
            parental_level_of_education=input_df['parental_level_of_education'][0],
            lunch=input_df['lunch'][0],
            test_preparation_course=input_df['test_preparation_course'][0],
            reading_score=float(input_df['reading_score'][0]),
            writing_score=float(input_df['writing_score'][0])
        )

        # Get DataFrame for prediction
        pred_df = custom_data.get_data_as_data_frame()
        logging.info(f"Prediction DataFrame: {pred_df}")

        # Run prediction pipeline
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        logging.info(f"Prediction results: {results}")

        # Display the prediction result
        st.success(f"Predicted Math Score: {results[0]}")

    except Exception as e:
        logging.error(f"Error during prediction: {e}", exc_info=True)
        st.error(f"An error occurred: {e}")

# Footer or additional information
st.markdown("""
    <div class="footer">
        ---
        <br>
        **Note:** This prediction app is for educational purposes only.
    </div>
""", unsafe_allow_html=True)


st.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <div class='footer'>
        <div class="contact">
            <a target="_blank" href="https://www.linkedin.com/in/daniel-opoku-mensah-5b016a75/">
                <i class="fab fa-linkedin fa-lg contact-icon"></i>
            </a>
        </div>
        <p class='footer-description'>Made by Daniel Mensah.</p>
    </div>
    """,
    unsafe_allow_html=True
)







