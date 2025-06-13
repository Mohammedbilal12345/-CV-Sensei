# utils/ats_score.py

def calculate_ats_score(resume_text):
    # Dummy scoring logic – replace with real algorithm
    keywords = [
    # 🧠 Programming Languages
    "python", "java", "c", "c++", "c#", "javascript", "typescript", "go", "ruby", "swift", "kotlin", "php", "r",

    # 🧰 Web Development
    "html", "css", "react", "angular", "vue", "next.js", "node.js", "express", "bootstrap", "tailwind",

    # 📊 Data & Machine Learning
    "data analysis", "data science", "data engineering", "machine learning", "deep learning", "nlp",
    "computer vision", "pandas", "numpy", "matplotlib", "seaborn", "scikit-learn", "tensorflow", "pytorch",
    "excel", "tableau", "power bi", "sql", "nosql", "mongodb", "postgresql", "mysql", "snowflake", "hadoop", "spark",

    # ☁️ Cloud & DevOps
    "aws", "azure", "gcp", "cloud computing", "docker", "kubernetes", "ci/cd", "jenkins", "terraform", "ansible",
    "linux", "bash", "shell scripting", "git", "github", "bitbucket",

    # 🔌 APIs & System Design
    "rest", "api", "graphql", "websockets", "microservices", "system design", "scalable systems", "architecture",

    # 🧪 Testing & QA
    "unit testing", "integration testing", "test automation", "selenium", "pytest", "junit", "jest",

    # 📈 Project & Collaboration Tools
    "jira", "confluence", "trello", "notion", "slack", "figma", "miro", "asana",

    # 💼 Project Types & Context
    "web development", "mobile app", "backend development", "frontend development",
    "ecommerce", "portfolio", "dashboard", "crm", "erp", "saas", "startup", "agile", "scrum", "kanban",

    # 🧠 Soft Skills (ATS picks these too!)
    "problem solving", "communication", "teamwork", "leadership", "collaboration",
    "critical thinking", "time management", "creativity", "adaptability", "initiative", "mentorship"
]

    matched = [kw for kw in keywords if kw.lower() in resume_text.lower()]
    score = int((len(matched) / len(keywords)) * 100)
    return score, matched
