import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_job_roles():
    return pd.read_csv("data/job_roles.csv")


def load_skills():
    skills = pd.read_csv("data/skill_dictionary.csv")
    return skills["skill"].dropna().tolist()


def get_resume_skills(resume_text):
    skills = load_skills()
    resume_skills = []

    text_lower = resume_text.lower()

    for skill in skills:
        if skill.lower() in text_lower:
            resume_skills.append(skill)

    return resume_skills


def calculate_match_scores(resume_text):
    jobs = load_job_roles()

    resume_skills = get_resume_skills(resume_text)

    resume_skill_text = " ".join(resume_skills)

    documents = [resume_skill_text] + jobs["required_skills"].tolist()

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)

    scores = cosine_similarity(
        vectors[0:1],
        vectors[1:]
    ).flatten()

    jobs["match_score"] = (scores * 100).round(2)

    return jobs.sort_values(
        "match_score",
        ascending=False
    )