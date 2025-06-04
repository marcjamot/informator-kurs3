from sklearn.datasets import load_iris
import pandas as pd

# Load the iris dataset
iris = load_iris()

# Create a DataFrame for better readability
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target
df["species"] = df["target"].map(
    {0: iris.target_names[0], 1: iris.target_names[1], 2: iris.target_names[2]}
)

print("Iris Dataset:")
print("=" * 50)
print(f"Dataset shape: {df.shape}")
print(f"Features: {list(iris.feature_names)}")
print(f"Target classes: {list(iris.target_names)}")

# Print sample for each flower type
for species_name in iris.target_names:
    print(f"\nSample of {species_name}:")
    species_data = df[df["species"] == species_name].head(3)
    print(species_data)

print("\nDataset summary:")
print(df.describe())
