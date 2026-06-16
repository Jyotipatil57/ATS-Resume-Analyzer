import pandas as pd

skills_df = pd.read_csv(
    "data/skills.csv",
    header=None
)

skills_list = skills_df[0].tolist()

def extract_skills(text):

    found = []

    text = text.lower()

    for skill in skills_list:

        if skill.lower() in text:
            found.append(skill)

    return found