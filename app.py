from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('crop_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    N = int(request.form['nitrogen'])
    P = int(request.form['phosphorus'])
    K = int(request.form['potassium'])
    temp = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    ph = float(request.form['ph'])
    rainfall = float(request.form['rainfall'])
    
    features = np.array([[N, P, K, temp, humidity, ph, rainfall]])
    prediction = model.predict(features)
    crop = prediction[0].capitalize()

    return render_template('result.html', prediction_text=f"🌾 Recommended Crop: {crop}")

if __name__ == '__main__':
    app.run(debug=True)
