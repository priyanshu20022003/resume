Zomato Delivery Time Prediction
This project builds a model to predict delivery time using various factors such as distance, delivery person age, weather conditions, vehicle condition, type of vehicle, city (tier1, tier2, tier3), road traffic, and other factors. The goal is to estimate the delivery time of food considering most of the factors that can affect the delivery process.

Environment Setup
Create a new Environment
bash
Copy code
conda create -p modular python=3.9 -y
Activate the Environment
Command Prompt
bash
Copy code
conda activate modular/
Git Bash
bash
Copy code
source activate modular/
Install Requirements
bash
Copy code
pip install -r requirements.txt
Project Description
Dataset
The dataset shared by Zomato is used in this project.

Data Preprocessing
Cleaning: Removing or correcting erroneous data.
Feature Engineering: Creating new features based on existing data to improve model performance.
Data Transformation: Transforming data into suitable formats for model building.
Feature Selection
Identifying and selecting relevant features for model building.

Model Training and Evaluation
Training and evaluating different regression models, such as:

Random Forest
Decision Tree
Gradient Boosting
Linear Regression
Ridge
XGBRegressor
Model Selection
Choosing the best-performing model based on evaluation metrics:

R² (R-squared)
MAE (Mean Absolute Error)
MSE (Mean Squared Error)
RMSE (Root Mean Squared Error)
Deployment
Packaging the model and its dependencies for deployment.

Code Organization
The project code is organized as follows:

articraft: Contains data ingestion, data transformation, and model training code.
data: Contains the final preprocessed data.
logs: Stores logs generated during the project.
prediction: Contains code for batch prediction.
batch_prediction: Stores the results of batch prediction.
config: Contains configuration files (e.g., config.yaml).
feature_eng: Includes code for feature engineering.
src: Contains various components, configurations, constants, entities, exceptions, loggers, pipelines, and utilities.
app.py: The main script that orchestrates the project.
exception.py: Handles exceptions and errors.
logs.py: Manages logging functionality.
schema.yaml: Defines the data schema.
main.py: The entry point of the project.
setup.py: Used for setting up the project environment.
template.py: Provides a template for data ingestion and preprocessing.
Additional Features
Interactive Dashboard
A dashboard that visualizes the model predictions and other project insights.

Documentation
Detailed documentation explaining the project architecture, code structure, and deployment process.

Continuous Integration/Continuous Deployment (CI/CD)
Automated pipelines for testing, building, and deploying the project.

Testing
Unit tests and integration tests to ensure code quality.

Version Control
Code is managed using Git for version control and collaboration.

Getting Started
To get a local copy up and running follow these simple steps.

Prerequisites
Ensure you have the following installed:

Python 3.9
Conda
