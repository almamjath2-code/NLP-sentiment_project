# 📘 Sentiment Analysis Project

# 📌 Project Overview

This project performs **Sentiment Analysis** using Natural Language Processing (NLP) to classify text into:

* Positive 😊
* Negative 😡
* Neutral 😐

The system uses text preprocessing, TF-IDF feature extraction, and a machine learning model (**LinearSVC**) to predict sentiment.

A **Streamlit web app** is built for real-time predictions.

---

# 🌐 Live Demo

👉 https://nlp-sentimentel-project-bqhuuhestxutsyvasprkf3.streamlit.app/

---

# 🗂 Dataset

* Text data (user reviews/comments)
* Target: Sentiment (Positive / Negative / Neutral)

---

# 🛠 Libraries & Modules Used

```python
import nltk
import pandas as pd
import contractions
import re                      # ✅ for text cleaning (regex)
from collections import Counter  # ✅ for word frequency
import matplotlib.pyplot as plt
from wordcloud import WordCloud

from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

import joblib
```

---

# ⚠️ Important Notes (Very Important)

* `re` and `collections` are **built-in Python modules** → ❌ do NOT add in `requirements.txt`
* `nltk.download()` → ❌ do NOT include in requirements
* These must be handled separately

---

# 📥 NLTK Setup

Run this **once before using the project**:

```python
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
```

---

# 🧹 Text Preprocessing

* Lowercasing text
* Removing HTML tags using `re`
* Expanding contractions (`don't → do not`)
* Removing special characters using regex (`re`)
* Removing stopwords
* Lemmatization using WordNet

---

# 📊 Exploratory Data Analysis (EDA)

* Class distribution
* Word frequency using `collections.Counter`
* WordCloud visualization ☁️
* Text length analysis

---

# 🧠 Feature Engineering

TF-IDF (Term Frequency - Inverse Document Frequency):

```python
TfidfVectorizer()
```

---

# 🤖 Model Training

Model Used: **Linear Support Vector Classifier (LinearSVC)**

Steps:

* Train/Test split
* Model training
* Prediction

---

# 📈 Model Performance

| Dataset | Accuracy | Precision | Recall | F1-Score |
| ------- | -------- | --------- | ------ | -------- |
| Train   | 0.7394   | 0.7414    | 0.7110 | 0.7197   |
| Test    | 0.7114   | 0.7081    | 0.6802 | 0.6882   |

✔ Good Fit (no overfitting)

---

# 📊 Confusion Matrix

Model performs well with small misclassification between similar sentiments.

---

# 💾 Model Saving

```python
joblib.dump(model, "sentiment_model.pkl")
joblib.dump(tfidf, "tfidf_vectorizer.pkl")
```

---

# 🌐 Application (sentiment_app.py)

Main application file: **sentiment_app.py**

## 📌 What it does:

* Load trained model
* Load TF-IDF vectorizer
* Accept user input
* Clean text (using `re` + preprocessing pipeline)
* Predict sentiment
* Display result (😊 😡 😐)

---

# ▶️ Run Application

```bash
pip install -r requirements.txt
streamlit run sentiment_app.py
```

---

# ⚙️ Requirements

```bash
pip install pandas nltk contractions scikit-learn matplotlib wordcloud joblib
```

---

# 📈 Project Workflow

* Load dataset
* Data cleaning (using `re`)
* Stopword removal
* Lemmatization
* EDA using `Counter`
* Feature extraction (TF-IDF)
* Model training
* Evaluation
* Deployment (Streamlit app)

---

# 💡 Insights

* Keywords strongly influence sentiment
* Negative texts contain strong emotional words
* Neutral texts are less expressive
* Preprocessing improves accuracy significantly

---

# ⚡ Future Improvements

* Use BERT / LSTM
* Improve emoji & slang handling
* Hyperparameter tuning
* Deploy to cloud

---

# 📁 Project Structure

sentiment_analysis_project/
│
├─ data/
├─ notebooks/
├─ sentiment_app.py
├─ sentiment_model.pkl
├─ tfidf_vectorizer.pkl
├─ requirements.txt
└─ README.md

---

# 👨‍💻 Author

**Amjath**
📧 [almamjath2@gmail.com](mailto:almamjath2@gmail.com)
