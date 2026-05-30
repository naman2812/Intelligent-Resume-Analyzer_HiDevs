# 🚀 Intelligent Resume Analyzer & Smart Hiring Assistant

This is a Python-based application that automates the resume screening process. It is designed to act as a Smart Hiring Assistant by automatically parsing resumes, matching candidate profiles to job requirements, and generating detailed, professional analysis reports. 

The system leverages the **LangChain** and **Groq AI** APIs alongside robust fallback logic to guarantee accuracy and reliability.

## 🎯 Key Features & Evaluation Criteria Met:
- **Code Quality**: Built using clean, modular Python scripts following strict PEP 8 guidelines.
- **Parsing Accuracy**: Reliably extracts candidate Name, Email, Skills, and Experience using AI data-extraction with a Regex safety fallback.
- **Matching Algorithm**: Employs an A/B tested matching engine (Strict vs. Fuzzy logic via `fuzzywuzzy`) to calculate a highly accurate 0-100 match score.
- **File Operations**: Automates the reading of raw `.txt` files and gracefully exports structured data into `.json` format.
- **Report Generation**: Dynamically constructs human-readable `.txt` analysis reports containing calculated match scores, fit summaries, and AI-generated custom interview questions.
- **Error Handling**: Designed with comprehensive `try/except` safeguards to gracefully handle missing files, missing API keys, or LLM deprecations without crashing.

## ⚙️ Core Architecture Flow
`Raw Resume Text` ➔ `[Parsing Layer]` ➔ `Candidate Dictionary` ➔ `[Matching Engine]` ➔ `Match Scores` ➔ `[Reporting Layer]` ➔ `Final Output (JSON & TXT)`