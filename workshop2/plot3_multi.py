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

# Create subplots for pairwise feature combinations
fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle("Iris Dataset: Pairwise Feature Combinations", fontsize=16)

# Define feature pairs to plot
feature_pairs = [
    (0, 1),
    (0, 2),
    (0, 3),  # sepal length vs others
    (1, 2),
    (1, 3),
    (2, 3),  # remaining combinations
]

# Plot each feature pair
for idx, (feat_x, feat_y) in enumerate(feature_pairs):
    row = idx // 3
    col = idx % 3

    for category_idx in range(3):
        # Get data for current category
        mask = y == category_idx
        x_data = X[mask, feat_x]
        y_data = X[mask, feat_y]

        # Create scatter plot
        axes[row, col].scatter(
            x_data,
            y_data,
            alpha=0.7,
            color=colors[category_idx],
            label=target_names[category_idx],
            s=50,
        )

    axes[row, col].set_xlabel(feature_names[feat_x])
    axes[row, col].set_ylabel(feature_names[feat_y])
    axes[row, col].legend()
    axes[row, col].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Print dataset info
print(f"Dataset shape: {X.shape}")
print(f"Feature names: {feature_names}")
print(f"Target names: {target_names}")
