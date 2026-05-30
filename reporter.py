from models import MatchResult

def generate_report(result: MatchResult) -> str:
    """Generates a human-readable string report for a match result."""
    report = f"--- Hiring Assistant Report ---\n"
    report += f"Candidate: {result.candidate_name}\n"
    report += f"Job Title: {result.job_title}\n"
    report += f"Match Score: {result.score:.2f}%\n"
    report += f"Matched Skills: {', '.join(result.matched_skills) if result.matched_skills else 'None'}\n"
    report += f"Missing Skills: {', '.join(result.missing_skills) if result.missing_skills else 'None'}\n"
    
    if result.feedback:
        report += f"\n--- AI Feedback & Interview Questions ---\n{result.feedback}\n"
        
    return report

def export_report_txt(result: MatchResult, filename: str):
    """Exports the report to a plain text file."""
    report_content = generate_report(result)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report_content)
    print(f"Report exported to {filename}")
