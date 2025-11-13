import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the dataset (make sure this file exists in the same folder)
data = pd.read_csv('Crop_recommendation.csv')

# Separate input features and target label
X = data.drop('label', axis=1)
y = data['label']

# Split data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model as crop_model.pkl
pickle.dump(model, open('crop_model.pkl', 'wb'))

print("✅ Model trained and saved successfully as crop_model.pkl")
