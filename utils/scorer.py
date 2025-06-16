def score_resume(text):
    desired_skills = ["python", "docker", "flask", "git", "api", "linux"]
    found_skills = [skill for skill in desired_skills if skill in text.lower()]
    
    score = int((len(found_skills) / len(desired_skills)) * 100)
    missing = list(set(desired_skills) - set(found_skills))
    
    return {
        "score": score,
        "skills_found": found_skills,
        "skills_missing": missing,
        "recommendation": "Try to include more technical keywords from job descriptions."
    }
