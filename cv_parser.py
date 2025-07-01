import fitz  # PyMuPDF

def parse_cv(cv_path: str) -> dict:
    try:
        with fitz.open(cv_path) as doc:
            text = ""
            for page in doc:
                text += page.get_text()

        print("📄 Extracted text:", text[:300])  # Preview text

        skills = []
        common_skills = ["Python", "Machine Learning", "AI", "LangChain", "Flutter", "Java", "C++", "SQL"]
        for skill in common_skills:
            if skill.lower() in text.lower():
                skills.append(skill)

        title = "AI Engineer" if "engineer" in text.lower() else "Software Developer"

        return {
            "title": title,
            "skills": skills
        }

    except Exception as e:
        print("❌ Error parsing CV:", e)
        return {"title": "", "skills": []}
