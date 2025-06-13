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
