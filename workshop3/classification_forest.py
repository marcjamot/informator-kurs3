import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.tree import plot_tree

N_TREES = 3
PLOT_TREES = True

# 1. Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# 2. Select features
X = df[["sepal width (cm)"]]
y = iris.target

# 3. Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 4. Train the random forest classifier
clf = RandomForestClassifier(n_estimators=N_TREES, max_depth=2)
clf.fit(X_train, y_train)

# 5. Predict and evaluate
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# 6. Display feature importance
print("Feature importance:", clf.feature_importances_)

if PLOT_TREES:
    fig, axes = plt.subplots(1, N_TREES, figsize=(15, 5))
    for i in range(N_TREES):
        plot_tree(
            clf.estimators_[i],
            feature_names=iris.feature_names,
            class_names=iris.target_names,
            filled=True,
            ax=axes[i],
        )
        axes[i].set_title(f"Tree {i + 1}")

    plt.tight_layout()
    plt.show()
