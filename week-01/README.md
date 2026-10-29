# Week 1: Student Score Data Processing

## Objective
Build a Python application that loads student scores, cleans invalid data, and analyzes valid scores using NumPy.

## Files
- `task.py` — Python source code.
- `task.ipynb` — Google Colab notebook with code and outputs.
- `students.csv` — Raw student-score dataset.
- `requirements.txt` — Required Python libraries.

## Method
The program reads student scores, converts them to numeric values, removes missing or invalid scores and scores outside 0–100, then uses NumPy to calculate the average, highest score, lowest score, and number of passing students (score >= 50).

## Results
- Raw records: 9
- Valid records: 5
- Average score: 73.4
- Highest score: 92
- Lowest score: 45
- Passing students: 4

## Run locally
Install the dependencies with `python -m pip install -r requirements.txt`, then run `python task.py`.
