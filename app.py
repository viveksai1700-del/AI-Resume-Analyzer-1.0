import streamlit as st
import fitz

st.set_page_config(page_title="AI Resume Analyzer")

st.title("AI Resume Analyzer")
st.write("Upload your resume and get a quick skill analysis.")

skills = [
    "Python", "Java", "C++", "SQL", "HTML", "CSS",
    "JavaScript", "React", "Git", "GitHub", "Docker",
    "AWS", "Machine Learning", "Pandas", "NumPy"
]

resume = st.file_uploader("Upload Resume (PDF)", type="pdf")

if resume:
    doc = fitz.open(stream=resume.read(), filetype="pdf")

    text = ""
    for page in doc:
        text += page.get_text()

    found = [skill for skill in skills if skill.lower() in text.lower()]

    score = min(len(found) * 7, 100)

    st.subheader("Resume Score")
    st.progress(score / 100)
    st.write(f"**{score}%**")

    st.subheader("Skills Detected")

    if found:
        st.success(", ".join(found))
    else:
        st.warning("No listed skills detected.")

    st.subheader("Suggestions")

    missing = [skill for skill in skills if skill not in found]

    st.write("Consider adding:")
    st.write(", ".join(missing[:5]))