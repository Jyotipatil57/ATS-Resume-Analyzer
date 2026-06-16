import streamlit as st

from utils.parser import extract_pdf, extract_docx
from utils.skills import extract_skills
from utils.ats_score import calculate_ats_score
from utils.similarity import get_match_score

st.title("AI ATS Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

job_description = st.text_area(
    "Paste Job Description"
)

if st.button("Analyze Resume"):

    if uploaded_file and job_description:

        if uploaded_file.name.endswith(".pdf"):
            resume_text = extract_pdf(uploaded_file)
        else:
            resume_text = extract_docx(uploaded_file)

        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(job_description)

        ats_score = calculate_ats_score(
            resume_skills,
            jd_skills
        )

        match_score = get_match_score(
            resume_text,
            job_description
        )

        missing_skills = list(
            set(jd_skills) -
            set(resume_skills)
        )

        st.success("Analysis Complete")

        st.subheader("ATS Score")
        st.metric("Score", f"{ats_score}%")

        st.subheader("Resume Match")
        st.metric("Match", f"{match_score}%")

        st.subheader("Detected Skills")
        st.write(resume_skills)

        st.subheader("Missing Skills")
        st.write(missing_skills)

    else:
        st.warning(
            "Please upload a resume and enter a job description."
        )