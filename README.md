Project Overview
This project is a web application that allows users to input two binary bits and choose a logic gate (AND, OR, XOR, etc.). The application uses pre-trained machine learning models to predict the output of the selected logic gate for the given input.

Built with Flask and Python, this project allows users to interact with the system through a clean, easy-to-use web interface. It leverages machine learning models to predict the result of logic gate operations based on user input.

Features
User Input: Users can input two binary bits (0 or 1) and select a logic gate.

Prediction: After submission, the app uses pre-trained models to compute the result of the selected logic gate.

Results Display: The predicted results are displayed on a new page, showing both the exact prediction and the rounded result.

Technology Stack
Frontend: HTML, CSS, JavaScript

Backend: Python, Flask

Machine Learning: Pickled trained models (using scikit-learn and TensorFlow)

Deployment: Render for web hosting

Project Structure
bash
Copy
Edit
/project_root
    /app.py                  # Main Flask application
    /templates
        index.html           # Home page
        result.html          # Results page
    /static
        style.css            # Styles for the app
        script.js            # JavaScript for interactivity
    logic_gate_models.pkl    # Pickled machine learning models
    requirements.txt         # Python dependencies
Setup and Installation
Clone the repository:


git clone https://github.com/your-username/logic-gates-miniproj.git
cd logic-gates-miniproj
Install the required dependencies:


pip install -r requirements.txt
Run the Flask app locally:


python app.py
Visit http://127.0.0.1:5000/ in your browser to see the app running locally.

Deployment
The app is deployed to Render, where it can be accessed through the following URL:

Live Demo

Requirements
Python 3.11 or higher

Flask

scikit-learn

TensorFlow

gunicorn

You can install the required dependencies with the requirements.txt file by running:

bash
Copy
Edit
pip install -r requirements.txt
Known Issues
If you encounter a "500 Internal Server Error", ensure that both index.html and result.html files are correctly placed in the /templates folder.

The machine learning models must be correctly loaded from the logic_gate_models.pkl file.