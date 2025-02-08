from flask import Flask, request, jsonify
import joblib
import numpy as np
import logging
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import DiagnosisRecord, Base
from mappings import disease_symptoms, symptom_mapping

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Load a pre-trained model (replace with your model)
model = joblib.load('model.pkl')

# Configure MySQL database connection
DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/sds_capstone'
engine = create_engine(DATABASE_URI)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

@app.route('/diagnose', methods=['POST'])
def diagnose():
    try:
        data = request.json
        logging.debug(f"Received data: {data}")
        symptoms = data['symptoms']
        # Convert symptoms to numerical format
        symptom_vector = [0] * len(symptom_mapping)
        for symptom in symptoms:
            if symptom in symptom_mapping:
                symptom_vector[symptom_mapping[symptom]] = 1
        logging.debug(f"Symptom vector: {symptom_vector}")
        # Predict using the model
        probabilities = model.predict_proba([symptom_vector])[0]
        logging.debug(f"Probabilities: {probabilities}")
        top_n = 3  # Number of top diagnoses to return
        top_indices = np.argsort(probabilities)[-top_n:][::-1]
        diagnoses = [(list(disease_symptoms.keys())[i], probabilities[i]) for i in top_indices]

        result = {'diagnoses': [{'disease': diagnosis, 'probability': prob} for diagnosis, prob in diagnoses]}
        logging.debug(f"Result: {result}")

        # Store the data in the database
        session = DBSession()
        record = DiagnosisRecord(symptoms=str(symptoms), diagnosis=json.dumps(result))
        session.add(record)
        session.commit()
        session.close()

        return jsonify(result)
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)