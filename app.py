import streamlit as st
import pandas as pd

from resume_parser import extract_text
from text_cleaner import clean_text
from skill_extractor import extract_skills
from job_matcher import calculate_match_scores
from roadmap_generator import generate_roadmap


# ---------------------------------------------------------
# PAGE SETTINGS
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer and Job Recommendation System")

st.write(
    "Upload your resume to analyze job-role suitability, "
    "identify skill gaps, and generate a learning roadmap."
)


# ---------------------------------------------------------
# RESPONSIBLE AI NOTICE
# ---------------------------------------------------------

st.info(
    "⚠️ Responsible AI Notice: This tool provides guidance only. "
    "It does not make automatic hiring or rejection decisions. "
    "Match scores are estimates and should not be treated as recruiter decisions. "
    "The system focuses on job-related skills, education, projects, "
    "and relevant experience."
)


# ---------------------------------------------------------
# RESUME UPLOAD
# ---------------------------------------------------------

uploaded_file = st.file_uploader(
    "📤 Upload your Resume",
    type=["pdf", "docx"]
)


if uploaded_file is not None:

    # -----------------------------------------------------
    # FILE VALIDATION
    # -----------------------------------------------------

    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

    file_name = uploaded_file.name
    file_size = uploaded_file.size

    st.write(f"📄 **Uploaded File:** {file_name}")
    st.write(f"📦 **File Size:** {file_size / (1024 * 1024):.2f} MB")

    if file_size > MAX_FILE_SIZE:
        st.error("❌ File size is too large. Maximum allowed size is 5 MB.")
        st.stop()

    if not file_name.lower().endswith((".pdf", ".docx")):
        st.error("❌ Only PDF and DOCX files are supported.")
        st.stop()


    # -----------------------------------------------------
    # TEXT EXTRACTION
    # -----------------------------------------------------

    try:

        resume_text = extract_text(uploaded_file)

        if not resume_text.strip():
            st.error("❌ Could not extract text from the resume.")
            st.stop()


        # -------------------------------------------------
        # TEXT CLEANING
        # -------------------------------------------------

        cleaned_text = clean_text(resume_text)


        # -------------------------------------------------
        # SKILL EXTRACTION
        # -------------------------------------------------

        resume_skills = extract_skills(cleaned_text)


        # -------------------------------------------------
        # JOB ROLE MATCHING
        # -------------------------------------------------

        results = calculate_match_scores(cleaned_text)


        st.success("✅ Resume analyzed successfully!")


        # -------------------------------------------------
        # EXTRACTED SKILLS
        # -------------------------------------------------

        st.subheader("🛠️ Extracted Skills")

        if resume_skills:
            st.write(", ".join(resume_skills))
        else:
            st.write("No matching skills found.")


        # -------------------------------------------------
        # RESUME SECTIONS
        # -------------------------------------------------

        st.subheader("📚 Resume Information")

        education_keywords = [
            "education",
            "academic",
            "qualification",
            "degree"
        ]

        project_keywords = [
            "project",
            "projects"
        ]

        experience_keywords = [
            "experience",
            "work experience",
            "employment",
            "internship"
        ]

        education_found = any(
            keyword in cleaned_text
            for keyword in education_keywords
        )

        projects_found = any(
            keyword in cleaned_text
            for keyword in project_keywords
        )

        experience_found = any(
            keyword in cleaned_text
            for keyword in experience_keywords
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            if education_found:
                st.success("✅ Education section detected")
            else:
                st.warning("⚠️ Education section not clearly detected")

        with col2:
            if projects_found:
                st.success("✅ Projects section detected")
            else:
                st.warning("⚠️ Projects section not clearly detected")

        with col3:
            if experience_found:
                st.success("✅ Experience section detected")
            else:
                st.warning("⚠️ Experience section not clearly detected")


        # -------------------------------------------------
        # TARGET ROLE SELECTION
        # -------------------------------------------------

        st.subheader("🎯 Select Target Job Role")

        target_role = st.selectbox(
            "Choose the role you want to analyze:",
            results["job_role"].tolist()
        )


        selected_role = results[
            results["job_role"] == target_role
        ].iloc[0]


        selected_score = selected_role["match_score"]


        st.write(
            f"**Selected Target Role:** {target_role}"
        )

        st.write(
            f"**Match Score:** {selected_score}%"
        )


        # -------------------------------------------------
        # TOP 3 RECOMMENDED ROLES
        # -------------------------------------------------

        st.subheader("🏆 Top 3 Suitable Job Roles")

        top_three = results.head(3)

        for _, row in top_three.iterrows():

            st.write(
                f"**{row['job_role']}** — "
                f"{row['match_score']}% match"
            )


        # -------------------------------------------------
        # MATCH SCORE CHART
        # -------------------------------------------------

        st.subheader("📊 Job Role Match Scores")

        chart_data = results[
            ["job_role", "match_score"]
        ].set_index("job_role")

        st.bar_chart(chart_data)


        # -------------------------------------------------
        # SKILL GAP ANALYSIS
        # -------------------------------------------------

        required_skills = [
            skill.strip()
            for skill in selected_role[
                "required_skills"
            ].split(",")
        ]

        resume_skills_lower = [
            skill.lower()
            for skill in resume_skills
        ]

        found_target_skills = [
            skill
            for skill in required_skills
            if skill.lower() in resume_skills_lower
        ]

        missing_skills = [
            skill
            for skill in required_skills
            if skill.lower() not in resume_skills_lower
        ]


        # -------------------------------------------------
        # SKILLS FOUND FOR TARGET ROLE
        # -------------------------------------------------

        st.subheader("✅ Skills Found for Target Role")

        if found_target_skills:

            for skill in found_target_skills:
                st.write(f"- {skill}")

        else:
            st.write("No required skills found for this target role.")


        # -------------------------------------------------
        # MISSING SKILLS
        # -------------------------------------------------

        st.subheader("❌ Missing or Weak Skills")

        if missing_skills:

            for skill in missing_skills:
                st.write(f"- {skill}")

        else:

            st.write(
                "🎉 No major missing skills found for this target role!"
            )


        # -------------------------------------------------
        # LEARNING ROADMAP
        # -------------------------------------------------

        st.subheader("🗺️ Learning Roadmap")

        roadmap = generate_roadmap(missing_skills)

        if roadmap:

            for index, step in enumerate(
                roadmap,
                start=1
            ):

                st.write(
                    f"**Step {index}:** {step}"
                )

        else:

            st.write(
                "Your skills already match the selected role well."
            )


        # -------------------------------------------------
        # DOWNLOADABLE ANALYSIS REPORT
        # -------------------------------------------------

        st.subheader("📥 Download Analysis Report")

        report = f"""
AI RESUME ANALYZER AND JOB RECOMMENDATION SYSTEM
================================================

Uploaded Resume:
{file_name}

Target Role:
{target_role}

Match Score:
{selected_score}%

------------------------------------------------
EXTRACTED SKILLS
------------------------------------------------

{", ".join(resume_skills)}

------------------------------------------------
SKILLS FOUND FOR TARGET ROLE
------------------------------------------------

{", ".join(found_target_skills) if found_target_skills else "None"}

------------------------------------------------
MISSING OR WEAK SKILLS
------------------------------------------------

{", ".join(missing_skills) if missing_skills else "None"}

------------------------------------------------
TOP 3 RECOMMENDED ROLES
------------------------------------------------

"""

        for _, row in top_three.iterrows():

            report += (
                f"{row['job_role']} - "
                f"{row['match_score']}% match\n"
            )


        report += """
------------------------------------------------
LEARNING ROADMAP
------------------------------------------------

"""

        for index, step in enumerate(
            roadmap,
            start=1
        ):

            report += f"Step {index}: {step}\n"


        report += """

------------------------------------------------
RESPONSIBLE AI NOTICE
------------------------------------------------

This tool provides guidance only and does not make
automatic hiring or rejection decisions.

Match scores are estimates, not recruiter decisions.

The system focuses on job-related skills, education,
projects, and relevant experience.

Missing keywords do not always mean missing ability.
"""


        st.download_button(
            label="⬇️ Download Analysis Report",
            data=report,
            file_name="resume_analysis_report.txt",
            mime="text/plain"
        )


        # -------------------------------------------------
        # COMPLETE RESULTS TABLE
        # -------------------------------------------------

        st.subheader("📋 Complete Job Role Results")

        display_results = results[
            ["job_role", "match_score"]
        ]

        st.dataframe(
            display_results,
            use_container_width=True
        )


    except Exception as e:

        st.error(
            f"❌ Something went wrong: {e}"
        )