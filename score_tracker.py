import json
import os
from datetime import datetime

SCORES_FILE = 'pyquiz_scores.json'


def save_score(username, difficulty, score):
    """Save user's quiz score to a JSON file."""
    if not os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, 'w') as f:
            json.dump([], f)

    with open(SCORES_FILE, 'r') as f:
        scores = json.load(f)

    new_score = {
        'username': username,
        'difficulty': difficulty,
        'score': score,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    scores.append(new_score)

    with open(SCORES_FILE, 'w') as f:
        json.dump(scores, f, indent=4)


def view_scores():
    """Display all saved scores."""
    if not os.path.exists(SCORES_FILE):
        print("No scores recorded yet.")
        return

    with open(SCORES_FILE, 'r') as f:
        scores = json.load(f)

    if not scores:
        print("No scores recorded yet.")
        return

    print("\n--- PyQuiz Score History ---")
    for score in scores:
        if score == scores[-1]:
            print(f"Username: {score['username']}")
            print(f"Difficulty: {score['difficulty']}")
            print(f"Score: {score['score']}/10")
            print(f"Date: {score['timestamp']}\n")
