# END TO END MACHINE LEARNING AND OPERATIONS (MLOPS) PROJECT FOR PREDICTING STUDENT PERFORMANCE

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

Name: testdockerdan.azurewebsites.net