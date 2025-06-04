from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

# Define colorblind-friendly colors
colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]  # Blue, Orange, Green

# Create subplots: 4 rows (features) x 3 columns (categories)
fig, axes = plt.subplots(4, 3, figsize=(15, 16))
fig.suptitle("Iris Dataset Visualization by Feature and Category", fontsize=16)

# Plot each feature for each category
for feature_idx in range(4):
    for category_idx in range(3):
        # Get data for current category
        category_data = X[y == category_idx, feature_idx]

        # Create scatter plot for current feature and category
        axes[feature_idx, category_idx].scatter(
            range(len(category_data)),
            category_data,
            alpha=0.7,
            color=colors[category_idx],
        )
        axes[feature_idx, category_idx].set_title(
            f"{target_names[category_idx]}\n{feature_names[feature_idx]}"
        )
        axes[feature_idx, category_idx].set_xlabel("Sample Index")
        axes[feature_idx, category_idx].set_ylabel("Value")

plt.tight_layout()
plt.show()

# Print dataset info
print(f"Dataset shape: {X.shape}")
print(f"Feature names: {feature_names}")
print(f"Target names: {target_names}")
