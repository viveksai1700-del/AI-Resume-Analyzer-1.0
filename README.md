# AI Resume Analyzer

A lightweight web application that analyzes PDF resumes, detects technical skills, calculates a resume score, and provides quick suggestions for improvement.

## Overview

The **AI Resume Analyzer** helps students and job seekers quickly evaluate their resumes based on a predefined set of technical skills.

Users can upload a PDF resume and instantly view:

* Resume match score
* Detected technical skills
* Suggested skills to consider adding
* Resume analysis results

## Features

* PDF resume upload
* Automatic resume text extraction
* Technical skill detection
* Resume scoring system
* Improvement suggestions
* Simple and responsive Streamlit interface

## Tech Stack

* **Python**
* **Streamlit**
* **PyMuPDF**

## Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd AI-Resume-Analyzer
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## How It Works

1. Upload your resume in PDF format.
2. The application extracts text using PyMuPDF.
3. The extracted content is scanned for predefined technical skills.
4. A resume score is calculated based on detected skills.
5. Detected skills and improvement suggestions are displayed.

## Future Improvements

* AI-powered resume feedback
* Job description upload and matching
* ATS compatibility analysis
* Experience and education extraction
* Resume section analysis
* Downloadable analysis reports
* LLM integration for personalized recommendations

## Author

**Mittapally Sai Vivek**

Computer Science & Engineering Student

GitHub: [github.com/viveksai1700-del](https://github.com/viveksai1700-del)

---

If you found this project useful, consider giving the repository a star.
