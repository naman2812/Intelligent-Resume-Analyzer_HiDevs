import json
import csv
from typing import List, Dict, Any
from models import MatchResult

def save_to_json(results: List[MatchResult], filename: str) -> None:
    """Save a list of MatchResult objects to a JSON file."""
    data = []
    for r in results:
        data.append({
            "candidate_name": r.candidate_name,
            "job_title": r.job_title,
            "score": r.score,
            "matched_skills": r.matched_skills,
            "missing_skills": r.missing_skills,
            "feedback": r.feedback
        })
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print(f"Results successfully saved to {filename}")

def save_to_csv(results: List[MatchResult], filename: str) -> None:
    """Save a list of MatchResult objects to a CSV file."""
    if not results:
        print("No results to save.")
        return
        
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Candidate Name", "Job Title", "Score", "Matched Skills", "Missing Skills", "Feedback"])
        for r in results:
            writer.writerow([
                r.candidate_name,
                r.job_title,
                round(r.score, 2),
                ", ".join(r.matched_skills),
                ", ".join(r.missing_skills),
                r.feedback
            ])
    print(f"Results successfully saved to {filename}")

def load_text_file(filename: str) -> str:
    """Load contents of a text file (like a resume or job description)."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return ""
