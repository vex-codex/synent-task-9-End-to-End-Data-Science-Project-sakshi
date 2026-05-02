

# House Price Prediction Web Application

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange?logo=scikitlearn)
![NumPy](https://img.shields.io/badge/Library-NumPy-lightgrey?logo=numpy)
![Pandas](https://img.shields.io/badge/Library-Pandas-yellow?logo=pandas)
![Deployment](https://img.shields.io/badge/Deployment-Local%20Server-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Maintenance](https://img.shields.io/badge/Maintained-Yes-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Overview

This project is a Machine Learning-based web application that predicts house prices based on user inputs such as area, number of bedrooms, and house age. It demonstrates a complete workflow from model development to deployment using an interactive interface.

---

## Problem Statement

The objective is to build a predictive system that estimates house prices using key property features and delivers results through a user-friendly web application.

---

## Dataset Details

A structured sample dataset is used for training the model.

### Features:

* Area (square feet)
* Number of bedrooms
* House age (years)

### Target:

* Price (in Lakhs)

---

## Approach

### Model Training

* Algorithm: Linear Regression
* Trained using input features (area, bedrooms, age)
* Model saved using Pickle

### Model Deployment

* Model loaded into a Streamlit application
* User inputs collected via UI
* Real-time predictions generated

---

## Implementation Details

This project has been developed **from scratch using Python in Visual Studio Code**.
All components, including model training, serialization, and deployment, were implemented manually without relying on pre-built templates.

---

## Development Environment

* IDE: Visual Studio Code
* Language: Python 3.x
* Execution: Local machine (Streamlit server)

---

## Features

* Interactive user interface
* Real-time prediction
* Lightweight and efficient model
* Simple and clean design

---

## Output

* Accepts user input for property details
* Predicts house price instantly
* Displays output in Lakhs

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle

---

## How to Run

### Install Dependencies

```bash
pip install streamlit pandas scikit-learn numpy
```

### Train Model (Optional)

```bash
python train_model.py
```

### Run Application

```bash
streamlit run app.py
```

### Access Application

Open in browser:

```
http://localhost:8501
```

---

## Project Structure

```
House-Price-App
│
├── app.py
├── train_model.py
├── model.pkl
└── README.md
```

---



## Author

Sakshi Patel

---

