import os
from flask import Flask, request, jsonify, render_template
import pickle
import re

app = Flask(__name__)

# Load models safely
MODEL_PATH = 'model.pkl'
VECTORIZER_PATH = 'vectorizer.pkl'

try:
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    with open(VECTORIZER_PATH, 'rb') as f:
        vectorizer = pickle.load(f)
    models_loaded = True
    if models_loaded:
        import numpy as np
        feature_names = vectorizer.get_feature_names_out()
        coefficients = model.coef_[0]
except Exception as e:
    print(f"Error loading models: {e}")
    models_loaded = False

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def get_top_words(vec, top_n=5):
    indices = vec.nonzero()[1]

    scores = []
    for i in indices:
        score = vec[0, i] * coefficients[i]
        scores.append((feature_names[i], score))

    # sort by importance
    scores = sorted(scores, key=lambda x: abs(x[1]), reverse=True)

    return [word for word, score in scores[:top_n]]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not models_loaded:
        return jsonify({'error': 'Models are not available. Please check server logs.'}), 500

    try:
        data = request.get_json()
        message = data.get('message', '')

        if not message.strip():
            return jsonify({'error': 'Message cannot be empty.'}), 400

        # Preprocess
        cleaned_message = clean_text(message)
        
        # Vectorize
        vectorized_message = vectorizer.transform([cleaned_message])
        
        words = get_top_words(vectorized_message)
        
        # Predict (0 -> Ham, 1 -> Spam based on notebook)
        prediction = model.predict(vectorized_message)[0]
        
        proba = model.predict_proba(vectorized_message)[0]
        prob_spam = float(proba[1])
        
        result = "Spam" if prediction == 1 else "Ham"
        
        return jsonify({
            'prediction': result,
            'confidence': prob_spam,
            'message': message,
            'words': words,
            'status': 'success'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)



