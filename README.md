# 📄 Smart Resume Score – Flask + Docker

A resume scoring API that uses natural language processing (NLP) to analyze a resume (PDF) and match it against job-relevant skills.

## 🔍 Features
- ✅ Upload PDF resume
- ✅ Parse and scan using NLP
- ✅ Compare against expected job skills
- ✅ Get a JSON response with:
  - Score
  - Skills found
  - Skills missing
  - Recommendations

## 🧰 Tech Stack
- Python
- Flask
- Docker
- Postman (for testing)
- NLP (basic keyword matching)

## 🚀 How to Run Locally (With Docker)

```bash
# Build the Docker image
docker build -t smart-resume-score .

# Run the container
docker run -p 5000:5000 smart-resume-score
Then test in Postman:

URL: http://localhost:5000/upload

Method: POST

Body: form-data → Key: file → upload your resume (PDF)
{
  "recommendation": "Try to include more technical keywords from job descriptions.",
  "score": 33,
  "skills_found": ["python", "git"],
  "skills_missing": ["docker", "flask", "api", "linux"]
}
