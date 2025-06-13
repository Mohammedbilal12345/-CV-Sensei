# import streamlit as st
# from PIL import Image
# import os
# from base64 import b64encode
# from utils.resume_parser import extract_text_from_pdf
# from utils.grammar_check import check_grammar
# from utils.role_matcher import match_resume_to_roles
# from utils.summary_generator import generate_summary
# from utils.ats_score import calculate_ats_score
# from utils.pdf_generator import generate_ats_report_pdf

# st.set_page_config(page_title="CV Sensei", page_icon="📄", layout="wide")

# # -------------------------------
# # 🎨 Custom CSS Loader (UTF-8 fix)
# # -------------------------------
# def load_css(file_path):
#     if os.path.exists(file_path):
#         with open(file_path, encoding="utf-8") as f:  # ✅ UTF-8 fix
#             st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
#     else:
#         st.warning(f"⚠️ CSS file not found: {file_path}")

# load_css("styles/custom.css")

# # -------------------------------
# # 🖼️ Logo Display
# # -------------------------------
# def image_to_base64(image_path):
#     with open(image_path, "rb") as img_file:
#         return b64encode(img_file.read()).decode()

# def display_logo(path, width=140):
#     if os.path.exists(path):
#         b64_img = image_to_base64(path)
#         st.markdown(
#             f"""
#             <div style='text-align:center; padding: 10px;'>
#                 <img src='data:image/png;base64,{b64_img}' width='{width}' style='border-radius:15px; box-shadow: 0px 4px 12px rgba(0,0,0,0.1);' />
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

# # -------------------------------
# # 📄 Layout
# # -------------------------------
# st.markdown("<h2 class='gradient-text'>📄 CV Sensei – Your AI Resume Mentor</h2>", unsafe_allow_html=True)
# st.markdown("<h5>Upload your resume and get AI-powered insights</h5>", unsafe_allow_html=True)

# col1, col2 = st.columns([1, 2])

# with col1:
#     display_logo("assets/logo.png")
#     uploaded_file = st.file_uploader("📤 Upload Resume (PDF only)", type=["pdf"])

# with col2:
#     if uploaded_file:
#         st.success("✅ Resume uploaded successfully!")
#         resume_text = extract_text_from_pdf(uploaded_file)

#         if resume_text:
#             st.subheader("📝 Extracted Resume Text")
#             st.text_area("Your Resume Content:", resume_text, height=300)

#             st.subheader("🧠 Professional Summary")
#             summary = generate_summary(resume_text)
#             st.info(summary)

#             st.subheader("🛠️ Grammar Feedback")
#             grammar_issues = check_grammar(resume_text)
#             if grammar_issues:
#                 for i, issue in enumerate(grammar_issues):
#                     st.markdown(f"""
#                     <div class='animated-block block'>
#                         <b>🔴 Issue {i+1}:</b> {issue['error']}<br>
#                         <b>Suggestions:</b> {', '.join(issue['suggestions']) or 'N/A'}<br>
#                         <i>Sentence:</i> {issue['sentence'].strip()}
#                     </div>
#                     """, unsafe_allow_html=True)
#             else:
#                 st.success("✅ No grammar issues found!")

#             st.subheader("🎯 Role Match Suggestions")
#             role_matches = match_resume_to_roles(resume_text, top_n=5)
#             if role_matches:
#                 for role, score in role_matches:
#                     st.markdown(f"**🧠 {role}** – Match Score: **{score}%**")
#                     st.progress(score / 100)
#             else:
#                 st.warning("⚠️ No matching roles found.")

#             st.subheader("📊 ATS Score Estimate")
#             ats_score, keyword_matches = calculate_ats_score(resume_text)
#             st.markdown(f"<span class='ats-score-tag'>Your ATS Score is: {ats_score}%</span>", unsafe_allow_html=True)  # ✅ Fix here
#             st.progress(ats_score / 100)

#             st.markdown("### ✅ Keywords Detected:")
#             st.markdown(", ".join(keyword_matches) if keyword_matches else "❌ No important keywords matched.")

#             # 🔽 Download ATS PDF Report
#             expected_keywords = keyword_matches  # Replace with real expected keywords if different
#             pdf_path = "generated_reports/ats_report.pdf"
#             os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
#             generate_ats_report_pdf(
#                 pdf_path,
#                 ats_score,
#                 summary,
#                 grammar_issues,
#                 keyword_matches,
#                 list(set(expected_keywords) - set(keyword_matches))
#             )

#             with open(pdf_path, "rb") as f:
#                 st.download_button(
#                     label="📥 Download ATS Report PDF",
#                     data=f.read(),
#                     file_name="ATS_Report_CV_Sensei.pdf",
#                     mime="application/pdf"
#                 )

#         else:
#             st.warning("⚠️ No readable text found in the PDF.")
#     else:
#         st.info("👆 Please upload a PDF resume to begin.")
import streamlit as st
from PIL import Image
import os
from base64 import b64encode
from utils.resume_parser import extract_text_from_pdf
from utils.grammar_check import check_grammar
from utils.role_matcher import match_resume_to_roles
from utils.summary_generator import generate_summary
from utils.ats_score import calculate_ats_score
from utils.pdf_generator import generate_ats_report_pdf

st.set_page_config(page_title="CV Sensei", page_icon="📄", layout="wide")

# -------------------------------
# 🎨 Load Custom CSS
# -------------------------------
def load_css(file_path):
    if os.path.exists(file_path):
        with open(file_path, encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.warning(f"⚠️ CSS file not found: {file_path}")

load_css("styles/custom.css")

# -------------------------------
# 🖼️ Convert Image to Base64
# -------------------------------
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return b64encode(img_file.read()).decode()

# -------------------------------
# 🏗️ Hero Section
# -------------------------------
with st.container():
    st.markdown("""
        <div class='hero-container'>
            <div class='hero-card'>
                <img src='data:image/png;base64,{}' class='logo'/>
                <h1 class='main-heading'>📄 CV Sensei</h1>
                <p class='sub-heading'>Your AI Resume Mentor</p>
                <label for='file-upload' class='custom-upload'>📤 Upload Your Resume (PDF only)</label>
            </div>
        </div>
    """.format(image_to_base64("assets/logo.png")), unsafe_allow_html=True)

    uploaded_file = st.file_uploader("📤 Upload Your Resume (PDF only)", type=["pdf"], label_visibility="collapsed")

st.markdown("---")

# -------------------------------
# 🔍 Resume Processing
# -------------------------------
if uploaded_file:
    st.success("✅ Resume uploaded successfully!")
    resume_text = extract_text_from_pdf(uploaded_file)

    if resume_text:
        st.markdown("<h3 class='section-heading'>🔍 Resume Insights Dashboard</h3>", unsafe_allow_html=True)

        st.markdown("### 📝 Extracted Resume Text")
        st.text_area("Your Resume Content:", resume_text, height=300)

        st.markdown("### 🧠 Professional Summary")
        summary = generate_summary(resume_text)
        st.info(summary)

        st.markdown("### 🛠️ Grammar Feedback")
        grammar_issues = check_grammar(resume_text)
        if grammar_issues:
            for i, issue in enumerate(grammar_issues):
                st.markdown(f"""
                <div class='animated-block block'>
                    <b>🔴 Issue {i+1}:</b> {issue['error']}<br>
                    <b>Suggestions:</b> {', '.join(issue['suggestions']) or 'N/A'}<br>
                    <i>Sentence:</i> {issue['sentence'].strip()}
                </div>
                """, unsafe_allow_html=True)
        else:
            st.success("✅ No grammar issues found!")

        st.markdown("### 🎯 Role Match Suggestions")
        role_matches = match_resume_to_roles(resume_text, top_n=5)
        if role_matches:
            for role, score in role_matches:
                st.markdown(f"**🧠 {role}** – Match Score: **{score}%**")
                st.progress(score / 100)
        else:
            st.warning("⚠️ No matching roles found.")

        colA, colB = st.columns(2)

        with colA:
            st.markdown("### 📊 ATS Score")
            ats_score, keyword_matches = calculate_ats_score(resume_text)
            st.markdown(f"<span class='ats-score-tag'>Your ATS Score is: {ats_score}%</span>", unsafe_allow_html=True)
            st.progress(ats_score / 100)

        with colB:
            st.markdown("### ✅ Keywords Detected")
            st.markdown(", ".join(keyword_matches) if keyword_matches else "❌ No important keywords matched.")

        pdf_path = "generated_reports/ats_report.pdf"
        os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
        expected_keywords = keyword_matches

        generate_ats_report_pdf(
            pdf_path,
            ats_score,
            summary,
            grammar_issues,
            keyword_matches,
            list(set(expected_keywords) - set(keyword_matches))
        )

        with open(pdf_path, "rb") as f:
            st.download_button(
                label="📥 Download ATS Report PDF",
                data=f.read(),
                file_name="ATS_Report_CV_Sensei.pdf",
                mime="application/pdf"
            )
    else:
        st.warning("⚠️ No readable text found in the PDF.")
else:
    st.info("👆 Please upload a PDF resume to begin.")
