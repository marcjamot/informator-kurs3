from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
from sklearn.metrics import mean_absolute_error, r2_score
import numpy as np

# Load dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Define features (X) and target (y)
# Check workshop2 plot3!
X = df[["sepal width (cm)"]]
# X = df[["sepal width (cm)", "..."]]

y = df["petal length (cm)"]

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Fit linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

# Calculate additional metrics
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Evaluate model performance with ranges
print("Model Performance Evaluation:")
print("-" * 40)
print(f"MSE: {mse:.4f} (Good: <0.1, OK: 0.1-0.5, Bad: >0.5)")
print(f"RMSE: {rmse:.4f} (Good: <0.3, OK: 0.3-0.7, Bad: >0.7)")
print(f"MAE: {mae:.4f} (Good: <0.2, OK: 0.2-0.5, Bad: >0.5)")
print(f"R²: {r2:.4f} (Good: >0.8, OK: 0.6-0.8, Bad: <0.6)")
