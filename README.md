
## STUDENT PERFORMANCE PREDICTION DEPLOYMENT ON STREAMLIT APP

### Overview

A simple web application that employs a Machine Learning algorithm to predict the performance of a student based on inputs such as race/ethnicity, parental level of education, lunch type, test preparation course, reading score, and so on, created with Streamlit and deployed on the Streamlit app.

### Motivation

Enthusiastic in data and machine learning, I have worked on several projects mostly emphasizing data preparation, model construction, issue specification, and assessment.While these are necessary procedures, I discovered that deploying models is critical for allowing others to engage with them. Sharing Jupyter notebooks is impractical for end users, so I wanted to investigate distributing models as part of an end-to-end ML project, making them more available to a wider audience.

    To View the Deployed Application, click on the link given below : Heart Disease Prediction App - https://heartdiseasepredict-nz8hrvjjkwcswccqmtm4yj.streamlit.app/

    To get the Code for Exploratory data analysis/visualisations, different algorithms used and the model evaluation, click on the link mentioned below : 
#### Link of jupyter notebook:
EDA:
https://github.com/dannymensah26/StudentPerformancePredict/blob/main/notebook/EDA%20STUDENT%20PERFORMANCE%20.ipynb


Model Building:
https://github.com/dannymensah26/StudentPerformancePredict/blob/main/notebook/MODEL%20TRAINING.ipynb


#### Technical Aspect

This Project is mainly divided into two parts:

    Exploring the dataset and traning the model using Sklearn.
    Building and hosting a streamlit App on Streamlit
    Building a Docker Container for the ML Model
    Deploying the model on Streamlit

### About the repository Structure

    The structure of the repository include the following:
    (i) app.py script which is used to run the application and is engine of this app. It contians API that gets input from the user and computes a predicted value based on the model.
    (ii) prediction.py contains code to build and train a Machine learning model.
    (iii) templates folder contains two files main.html and result.html which describe the structure of the app and the way this web application behaves. These files are connected with Python via Flask framework.
    (iv) static folder contains file style.css which adds some styling and enhance the look of the application.

### Installation

    The Code is written in Python 3.9. If you don't have Python installed you can find it here. If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip.      To install the required packages and libraries, run this command in the project directory after cloning the repository:

    pip install -r requirements.txt 


### Clone Repository  
    To clone the repository
    git clone https://github.com/dannymensah26/StudentPerformancePredict.git


### Run on Local Host
 To run the application use:
 
    stream run app.py


### Deployment on Streamlit
    Install Streamlit as this makes it easy to create and manage your Streamlit apps directly from the terminal.
    Next step would be to follow the instruction given on Streamlit Documentation to deploy a web app.


### Build a Docker Container for the ML Model
    Build the docker image docker build -t studentperformancepredict
    Run the app docker run -d -p 8501:8501 studentperformancepredict
    Deploy it on a Docker container.
    View the app within Docker Desktop docker image studentperformancepredict

### A Demo of the Web App :
https://github.com/user-attachments/assets/8ced7883-b7cd-49cf-814c-83f8108e9abd


### Future work

    Improve model performance using Adaboost or XGBoost Gradient Algorithm
    Add more better styling to the user interface.

### Some Useful Resources

    Streamlit Quickstart Documentation : https://docs.streamlit.io/

    
 
 

 
