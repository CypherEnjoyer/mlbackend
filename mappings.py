# filepath: /c:/Users/User/ml_backend - Copy/mappings.py
disease_symptoms = {
    'Common Cold': ['cough', 'cold', 'sore throat', 'fatigue'],
    'Influenza (Flu)': ['fever', 'cough', 'fatigue', 'sore throat', 'headache', 'nausea'],
    'COVID-19': ['fever', 'cough', 'fatigue', 'sore throat', 'shortness of breath', 'headache'],
    'Strep Throat': ['sore throat', 'headache', 'fever'],
    'Gastroenteritis (Stomach Flu)': ['nausea', 'vomiting', 'diarrhea', 'fever', 'fatigue'],
    'Bronchitis': ['cough', 'shortness of breath', 'fatigue', 'sore throat'],
    'Pneumonia': ['fever', 'cough', 'shortness of breath', 'fatigue'],
    'Migraine': ['headache', 'nausea', 'vomiting', 'fatigue'],
    'Tuberculosis (TB)': ['cough', 'fatigue', 'fever', 'shortness of breath'],
    'Allergic Rhinitis': ['cough', 'cold', 'sore throat', 'headache'],
    'Mononucleosis (Mono)': ['sore throat', 'fatigue', 'headache', 'fever'],
    'Food Poisoning': ['nausea', 'vomiting', 'diarrhea', 'fever'],
    'Chronic Fatigue Syndrome (CFS)': ['fatigue', 'headache', 'sore throat'],
    'Asthma': ['cough', 'shortness of breath', 'fatigue'],
    'Sinusitis': ['headache', 'sore throat', 'fatigue', 'cold', 'cough']
}

symptom_mapping = {
    'cough': 0,
    'cold': 1,
    'fever': 2,
    'headache': 3,
    'fatigue': 4,
    'nausea': 5,
    'vomiting': 6,
    'diarrhea': 7,
    'sore throat': 8,
    'shortness of breath': 9
}