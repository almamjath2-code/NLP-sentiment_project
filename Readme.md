# 😊 SentimentScope AI Project

# 📌 Overview

SentimentScope AI is a Machine Learning and NLP-based web application that predicts sentiment from user text.

The application classifies text into:

- Positive 😊
- Negative 😡
- Neutral 😐

The project includes text preprocessing, TF-IDF feature engineering, machine learning model training, FastAPI backend development, Docker containerization, AWS deployment, and CI/CD automation using GitHub Actions.

---

# 🌐 Live Demo
http://sentimentscope-ai.s3-website.ap-south-1.amazonaws.com


# 🐳 Dockerized Application

This project is fully containerized using Docker to provide:

- Consistent runtime environment
- Easy deployment
- No dependency conflicts
- Cloud-ready infrastructure

# 📦 Run Using Docker

# 1️⃣ Build Docker Image

```bash
docker build -t sentimentscope-ai .
```

# 2️⃣ Run Docker Container

```bash
docker run -p 8080:8080 sentimentscope-ai
```

# 📄 Sample Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080"]
```

---

# ☁️ Deployment (AWS + Docker)

# 🌐 Frontend

- Hosted on AWS S3 Static Website Hosting
- Built using HTML, CSS, JavaScript

# ⚙️ Backend API

- Built using FastAPI
- Containerized using Docker
- Deployed on AWS Elastic Beanstalk

# 🚀 Deployment Flow

```text
GitHub Repository
      ↓
GitHub Actions CI/CD
      ↓
Docker Build
      ↓
AWS Elastic Beanstalk
      ↓
Backend API Running
      ↓
Frontend (S3) calls API
```

---

# 🗂 Dataset

The dataset contains text reviews, comments, and user opinions.

# 🎯 Target Labels

- Positive
- Negative
- Neutral

---

# 🛠 Tools & Technologies

- Python
- Pandas
- NumPy
- NLTK
- Scikit-learn
- FastAPI
- Joblib
- Docker
- AWS S3
- AWS Elastic Beanstalk
- GitHub Actions

---

# 🧹 Text Preprocessing

The preprocessing pipeline includes:

- Lowercasing text
- Removing HTML tags
- Expanding contractions
- Removing special characters
- Stopword removal
- Lemmatization
- Text normalization

---

# 📊 Exploratory Data Analysis (EDA)

- Sentiment distribution analysis
- Word frequency analysis
- WordCloud visualization
- Text length analysis
- Common keyword analysis

---

# 🤖 Machine Learning Model

# 📌 Feature Engineering

```python
TfidfVectorizer()
```

# 📌 Model Used

```python
LinearSVC()
```

---

# 📈 Model Performance

| Dataset | Accuracy | Precision | Recall | F1-Score |
|----------|-----------|------------|---------|-----------|
| Train | 0.7394 | 0.7414 | 0.7110 | 0.7197 |
| Test | 0.7114 | 0.7081 | 0.6802 | 0.6882 |

# ✅ Result

Good model performance with minimal overfitting.

---

# 🚀 Web Application

Interactive AI-powered sentiment prediction application.

# 📌 Features

- Real-time sentiment prediction
- FastAPI REST API
- Responsive frontend UI
- Dockerized backend
- AWS cloud deployment

---

# ⚙️ API Endpoint

# 📌 Predict Sentiment

## POST `/predict`

# Request

```json
{
  "text": "I love this project"
}
```

# Response

```json
{
  "text": "I love this project",
  "prediction": "Positive 😊"
}
```

---

# 📥 NLTK Setup

Run once before using the application:

```python
import nltk

nltk.download('stopwords')
nltk.download('wordnet')
```

---

# 📈 Project Workflow

- Load dataset
- Data preprocessing
- Text cleaning
- Stopword removal
- Lemmatization
- TF-IDF vectorization
- Model training
- Model evaluation
- Docker containerization
- AWS deployment
- Frontend integration

---

# 💡 Key Insights

- Text preprocessing improves model accuracy
- Emotional keywords strongly affect predictions
- Neutral sentences are less expressive
- TF-IDF improves feature representation

---

# 🔄 CI/CD Automation

This project uses GitHub Actions for automatic deployment.

# 🚀 CI/CD Flow

```text
Git Push
   ↓
GitHub Actions
   ↓
Build Docker Container
   ↓
Deploy to AWS Elastic Beanstalk
```

---

# ⚡ Future Improvements

- Add BERT / Transformer models
- Improve emoji detection
- Add multilingual sentiment support
- Add user authentication
- Deploy using Kubernetes
- Add monitoring dashboard

---

# 📁 Project Structure

```text
sentiment_analysis_project/
│
├── backend/
│   ├── api.py
│   ├── clean_text.py
│   ├── clean_lemmitezer.py
│   ├── sentiment_model.pkl
│   ├── tfidf_vectorizer.pkl
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   └── index.html
│
├── .github/
│   └── workflows/
│       └── frontend deploy.yml
│       └── backend deploy.yml
└── README.md
```

---

# 🤝 Contributing

- Fork repository
- Create feature branch
- Commit changes
- Push branch
- Create Pull Request

---

# 📜 License

MIT License

---

# 👨‍💻 Author

## Amjath

- AI & NLP Developer
- FastAPI Developer
- Machine Learning Enthusiast

# 🌐 GitHub

:https://github.com/almamjath2-code/NLP-sentiment_project.git

# 📧 Email

almamjath2@gmail.com