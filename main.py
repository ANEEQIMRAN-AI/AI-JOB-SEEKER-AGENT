import streamlit as st
from graph import build_job_search_graph
from dotenv import load_dotenv
import os

st.set_page_config(page_title="Job Searcher Agent", layout="centered")
st.title("🤖 JOB SEARCHER")
st.write("Upload your CV and get job matches on WhatsApp!")

cv_file = st.file_uploader("📄 Upload your CV (PDF only)", type=['pdf'])

if cv_file:
    with open("temp_cv.pdf", "wb") as f:
        f.write(cv_file.read())
    st.success("✅ CV uploaded!")

    if st.button("🔍 Start Job Search"):
        load_dotenv()
        graph = build_job_search_graph()
        graph.invoke({"cv_path": "temp_cv.pdf"})
        st.success("✅ Job search started. Check your WhatsApp!")
