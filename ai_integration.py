import os
import json
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from typing import Dict, Any

AI_PROMPTS = {
    "extraction": """
    You are an AI specialized in reading resumes and extracting structured data.
    Extract the following information from the resume text:
    - Name
    - Email
    - List of skills (as a JSON array of strings)
    - Years of experience (as an integer)
    - Education
    
    Output ONLY a valid JSON object matching this schema, no other text:
    {{
        "name": "Full Name",
        "email": "Email Address",
        "skills": ["Skill1", "Skill2"],
        "experience": 5,
        "education": "Degree, University"
    }}
    
    Resume Text:
    {text}
    """,
    "recommendation": """
    You are an AI specialized in HR and recruiting.
    Given a candidate's profile and a job description, provide a short, professional assessment
    of their fit for the role and suggest 2 interview questions.
    
    Candidate Profile:
    {candidate}
    
    Job Description:
    {job}
    
    Provide your response as a clear, concise paragraph followed by the interview questions.
    """
}

class AIIntegration:
    def __init__(self, model_name="llama-3.1-8b-instant"):
        # Expects GROQ_API_KEY environment variable to be set
        try:
            self.llm = ChatGroq(model_name=model_name, temperature=0.1)
        except Exception as e:
            print(f"Warning: Failed to initialize ChatGroq. Is GROQ_API_KEY set? Error: {e}")
            self.llm = None
            
    def extract_candidate_info(self, resume_text: str) -> Dict[str, Any]:
        """Uses LLM to extract structured data from a resume."""
        if not self.llm:
            return {}
            
        prompt = ChatPromptTemplate.from_template(AI_PROMPTS["extraction"])
        chain = prompt | self.llm
        
        try:
            response = chain.invoke({"text": resume_text})
            # Parse the JSON string from the response
            # Sometimes LLMs wrap JSON in markdown blocks
            content = response.content.strip()
            if content.startswith("```json"):
                content = content[7:-3]
            elif content.startswith("```"):
                content = content[3:-3]
                
            return json.loads(content)
        except Exception as e:
            print(f"Error during AI extraction: {e}")
            return {}

    def generate_recommendation(self, candidate_data: str, job_data: str) -> str:
        """Uses LLM to generate interview questions and a fit summary."""
        if not self.llm:
            return "AI Recommendation not available."
            
        prompt = ChatPromptTemplate.from_template(AI_PROMPTS["recommendation"])
        chain = prompt | self.llm
        
        try:
            response = chain.invoke({"candidate": candidate_data, "job": job_data})
            return response.content
        except Exception as e:
            print(f"Error generating AI recommendation: {e}")
            return "Could not generate recommendation."
