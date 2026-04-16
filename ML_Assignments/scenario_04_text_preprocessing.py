# Scenario 4: Text Pre-processing
# Task: Clean a text column by converting to lowercase, removing special characters,
# and tokenizing the text into words.

import pandas as pd
import re

def clean_text(df, column):
    df[column] = df[column].str.lower()
    df[column] = df[column].apply(lambda x: re.sub(r'[^a-zA-Z\s]', '', x))
    df[column] = df[column].apply(lambda x: x.split())
    return df


if __name__ == "__main__":
    df = pd.DataFrame({"text": ["Hello World!", "AI @2025 is GREAT!!!"]})
    print(clean_text(df, "text"))