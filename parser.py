import re
from typing import Optional
from models import Candidate
from ai_integration import AIIntegration

def parse_resume_regex(text: str) -> Candidate:
    """Fallback parser using basic string operations and regex if AI is unavailable."""
    name_match = re.search(r"Name:\s*(.*)", text)
    email_match = re.search(r"Email:\s*([\w\.-]+@[\w\.-]+)", text)
    skills_match = re.search(r"Skills:\s*(.*)", text)
    exp_match = re.search(r"Experience:\s*(\d+)", text)
    edu_match = re.search(r"Education:\s*(.*)", text)
    
    name = name_match.group(1).strip() if name_match else "Unknown"
    email = email_match.group(1).strip() if email_match else "Unknown"
    
    skills = []
    if skills_match:
        skills = [s.strip() for s in skills_match.group(1).split(",")]
        
    experience = int(exp_match.group(1)) if exp_match else 0
    education = edu_match.group(1).strip() if edu_match else "Unknown"
    
    return Candidate(
        name=name,
        email=email,
        skills=skills,
        experience=experience,
        education=education
    )

def parse_resume(text: str, ai_client: Optional[AIIntegration] = None) -> Candidate:
    """Parses a resume using AI first, falling back to regex on failure."""
    if ai_client:
        try:
            data = ai_client.extract_candidate_info(text)
            if data:
                return Candidate(
                    name=data.get("name", "Unknown"),
                    email=data.get("email", "Unknown"),
                    skills=data.get("skills", []),
                    experience=data.get("experience", 0),
                    education=data.get("education", "Unknown")
                )
        except Exception as e:
            print(f"AI parsing failed, falling back to regex. Error: {e}")
            
    # Fallback to regex
    return parse_resume_regex(text)
