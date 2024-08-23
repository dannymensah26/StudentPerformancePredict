# STUDENT PERFORMANCE PREDICTION WEB APP

# Azure Deployment
1. Build Docker Image 
2. Container Registry
3. Azure Web app with container
4. Configured the GitHub deployment center




# Run from terminal

docker build -t testdockerdaniel.azurecr.io/studentpredict:latest .

docker login testdockerdaniel.azurecr.io

docker push  testdockerdaniel.azurecr.io/studentpredict:latest


# Docker Account
resource group: testdockerdaniel

registry name: testdockerdaniel


Login server: testdockerdaniel.azurecr.io

password: JAh7kD7ulKPt5xhriUtuuBqslkiis2JrszOnN8p1/s+ACRDrNq14


MaMu1Sc1Ver85jFtmLCoeqy8E+X0yVh02cCxSMEzCV+ACRCdjJw6


# Web App
Resource group:



## STUDENT PERFORMANCE PREDICTION DEPLOYMENT ON STREAMLIT APP

### Overview

A simple web application which uses Machine Learning algorithm to predict the heart condition of a person by providing some inputs about the person health like age, gender, blood pressure, cholesterol level etc built using streamlit and deployed on Streamlit.

### Motivation

As being a Data and ML enthusiast I have tried many different projects related to the subject but what I have realised is that Deploying your machine learning model is a key aspect of every ML and Data science project. Everything thing I had studied or been taught so far in my Data science and ML journey had mostly focused on defining problem statement followed by Data collection and preparation, model building and evaluation process which is of course important for every ML/DS project but what if I want different people to interact with my models, how can I make my model available for end-users? I can't send them jupyter notebooks right!. That's why I wanted to try my hands on complete end-to-end machine learning project.

    To View the Deployed Application, click on the link given below : Heart Disease Prediction App - https://heartdiseasepredict-nz8hrvjjkwcswccqmtm4yj.streamlit.app/

    To get the Code for Exploratory data analysis/visualisations, different algorithms used and the model evaluation, click on the link mentioned below : Link of jupyter notebook - 
EDA:
https://github.com/dannymensah26/HeartDiseasePredict/blob/main/notebook/EDA.ipynb

Model Building:
https://github.com/dannymensah26/HeartDiseasePredict/blob/main/notebook/ModelBuilding.ipynb


### A Demo of the Web App :

Heart_disease


#### Technical Aspect

This Project is mainly divided into two parts:

    Exploring the dataset and traning the model using Sklearn.
    Building and hosting a streamlit App on Streamlit

### About the repository Structure :

    Project consist app.py script which is used to run the application and is engine of this app. contians API that gets input from the user and computes a predicted value based on the model.
    prediction.py contains code to build and train a Machine learning model.
    templates folder contains two files main.html and result.html which describe the structure of the app and the way this web application behaves. These files are connected with Python via Flask framework.
    static folder contains file style.css which adds some styling and enhance the look of the application.

### Installation

The Code is written in Python 3.9. If you don't have Python installed you can find it here. If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after cloning the repository:

pip install -r requirements.txt 

To clone the repository

git clone https://github.com/dannymensah26/HeartDiseasePredict.git

### Run

To Run the Application

stream run app.py

### Deployement on Streamlit

Install Streamlit as this makes it easy to create and manage your Streamlit apps directly from the terminal. You can download it from here.

next step would be to follow the instruction given on Heroku Documentation to deploy a web app.


### Future work

    Improve model performance using Adaboost or XGBoost Gradient Algorithm
    Add more better styling to the user interface.

Some Useful Resources

    Streamlit Quickstart Documentation : https://docs.streamlit.io/


### Demo
https://github.com/user-attachments/assets/8ced7883-b7cd-49cf-814c-83f8108e9abd

### Build a Docker Container for the ML Model
 Create a Streamlit application to interact with the model.
 Deploy it on a Docker container.
