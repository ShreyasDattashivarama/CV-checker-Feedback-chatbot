import streamlit as st
from resume_parser import extract_resume_text
from feedback_engine import generate_feedback

st.set_page_config(page_title="CV Whisperer", layout="centered")
st.title("CV Checker - Resume Feedback Chatbot")
st.markdown("Upload your resume and get personalized feedback using NLP and LLM magic ")

uploaded_file = st.file_uploader("Upload your Resume (PDF or TXT)", type=["pdf", "txt"])
job_description = st.text_area("Optional: Paste a Job Description to match against")

if uploaded_file:
    with st.spinner("Analyzing your resume..."):
        resume_text = extract_resume_text(uploaded_file)
        feedback = generate_feedback(resume_text, job_description)
        
        st.subheader("Chatbot Feedback")
        st.write(feedback)

        st.download_button("Download Feedback as TXT", feedback, file_name="cv_feedback.txt")
