from sklearn.linear_model import LinearRegression
import numpy as np
import pickle

# Input data for all gates (each row is [bit1, bit2])
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Output data for AND, OR, XOR, NOR gates
y_and = np.array([0, 0, 0, 1])  # AND gate outputs
y_or = np.array([0, 1, 1, 1])   # OR gate outputs
y_xor = np.array([0, 1, 1, 0])  # XOR gate outputs
y_nor = np.array([1, 0, 0, 0])  # NOR gate outputs

# Train a model for each gate
model_and = LinearRegression()
model_and.fit(X, y_and)

model_or = LinearRegression()
model_or.fit(X, y_or)

model_xor = LinearRegression()
model_xor.fit(X, y_xor)

model_nor = LinearRegression()
model_nor.fit(X, y_nor)

# Save all models
models = {
    "and": model_and,
    "or": model_or,
    "xor": model_xor,
    "nor": model_nor
}

with open('logic_gate_models.pkl', 'wb') as f:
    pickle.dump(models, f)
