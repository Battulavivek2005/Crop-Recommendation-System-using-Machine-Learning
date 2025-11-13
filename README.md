Crop Recommendation System using Machine Learning

The Crop Recommendation System is a machine learning–based web application that predicts the most suitable crop to grow based on soil nutrients and environmental conditions. This system helps farmers make data-driven decisions to improve crop yield and optimize agricultural planning.

Key Features:

1. Predicts the best crop based on soil nutrients (N, P, K), temperature, humidity, pH, and rainfall
2. Machine Learning model trained using Random Forest Classifier
3. Clean, user-friendly web interface developed with Flask
4. Attractive blurred farmer-themed background design
5. Easy to deploy and extend with APIs and additional features

Technologies Used:

1. Python
2. Flask (Web Framework)
3. Scikit-Learn (Machine Learning)
4. Pandas, NumPy (Data Processing)
5. HTML5, CSS3
6. Pickle (Model Serialization)
7. Kaggle Crop Recommendation Dataset

Project Structure:

Crop-Prediction/
│
├── app.py                     # Flask web application
├── train_model.py             # Script to train the ML model
├── crop_model.pkl             # Saved machine learning model
├── Crop_recommendation.csv    # Dataset used for training
├── requirements.txt           # Required Python libraries
│
├── templates/
│   ├── index.html             # Input form page
│   ├── result.html            # Result page
│
├── static/
│   ├── style.css              # Styling for UI
│   └── images/
│       └── farmer.jpg         # Background image
│
└── README.md                  # Project documentation

Dataset Information:

This project uses the Crop Recommendation Dataset from Kaggle.
It contains the following features:
| Feature     | Description                |
| ----------- | -------------------------- |
| N           | Nitrogen content in soil   |
| P           | Phosphorus content in soil |
| K           | Potassium content in soil  |
| temperature | Temperature in °C          |
| humidity    | Relative humidity (%)      |
| ph          | Soil pH value              |
| rainfall    | Rainfall in mm             |
| label       | Recommended crop           |

How It Works:

1. User enters soil and environmental values into the form
2. The trained Random Forest model processes the input
3. The model predicts the most suitable crop
4. The result is displayed on a beautifully designed output page

How to Run the Project:

Install Dependencies:
pip install -r requirements.txt

Train the Machine Learning Model:
python train_model.py

Run the Flask App:
python app.py

Open the Application:
Visit the following link in your browser:
http://127.0.0.1:5000

User Interface:

1. Modern UI with blurred farmer background
2. Centered card layout
3. Responsive and clean design
4. Simple and easy-to-use input form