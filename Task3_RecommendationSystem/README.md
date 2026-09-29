# CODSOFT AI Internship - Task 3

## Movie Recommendation System

### Objective
Build a simple movie recommendation system that recommends movies based on similarity between a selected movie and other movies.

### Description
This project implements a simple content-based movie recommendation system using Python. It reads movie information from a CSV dataset and compares genres and description words to find similar movies.

### Technologies Used
- Python
- CSV module
- File handling
- Sets and string processing
- Content-based similarity

### Features
- Displays available movies
- Accepts a movie name
- Provides five recommendations
- Calculates a similarity score
- Handles invalid movie names
- Provides an exit option

### How It Works
1. Loads movies from `movies.csv`.
2. Converts genre and description text into word sets.
3. Compares common genre and description words.
4. Calculates a similarity score.
5. Sorts movies by similarity score.
6. Displays the top five recommendations.

### How to Run

No external libraries are required.

```bash
python recommendation_system.py
