import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import pandas as pd
import json

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Extract text from PDF
def extract_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# Use Gemini to analyze resume vs JD
def get_gemini_response(resume_text, full_jd):
    prompt = f"""
    <ROLE> You are an expert ATS evaluator specializing in resume parsing, job description analysis, and candidate-job matching for data analysis and technology roles. </ROLE> <OBJECTIVE> Analyze and compare a given resume against a job description, providing a comprehensive evaluation of the candidate’s suitability. </OBJECTIVE> <CONTEXT> You will receive two texts: a resume and a job description. Focus on alignment of skills, experience, and keywords relevant to data analysis and technology. </CONTEXT> <REQUIREMENTS> 1. Parse and interpret the resume and job description accurately. 2. Identify key skills, qualifications, and experiences in both texts. 3. Calculate a percentage match reflecting alignment. 4. Identify important keywords in the job description missing from the resume. 5. Provide a concise profile summary based on the resume. 6. Output only valid JSON with no extra formatting or explanation. </REQUIREMENTS> <IMPLEMENTATION> 1. Extract relevant skills, experience, and qualifications from the resume. 2. Extract key requirements and important keywords from the job description. 3. Compare both to calculate match percentage. 4. Identify missing keywords from the resume. 5. Summarize the candidate profile concisely. 6. Output JSON as specified below. </IMPLEMENTATION> <OUTPUT FORMAT> ```json {{
  "JD Match": "X%",
  "MissingKeywords": ["keyword1", "keyword2", ...],
  "Profile Summary": "Brief relevant summary of candidate’s profile"
}} ``` No markdown or explanations, only JSON.
Resume: {resume_text}
Job Description: {full_jd}
    """


    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)

        if hasattr(response, 'text') and response.text:
            raw_text = response.text
        else:
            raw_text = response.parts[0].text if response.parts else ""

        import re
        cleaned_response = re.sub(r"^```json|```$", "", raw_text.strip(), flags=re.MULTILINE).strip()
        return json.loads(cleaned_response)

    except Exception as e:
        print("Gemini Error:", e)
        return {
            "JD Match": "0%",
            "MissingKeywords": ['all'],
            "Profile Summary": f"❌ Could not parse Gemini response: {str(e)}"
        }

# Streamlit UI
st.set_page_config(page_title="Smart ATS", layout="wide")
st.title("📁 Smart ATS – Bulk Resume Evaluator")
st.write("🚀 Upload up to 20 resumes and match them against a detailed job description.")

# Job Description Segmented Inputs
st.header("📌 Job Description Inputs")
col1, col2 = st.columns(2)
with col1:
    title = st.text_input("Job Title")
    skills_required = st.text_area("Required Skills / Tools")
with col2:
    responsibilities = st.text_area("Responsibilities")
    qualifications = st.text_area("Qualifications")

# Upload resumes
st.header("📤 Upload Resumes")
uploaded_files = st.file_uploader("Upload up to 20 resumes (PDF format)", type="pdf", accept_multiple_files=True)

# Process button
if st.button("🔍 Analyze Resumes"):
    if not uploaded_files or not any([title, skills_required, responsibilities, qualifications]):
        st.warning("Please upload resumes and fill out job description fields.")
    else:
        results = []
        full_jd = f"""
        Title: {title}
        Skills Required: {skills_required}
        Responsibilities: {responsibilities}
        Qualifications: {qualifications}
        """

        for file in uploaded_files:
            resume_text = extract_pdf_text(file)
            name_line = resume_text.strip().split("\n")[0].strip()  # Name from top line
            gemini_result = get_gemini_response(resume_text, full_jd)

            results.append({
                "Candidate Name": name_line or "Not Found",
                "JD Match (%)": int(gemini_result["JD Match"].replace("%", "")),
                "Missing Keywords": ", ".join(gemini_result["MissingKeywords"]),
                "Profile Summary": gemini_result["Profile Summary"]
            })

        # DataFrame output
        df = pd.DataFrame(results).sort_values(by="JD Match (%)", ascending=False).reset_index(drop=True)

        # Slider to filter
        st.slider("📈 Filter by JD Match %", 0, 100, 0, key="filter_slider")
        st.dataframe(df, use_container_width=True)

        # Download option
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Results as CSV", data=csv, file_name="ATS_Results.csv", mime="text/csv")
