import os
os.environ["GROQ_API_KEY"] = "insert_your_api_key_here"
import sys

from models import Job
from file_manager import load_text_file, save_to_json, save_to_csv
from parser import parse_resume
from matcher import ab_test_matchers
from reporter import generate_report, export_report_txt
from ai_integration import AIIntegration

def main():
    print("=== Smart Hiring Assistant ===")
    
    # Ensure output directory exists
    os.makedirs("output", exist_ok=True)
    
    # 1. Define standard job requirement
    job = Job(
        title="Senior Python Developer",
        required_skills=["Python", "Django", "REST APIs", "SQL", "AWS"],
        required_experience=5
    )
    
    resume_path = os.path.join("data", "sample_resume.txt")
    
    # Error Handling for missing input file
    try:
        print(f"Loading resume from {resume_path}...")
        resume_text = load_text_file(resume_path)
        if not resume_text:
            raise ValueError(f"Resume text could not be loaded or is empty.")
    except Exception as e:
        print(f"[Error] Failed to load resume: {e}")
        sys.exit(1)
        
    # Setup AI Client gracefully
    try:
        ai_client = AIIntegration()
    except Exception as e:
        print(f"[Warning] Failed to initialize AI client: {e}")
        ai_client = None

    # Parsing
    try:
        print("Parsing resume...")
        candidate = parse_resume(resume_text, ai_client=ai_client)
        print(f"Extracted Profile: {candidate.name} | Exp: {candidate.experience} yrs")
    except Exception as e:
        print(f"[Error] Parsing failed: {e}")
        sys.exit(1)

    # Matching
    try:
        print("Running Matching Algorithm (Strict vs Fuzzy)...")
        ab_test_result = ab_test_matchers(candidate, job)
        fuzzy_result = ab_test_result['fuzzy']
        print(f"Match Score: {fuzzy_result.score:.1f}%")
    except Exception as e:
        print(f"[Error] Matching failed: {e}")
        sys.exit(1)

    # Report Generation & Saving
    try:
        print("Generating recommendations and reports...")
        if ai_client:
            feedback = ai_client.generate_recommendation(
                candidate_data=str(candidate),
                job_data=str(job)
            )
            fuzzy_result.feedback = feedback
        
        # Save Text Report
        txt_path = os.path.join("output", "report.txt")
        export_report_txt(fuzzy_result, txt_path)
        
        # Save JSON Data
        json_path = os.path.join("output", "results.json")
        save_to_json([fuzzy_result], json_path)
        
        print("\nAll tasks completed successfully!")
        print(f"Outputs saved to: {txt_path} and {json_path}")
        
    except Exception as e:
        print(f"[Error] Reporting/Saving failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
