def generate_roadmap(missing_skills):
    roadmap = []

    for skill in missing_skills:
        roadmap.append(
            f"Learn {skill} → Practice with a small project → Add it to your resume"
        )

    return roadmap