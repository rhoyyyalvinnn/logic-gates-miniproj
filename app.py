from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load all trained models
with open('logic_gate_models.pkl', 'rb') as f:
    models = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get user inputs for the two bits
        bit1 = int(request.form['bit1'])
        bit2 = int(request.form['bit2'])
        gate = request.form['gate']

        prediction = models[gate].predict(np.array([[bit1, bit2]]))
        rounded_prediction = round(prediction[0])
        return render_template('result.html', gate=gate.upper(), prediction=prediction, rounded_prediction=rounded_prediction)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)