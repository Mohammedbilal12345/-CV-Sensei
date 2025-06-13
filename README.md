<<<<<<< HEAD
## 🧰 Tech Stack Used

| Tool/Library                          | Purpose                                                                 |
|--------------------------------------|-------------------------------------------------------------------------|
| **Streamlit**                        | Web app framework for interactive dashboards                           |
| **pdfplumber**                       | Extracts resume content from PDFs                                      |
| **fitz (PyMuPDF)**                   | High-fidelity PDF parsing                                              |
| **docx**                             | Parse `.docx` resumes (optional support)                               |
| **FPDF**                             | Generate downloadable PDF ATS reports                                  |
| **unicodedata / unicodedata2**       | Normalize text to clean Unicode characters                            |
| **language_tool_python**             | Grammar checking using LanguageTool engine                             |
| **transformers (HuggingFace)**       | Load summarization models (e.g., `facebook/bart-large-cnn`)            |
| **sentence-transformers**            | Create semantic vector embeddings of resumes and job roles             |
| **scikit-learn** (`cosine_similarity`) | Compute similarity for job match scoring                             |
| **spaCy**                            | Optional NLP tasks (entity recognition, POS tagging, etc.)             |
| **torch**                            | Required by `transformers` and `sentence-transformers`                 |
=======
# 📄 CV Sensei – AI-Powered Resume Analyzer

> An intelligent resume analyzer offering ATS score, job match insights, grammar fixes, keyword analysis & summaries – powered by NLP, Hugging Face, and Streamlit.

![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-orange?logo=streamlit)
![Python](https://img.shields.io/badge/Made%20with-Python-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Open Source](https://badgen.net/badge/Open%20Source/Yes/green)

---

## 🚀 Key Features

* 📄 **Smart Resume Parsing** (PDF/DOCX)
* 🧠 **AI Summarization** using Hugging Face models (BART/T5)
* ✍️ **Grammar Correction** powered by LanguageTool
* 🎯 **ATS Score Calculation** for job-readiness insights
* 🔍 **Keyword Extraction & Highlighting**
* 🤝 **Job Description Matching** via semantic similarity
* 📥 **Downloadable PDF Report** with feedback
* ✨ **Sleek Streamlit UI with 3D effects**

---

## 🌐 Live Preview & Demo Screenshots

📍 GitHub Repo: [CV Sensei](https://github.com/Mohammedbilal12345/-CV-Sensei/)

| Upload Resume                                                                              | ATS Score                                                                               | Summary & Keywords                                                                           | Grammar Suggestions                                                                         |
| ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| ![Upload](https://github.com/user-attachments/assets/7568c420-8958-425b-825c-e59fb7a7c2ef) | ![ATS](https://github.com/user-attachments/assets/1b90b00b-e974-4a44-9b82-9375cb44b63f) | ![Keywords](https://github.com/user-attachments/assets/971af84b-1112-44c7-9cd1-71e931704b6b) | ![Grammar](https://github.com/user-attachments/assets/53a51c62-e321-4f1b-ae45-04f35f1701f1) |

---

## 📂 Project Structure

```bash
📁 CV-Sensei/
├── 📄 app.py                        # Main Streamlit app script
├── 📄 grammar_test.py              # Grammar check test script
├── 📄 README.md                    # Project documentation

├── 📁 .streamlit/
│   └── 📄 config.toml              # Streamlit configuration

├── 📁 assets/
│   └── 🖼️ logo.png                 # Project logo

├── 📁 data/
│   └── 📄 sample_resume.pdf        # Sample resume input

├── 📁 generated_reports/
│   └── 📄 ats_report.pdf           # Output report PDF

├── 📁 styles/
│   └── 🎨 custom.css               # Custom 3D glowing UI styles

├── 📁 utils/
│   ├── 📄 ats_score.py             # Calculates ATS score
│   ├── 📄 grammar_checker.py      # Grammar correction logic
│   ├── 📄 pdf_generator.py        # Generates styled PDF reports
│   ├── 📄 resume_parser.py        # Extracts text from PDF/DOCX
│   ├── 📄 role_matcher.py         # Job match logic (cosine similarity)
│   └── 📄 summary_generator.py    # Summarizes resume content using Hugging Face

└── 📁 __pycache__/                # Python cache (auto-generated)

```

---

## 🧠 Tech Stack

| Tool / Library            | Role / Purpose                             |
| ------------------------- | ------------------------------------------ |
| **Streamlit**             | Frontend UI framework                      |
| **pdfplumber / PyMuPDF**  | Extract text from PDF resumes              |
| **python-docx**           | Extract text from DOCX resumes             |
| **fpdf**                  | PDF report generation                      |
| **language-tool-python**  | Grammar correction                         |
| **transformers**          | Text summarization via Hugging Face models |
| **sentence-transformers** | Job-resume matching via embeddings         |
| **scikit-learn**          | Cosine similarity & ML utilities           |
| **torch**                 | Backend for transformer models             |
| **spaCy** (optional)      | NER, text preprocessing                    |
| **unicodedata2**          | Handling unicode text from parsed resumes  |

---

## ⚙️ Installation & Usage

```bash
# 1. Clone the repository
$ git clone https://github.com/Mohammedbilal12345/-CV-Sensei.git
$ cd cv-sensei

# 2. Install dependencies
$ pip install -r requirements.txt

# 3. Launch the app
$ streamlit run app.py
```

---

## 📌 Example Workflow

1. Upload your resume (PDF/DOCX)
2. View extracted text, grammar feedback & keyword suggestions
3. Get ATS score and job match percentage
4. Download AI-generated PDF report

---

## 📜 Requirements

```txt
streamlit
pdfplumber
PyMuPDF
python-docx
fpdf
language-tool-python
transformers
sentence-transformers
scikit-learn
spacy
torch
unicodedata2
```

---

## 📬 Contact & Author

**👤 Mohammed Bilal**
📧 [mohammedbilal96654@gmail.com](mailto:mohammedbilal96654@gmail.com)
🌐 [Portfolio Website](https://mohammedbilal.vercel.app/)
🔗 [GitHub](https://github.com/Mohammedbilal12345)

---

## ⭐ Like this Project?

If this helped you or inspired you, give it a star ⭐ and share with others!

> Empower your resume with AI. Get smarter job matches with **CV Sensei**.

---

© 2025 Mohammed Bilal – All Rights Reserved. Licensed under MIT.
>>>>>>> 38b13a9440097a455de1b954b1d35cf17c29141d
