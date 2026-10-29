
import pandas as pd
import numpy as np


def clean_scores(data):
    """Keep only numeric scores between 0 and 100."""
    data = data.copy()
    data["score"] = pd.to_numeric(data["score"], errors="coerce")
    data = data.dropna(subset=["score"])
    data = data[data["score"].between(0, 100)]
    return data


# Load the raw dataset
data = pd.read_csv("students.csv")

print("Original dataset:")
print(data)

# Clean the data using our function
cleaned_data = clean_scores(data)

print("\nCleaned dataset:")
print(cleaned_data)


# Process the cleaned scores with NumPy
scores = cleaned_data["score"].to_numpy()

average_score = np.mean(scores)
highest_score = np.max(scores)
lowest_score = np.min(scores)
passing_students = np.sum(scores >= 50)

print("\nNumPy Analysis:")
print("Average score:", round(average_score, 2))
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)
print("Number of passing students:", passing_students)

