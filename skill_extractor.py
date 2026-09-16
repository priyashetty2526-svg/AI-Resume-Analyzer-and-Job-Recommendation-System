import pandas as pd


def load_skills():
    skills = pd.read_csv("data/skill_dictionary.csv")
    return skills["skill"].dropna().tolist()


def extract_skills(text):
    skills = load_skills()
    found_skills = []

    text_lower = text.lower()

    for skill in skills:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills