from flask import Flask, render_template, request
import pickle
import numpy as np

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
    app.run(debug=True)
