from sklearn.linear_model import LogisticRegression
import numpy as np
import pickle

# Input data for all gates (each row is [bit1, bit2])
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Output data for AND, OR, XOR, NOR, NAND, XNOR gates
y_and = np.array([0, 0, 0, 1])  # AND gate outputs
y_or = np.array([0, 1, 1, 1])   # OR gate outputs
y_xor = np.array([0, 1, 1, 0])  # XOR gate outputs
y_nor = np.array([1, 0, 0, 0])  # NOR gate outputs
y_nand = np.array([1, 1, 1, 0]) # NAND gate outputs
y_xnor = np.array([1, 0, 0, 1]) # XNOR gate outputs

# Train a Logistic Regression model for each gate
model_and = LogisticRegression()
model_and.fit(X, y_and)

model_or = LogisticRegression()
model_or.fit(X, y_or)

model_xor = LogisticRegression()
model_xor.fit(X, y_xor)

model_nor = LogisticRegression()
model_nor.fit(X, y_nor)

model_nand = LogisticRegression()
model_nand.fit(X, y_nand)

model_xnor = LogisticRegression()
model_xnor.fit(X, y_xnor)

# Save all models
models = {
    "and": model_and,
    "or": model_or,
    "xor": model_xor,
    "nor": model_nor,
    "nand": model_nand,
    "xnor": model_xnor
}

# Save the trained models into a pickle file
with open('logic_gate_models.pkl', 'wb') as f:
    pickle.dump(models, f)

print("Models trained and saved successfully!")
