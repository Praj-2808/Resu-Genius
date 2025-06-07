import streamlit as st

st.set_page_config(page_title="ResuGenius | Smart Resume Tools", layout="wide")

st.markdown("""
   <style>
    body {
        background: linear-gradient(135deg, #0b0c10, #1f2833);
        font-family: 'Segoe UI', 'Roboto', sans-serif;
        margin: 0;
        padding: 0;
        color: #f8f8f8;
    }

    .hero-container {
        padding: 4rem 2rem;
        border-radius: 2rem;
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.6);
        margin-bottom: 4rem;
        text-align: center;
    }

    .hero-title {
        font-size: 3.5rem;
        font-weight: 900;
        color: #64ffda;
        margin-bottom: 1rem;
        text-shadow: 0 0 12px rgba(100, 255, 218, 0.3);
        animation: glow 2s infinite alternate;
    }

    @keyframes glow {
        from { text-shadow: 0 0 12px rgba(100, 255, 218, 0.3); }
        to { text-shadow: 0 0 24px rgba(100, 255, 218, 0.6); }
    }

    .hero-subtitle {
        font-size: 1.3rem;
        color: #ccc;
        margin-bottom: 2rem;
    }

    .feature-box {
        background: rgba(255, 255, 255, 0.04);
        backdrop-filter: blur(12px);
        border-radius: 1.5rem;
        padding: 2.5rem;
        box-shadow: 0 8px 30px rgba(0, 255, 255, 0.07);
        transition: all 0.3s ease;
        height: 100%;
        border: 1px solid rgba(255, 255, 255, 0.08);
    }

    .feature-box:hover {
        transform: translateY(-8px);
        box-shadow: 0 10px 40px rgba(100, 255, 218, 0.15);
    }

    .feature-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #a9f0ff;
        margin-bottom: 1.2rem;
        text-align: center;
    }

    .feature-desc {
        font-size: 1.05rem;
        color: #d0d0d0;
        line-height: 1.6;
        margin-bottom: 2rem;
        text-align: center;
    }

    .feature-btn {
        background: linear-gradient(to right, #7f5af0, #64ffda);
        color: #0f0f0f;
        padding: 0.8rem 1.8rem;
        border-radius: 12px;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(100, 255, 218, 0.3);
        text-align: center;
    }

    .feature-btn:hover {
        transform: scale(1.05);
        background: linear-gradient(to right, #64ffda, #7f5af0);
        box-shadow: 0 6px 20px rgba(127, 90, 240, 0.4);
    }

    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.4rem;
        }

        .feature-title {
            font-size: 1.6rem;
        }

        .feature-box {
            padding: 2rem 1.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# HERO SECTION
st.markdown('''
<div class="hero-container">
    <div class="hero-title">✨ Welcome to ResuGenius</div>
    <div class="hero-subtitle">Your smart assistant for building standout, ATS-optimized resumes</div>
</div>
''', unsafe_allow_html=True)

# FEATURE CARDS
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
        <div class="feature-box">
            <div class="feature-title">📂 ATS Resume Checker</div>
            <div class="feature-desc">
                Upload up to 20 resumes and match them with a job description.
                Receive ATS scores, keyword analysis, and detailed AI insights.
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/ats.py", label="ATS Checker →", icon="📂")

with col2:
    st.markdown("""
        <div class="feature-box">
            <div class="feature-title">🧠 AI Resume Builder</div>
            <div class="feature-desc">
                Generate personalized, job-tailored resumes using generative AI.
                Save time and stand out with a professional resume in seconds.
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/resume_builder.py", label="Start Building →", icon="🧠")

# FOOTER
st.markdown("""
    <br><hr style='border: 1px solid #555;'>
    <div style='text-align:center; color: #aaa;'>
        &copy; 2025 ResuGenius | Smart Resume Tools powered by AI
    </div>
""", unsafe_allow_html=True)

#if st.button("ATS Checker →"):
#    st.switch_page("pages/ats.py")

#if st.button("Start Building →"):
#    st.switch_page("pages/resume_builder.py")



