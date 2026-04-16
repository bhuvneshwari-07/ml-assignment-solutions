# Scenario 5: Hyperparameter Tuning
# Task: Use GridSearchCV to find the best combination of 'max_depth' and 'n_estimators'
# for a Random Forest classifier.

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_iris

def tune_model():
    X, y = load_iris(return_X_y=True)

    model = RandomForestClassifier()

    param_grid = {
        "max_depth": [3, 5, 7],
        "n_estimators": [50, 100]
    }

    grid = GridSearchCV(model, param_grid, cv=5)
    grid.fit(X, y)

    print("Best Params:", grid.best_params_)
    return grid.best_estimator_


if __name__ == "__main__":
    tune_model()