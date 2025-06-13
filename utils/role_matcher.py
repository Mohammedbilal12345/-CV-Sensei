from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

job_roles = {
    "Data Scientist": "Analyze large datasets, build statistical models, visualize insights, and communicate data-driven decisions.",
    "Frontend Developer": "Build beautiful, responsive UIs using HTML, CSS, JavaScript, React, or Angular.",
    "Backend Developer": "Design scalable APIs, manage databases, and implement core logic using Node.js, Python, or Java.",
    "AI/ML Engineer": "Train, tune, and deploy machine learning and deep learning models in production.",
    "Product Manager": "Define product vision, prioritize features, and collaborate with engineering and design teams.",
    "DevOps Engineer": "Automate CI/CD pipelines, manage cloud infrastructure using AWS, Azure, or GCP, and ensure system reliability.",
    "Cloud Architect": "Design scalable cloud-native solutions, select appropriate services, and optimize cost/performance on cloud platforms.",
    "Mobile App Developer": "Develop native and cross-platform apps using Swift, Kotlin, Flutter, or React Native.",
    "Full Stack Developer": "Work on both frontend and backend of web apps, using technologies like MERN or Django + React.",
    "Cybersecurity Analyst": "Identify vulnerabilities, implement protection mechanisms, and monitor threats to secure infrastructure.",
    "Data Engineer": "Build data pipelines, transform and process data using tools like Spark, Airflow, and SQL.",
    "UI/UX Designer": "Design user flows, wireframes, and interfaces with tools like Figma, Adobe XD, focusing on user experience.",
    "Blockchain Developer": "Build decentralized apps, smart contracts using Solidity, and work on Ethereum or other blockchains.",
    "Game Developer": "Develop immersive gaming experiences using Unity or Unreal Engine, with strong knowledge of C# or C++.",
    "Business Analyst": "Gather requirements, analyze trends, and support decision-making using BI tools like Power BI or Tableau.",
    "QA Engineer": "Create automated/manual test plans, write scripts using Selenium or Cypress, and ensure software quality.",
}


def match_resume_to_roles(resume_text, top_n=3):
    resume_embedding = model.encode([resume_text])[0]

    scores = []
    for role, desc in job_roles.items():
        role_embedding = model.encode([desc])[0]
        similarity = cosine_similarity([resume_embedding], [role_embedding])[0][0]
        scores.append((role, round(similarity * 100, 2)))

    return sorted(scores, key=lambda x: x[1], reverse=True)[:top_n]
