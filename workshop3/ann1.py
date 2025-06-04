import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
import warnings

warnings.filterwarnings("ignore")  # Ignore convergence warnings

# 1. Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# 2. Scale the features (important for neural nets!)
scaler = StandardScaler()
X = scaler.fit_transform(X)

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Train the MLP model
clf = MLPClassifier(
    hidden_layer_sizes=(10,),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42,
)
clf.fit(X_train, y_train)

# 5. Predict and evaluate
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(
    "\nClassification Report:\n",
    classification_report(y_test, y_pred, target_names=iris.target_names),
)

# 6. Plot the loss curve
plt.figure(figsize=(8, 4))
plt.plot(clf.loss_curve_, label="Loss")
plt.title("Loss Curve During Training")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
