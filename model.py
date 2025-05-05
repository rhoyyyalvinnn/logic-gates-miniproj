from sklearn.neural_network import MLPClassifier
import numpy as np
import pickle

# Input data for all gates
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Output data for logic gates
y_and = np.array([0, 0, 0, 1])
y_or = np.array([0, 1, 1, 1])
y_nand = np.array([1, 1, 1, 0])
y_nor = np.array([1, 0, 0, 0])
y_xor = np.array([0, 1, 1, 0])
y_xnor = np.array([1, 0, 0, 1])

# Function to train MLP model for a gate
def train_gate_model(X, y):
    model = MLPClassifier(
        hidden_layer_sizes=(10, 5),  # two layers
        activation='relu',
        solver='adam',
        max_iter=10000,
        random_state=42
    )
    model.fit(X, y)
    return model



# Train models
model_and = train_gate_model(X, y_and)
model_or = train_gate_model(X, y_or)
model_nand = train_gate_model(X, y_nand)
model_nor = train_gate_model(X, y_nor)
model_xor = train_gate_model(X, y_xor)
model_xnor = train_gate_model(X, y_xnor)

# Save all models in a dictionary
models = {
    "and": model_and,
    "or": model_or,
    "nand": model_nand,
    "nor": model_nor,
    "xor": model_xor,
    "xnor": model_xnor
}

# Save models to file
with open("logic_gate_models.pkl", "wb") as f:
    pickle.dump(models, f)

# Optional: Show predictions for testing
print("✅ MLPClassifier Predictions:")
for gate, model in models.items():
    print(f"{gate.upper()} predictions: {model.predict(X)}")
