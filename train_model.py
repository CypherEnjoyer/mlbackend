# filepath: /c:/Users/Balagsa/ml_backend/train_model.py
import numpy as np # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.ensemble import RandomForestClassifier # type: ignore
import joblib # type: ignore
import csv # type: ignore
from mappings import disease_symptoms, symptom_mapping

# Generate a dataset based on the disease_symptoms mapping
n_samples = 1000
X = []
y = []

for disease, symptoms in disease_symptoms.items():
    for _ in range(n_samples // len(disease_symptoms)):
        # Generate full symptom vector
        symptom_vector = [0] * len(symptom_mapping)
        for symptom in symptoms:
            symptom_vector[symptom_mapping[symptom]] = 1
        X.append(symptom_vector)
        y.append(list(disease_symptoms.keys()).index(disease))
        
        # Generate individual symptom vectors
        for symptom in symptoms:
            symptom_vector = [0] * len(symptom_mapping)
            symptom_vector[symptom_mapping[symptom]] = 1
            X.append(symptom_vector)
            y.append(list(disease_symptoms.keys()).index(disease))

X = np.array(X)
y = np.array(y)

# Save the dataset to a CSV file for inspection
with open('dataset.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['symptom_vector', 'disease_index'])
    for i in range(len(X)):
        writer.writerow([X[i], y[i]])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model to a file
joblib.dump(model, 'model.pkl')

print("Model trained and saved as model.pkl")
print("Dataset saved as dataset.csv")