from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Candidate:
    name: str
    email: str
    skills: List[str]
    experience: int # years
    education: str

@dataclass
class Job:
    title: str
    required_skills: List[str]
    required_experience: int # years

@dataclass
class MatchResult:
    candidate_name: str
    job_title: str
    score: float
    matched_skills: List[str]
    missing_skills: List[str]
    feedback: str = ""
