from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pandas as pd
from itertools import combinations

# Load dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Define target
y = df["petal length (cm)"]

# Get all feature combinations (excluding the target)
features = ["sepal length (cm)", "sepal width (cm)", "petal width (cm)"]
all_combinations = []

# Generate all possible combinations (1 to 3 features)
for r in range(1, len(features) + 1):
    all_combinations.extend(combinations(features, r))

print("Feature Combination Analysis:")
print("=" * 80)

results = []

for feature_combo in all_combinations:
    X = df[list(feature_combo)]
    
    # Split into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Fit linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Predict and evaluate
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = mse**0.5
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    # Store results
    results.append({
        'features': feature_combo,
        'mse': mse,
        'rmse': rmse,
        'mae': mae,
        'r2': r2
    })
    
    print(f"Features: {', '.join(feature_combo)}")
    print(f"MSE: {round(mse, 4)}, RMSE: {round(rmse, 4)}, MAE: {round(mae, 4)}, R²: {round(r2, 4)}")
    print("-" * 80)

# Find best combination based on R²
best_combo = max(results, key=lambda x: x['r2'])
print(f"\nBest combination (highest R²): {', '.join(best_combo['features'])}")
print(f"R² Score: {round(best_combo['r2'], 4)}")
