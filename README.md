# 🚀 Intelligent Resume Analyzer & Smart Hiring Assistant

## 👤 Contact Information
- **Name:** [Naman Lad]
- **Email:** [namanlad28@gmail.com]
- **LinkedIn/Portfolio:** [www.linkedin.com/in/naman-lad-44bb1a35a]

## 🎥 Project Demo Video
[https://youtu.be/BYwqIBIAy8A]

---

## 📖 Project Overview
This is a Python-based application that automates the resume screening process. It is designed to act as an Intelligent Resume Analyzer by automatically parsing resumes, matching candidate profiles to job requirements, and generating detailed, professional analysis reports. The system leverages the LangChain and Groq AI APIs alongside robust fallback logic to guarantee accuracy and reliability.

## ✨ Key Features Implemented
- **Intelligent Parsing:** Accurately extracts Candidate Name, Email, Skills, and Experience using AI with a Regex safety fallback.
- **Matching Algorithm:** Employs an A/B tested matching engine (Strict vs. Fuzzy logic via `fuzzywuzzy`) to calculate a highly accurate 0-100 match score against Job Requirements.
- **Automated Reporting:** Dynamically constructs human-readable `.txt` analysis reports containing calculated match scores, fit summaries, and AI-generated custom interview questions.
- **Robust File Operations:** Automates the reading of raw `.txt` files and gracefully exports structured data into `.json` format.
- **Graceful Error Handling:** Designed with comprehensive `try/except` safeguards to handle missing files, invalid inputs, or missing API keys without crashing.

## 💻 Setup Instructions
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/naman2812/intelligent_resume_analyzer_hidevs.git
   
2. Navigate into the project directory:
   ```bash
   cd intelligent_resume_analyzer_hidevs

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
4. Set your Groq API Key as an environment variable in your terminal:
   ```bash
   export GROQ_API_KEY="gsk_your_actual_key_here"

🚀 Usage Guidelines
Once your environment is set up, you can run the main orchestrator script.

To analyze the sample resume provided in the data/ folder, run:

   ```bash
   python main.py

   The application will output its progress to the terminal. Once complete, navigate to the output/ directory to view the exported report.txt and results.json files! To test a different resume, simply replace the text inside data/sample_resume.txt.
