# Scenario 6: Custom Evaluation Metric
# Task: Implement a weighted accuracy metric where class 0 has weight 1
# and class 1 has weight 2.

import numpy as np

def weighted_accuracy(y_true, y_pred):
    weight_0 = 1
    weight_1 = 2

    correct_0 = ((y_true == 0) & (y_pred == 0)).sum()
    correct_1 = ((y_true == 1) & (y_pred == 1)).sum()

    total_weight = weight_0 * (y_true == 0).sum() + weight_1 * (y_true == 1).sum()

    return (weight_0 * correct_0 + weight_1 * correct_1) / total_weight


if __name__ == "__main__":
    y_true = np.array([0, 1, 0, 1, 1])
    y_pred = np.array([0, 1, 0, 0, 1])
    print("Weighted Accuracy:", weighted_accuracy(y_true, y_pred))