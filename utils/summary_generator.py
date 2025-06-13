import os
import fitz  # PyMuPDF
import docx
from transformers import pipeline

# Load Hugging Face summarizer model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def extract_text_from_pdf(file_path):
    """Extract text from a PDF file"""
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_docx(file_path):
    """Extract text from a DOCX file"""
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def generate_summary(resume_text):
    """Summarize resume text using Hugging Face"""
    try:
        if len(resume_text) > 2000:
            resume_text = resume_text[:2000]
        summary = summarizer(resume_text, max_length=80, min_length=30, do_sample=False)
        return summary[0]['summary_text'].strip()
    except Exception as e:
        return f"⚠️ Failed to summarize: {e}"

def handle_resume_upload(file_path):
    """Main function to handle file upload and summarize"""
    try:
        if file_path.endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        elif file_path.endswith(".docx"):
            text = extract_text_from_docx(file_path)
        else:
            return "❌ Unsupported file format. Only PDF and DOCX allowed."

        return generate_summary(text)
    except Exception as e:
        return f"❌ Error processing file: {e}"
