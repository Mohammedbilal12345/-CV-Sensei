from fpdf import FPDF
import unicodedata

def clean_text(text):
    if not text:
        return ""
    try:
        return unicodedata.normalize('NFKD', text).encode('latin-1', 'ignore').decode('latin-1')
    except:
        return text.encode('ascii', 'ignore').decode('ascii')

def generate_ats_report_pdf(file_path, ats_score, summary, grammar_issues, matched_keywords, missing_keywords):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt=clean_text("CV Sensei – ATS Report"), ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", "B", size=12)
    pdf.cell(200, 10, txt=clean_text(f"ATS Score: {ats_score}%"), ln=True)

    pdf.set_font("Arial", size=12)
    pdf.ln(5)
    pdf.multi_cell(0, 10, txt=clean_text("Professional Summary:\n" + summary))

    if grammar_issues:
        pdf.ln(5)
        pdf.set_font("Arial", "B", size=12)
        pdf.cell(200, 10, txt=clean_text("Grammar Issues:"), ln=True)
        pdf.set_font("Arial", size=12)
        for issue in grammar_issues:
            error = clean_text(issue.get('error', ''))
            sentence = clean_text(issue.get('sentence', ''))
            suggestions = ', '.join(issue.get('suggestions', [])) or "N/A"
            pdf.multi_cell(0, 10, txt=clean_text(f"- {error} -> Suggestions: {suggestions}\n  Sentence: {sentence}"))

    pdf.ln(5)
    pdf.set_font("Arial", "B", size=12)
    pdf.cell(200, 10, txt=clean_text("Keywords Matched:"), ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, clean_text(", ".join(matched_keywords) if matched_keywords else "None"))

    pdf.ln(5)
    pdf.set_font("Arial", "B", size=12)
    pdf.cell(200, 10, txt=clean_text("Missing Keywords:"), ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, clean_text(", ".join(missing_keywords) if missing_keywords else "None"))

    pdf.output(file_path)
