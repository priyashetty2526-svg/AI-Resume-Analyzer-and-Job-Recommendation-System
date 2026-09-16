# AI Resume Analyzer and Job Recommendation System

## Objective

The AI Resume Analyzer and Job Recommendation System analyzes a resume and checks how well it matches different job roles.

It provides:

- Resume text extraction
- Resume text cleaning
- Skill extraction
- Job-role match scores
- Top 3 suitable job roles
- Missing or weak skills
- Basic learning roadmap
- Downloadable analysis report

## Features

- Upload resumes in PDF or DOCX format
- Validate uploaded file type and file size
- Extract resume text
- Clean and normalize resume text
- Identify job-related skills
- Compare resumes with five predefined job roles
- Calculate match scores using TF-IDF and cosine similarity
- Display the top 3 suitable job roles
- Select a target job role
- Show skills found for the selected role
- Show missing or weak skills
- Generate a basic learning roadmap
- Display job-role match scores using a chart
- Download an analysis report
- Display a Responsible AI notice

## Technologies Used

- Python
- Streamlit
- pypdf
- python-docx
- Pandas
- NumPy
- Scikit-learn
- TF-IDF
- Cosine Similarity
- Git
- GitHub

## Supported Resume Formats

- PDF
- DOCX

## Job Roles

The system currently analyzes these five job roles:

1. Data Analyst
2. Machine Learning Engineer
3. AI Engineer
4. NLP Engineer
5. Computer Vision Engineer

## Skill Dataset

The project contains a controlled skill dictionary with 30 job-related skills covering areas such as:

- Programming
- Databases
- Data
- Machine Learning
- NLP
- AI
- Computer Vision
- Tools
- Cloud

## How It Works

1. Upload a PDF or DOCX resume.
2. Validate the uploaded file.
3. Extract the resume text.
4. Clean and normalize the text.
5. Extract relevant job-related skills.
6. Load predefined job-role requirements.
7. Compare resume skills with job-role requirements.
8. Calculate match scores using TF-IDF and cosine similarity.
9. Rank the job roles.
10. Display the top 3 suitable roles.
11. Select a target job role.
12. Identify skills found for the selected role.
13. Identify missing or weak skills.
14. Generate a basic learning roadmap.
15. Provide a downloadable analysis report.

## Matching Approach

The project follows the beginner approach described in the project guidance:

- Keyword matching for skill extraction
- TF-IDF for comparable text vectors
- Cosine similarity for match scores
- Rule-based learning roadmap

## Project Structure

```text
ai_resume_analyzer/
│
├── app.py
├── resume_parser.py
├── text_cleaner.py
├── skill_extractor.py
├── job_matcher.py
├── roadmap_generator.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── data/
│   ├── job_roles.csv
│   └── skill_dictionary.csv
│
├── sample_resumes/
│   ├── Anonymized Sample Resume A.pdf
│   ├── Anonymized Sample Resume A.docx
│   ├── Anonymized Sample Resume B.pdf
│   ├── Anonymized Sample Resume B.docx
│   ├── Anonymized Sample Resume C.pdf
│   └── Anonymized Sample Resume C.docx
│
├── reports/
│   └── workflow diagram
│
└── tests/
    └── test cases.csv