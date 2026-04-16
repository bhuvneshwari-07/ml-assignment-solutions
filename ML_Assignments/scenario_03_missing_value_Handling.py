# Scenario 3: Missing Value Handling
# Task: Handle missing values in the 'income' column of a dataset.

import pandas as pd

def handle_missing_values(df):
    skewness = df["income"].skew()

    if abs(skewness) < 0.5:
        df["income"].fillna(df["income"].median(), inplace=True)
        print("Filled with Median")
    else:
        df["income"].fillna(df["income"].mode()[0], inplace=True)
        print("Filled with Mode")

    return df


if __name__ == "__main__":
    df = pd.DataFrame({"income": [50000, 60000, None, 55000, None, 70000]})
    print(handle_missing_values(df))