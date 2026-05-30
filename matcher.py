from fuzzywuzzy import fuzz
from models import Candidate, Job, MatchResult

def fuzzy_skill_match(candidate_skill: str, required_skill: str, threshold: int = 85) -> bool:
    """Uses fuzzy string matching to compare skills."""
    ratio = fuzz.ratio(candidate_skill.lower(), required_skill.lower())
    return ratio >= threshold

def match_candidate_strict(candidate: Candidate, job: Job) -> MatchResult:
    """Strict matching algorithm for A/B testing."""
    matched_skills = []
    missing_skills = []
    
    cand_skills_lower = [s.lower() for s in candidate.skills]
    
    for req_skill in job.required_skills:
        if req_skill.lower() in cand_skills_lower:
            matched_skills.append(req_skill)
        else:
            missing_skills.append(req_skill)
            
    score = (len(matched_skills) / len(job.required_skills)) * 100 if job.required_skills else 100
    
    # Penalize if candidate doesn't have required experience
    if candidate.experience < job.required_experience:
        score *= 0.8
        
    return MatchResult(
        candidate_name=candidate.name,
        job_title=job.title,
        score=score,
        matched_skills=matched_skills,
        missing_skills=missing_skills
    )

def match_candidate_fuzzy(candidate: Candidate, job: Job) -> MatchResult:
    """Fuzzy matching algorithm to tolerate typos/variations."""
    matched_skills = []
    missing_skills = []
    
    for req_skill in job.required_skills:
        is_match = False
        for cand_skill in candidate.skills:
            if fuzzy_skill_match(cand_skill, req_skill):
                is_match = True
                break
        
        if is_match:
            matched_skills.append(req_skill)
        else:
            missing_skills.append(req_skill)
            
    score = (len(matched_skills) / len(job.required_skills)) * 100 if job.required_skills else 100
    
    if candidate.experience < job.required_experience:
        score *= 0.8
        
    return MatchResult(
        candidate_name=candidate.name,
        job_title=job.title,
        score=score,
        matched_skills=matched_skills,
        missing_skills=missing_skills
    )

def ab_test_matchers(candidate: Candidate, job: Job) -> dict:
    """Runs an A/B test comparing strict vs fuzzy matching."""
    res_strict = match_candidate_strict(candidate, job)
    res_fuzzy = match_candidate_fuzzy(candidate, job)
    
    return {
        "strict": res_strict,
        "fuzzy": res_fuzzy,
        "difference_in_score": res_fuzzy.score - res_strict.score,
        "difference_in_skills": list(set(res_fuzzy.matched_skills) - set(res_strict.matched_skills))
    }
