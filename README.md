# 🤖 Sentiment Analysis Web App — IMDB Movie Reviews

**Develop by : Kevin Marakana**

**Dataset** : https://drive.google.com/drive/folders/1_B5cgYB7J6W5KDQeYgLEWIeWbAdglFhc?usp=sharing
This project is an AI-powered Sentiment Analysis web application built using machine learning techniques on the IMDB movie reviews dataset. Users can input any movie review and receive real-time predictions (Positive or Negative) with high accuracy.

![image1](https://github.com/user-attachments/assets/aaa05ce7-9c6b-4de9-b340-44fbac2ea3da)

---

## 📌 Project Overview

- 🧠 Machine Learning Models: Logistic Regression, Naive Bayes, Random Forest, SVM
- 📈 Best Accuracy: 88.01% using Logistic Regression
- 🧰 Tech Stack: Python, scikit-learn, NLTK, Flask, HTML/CSS (Tailwind), Jupyter
- 🌐 Web App: Lightweight Flask application for live predictions

---

## 📊 Dataset

- Name: IMDB Dataset
- Size: 50,000 labeled movie reviews (balanced)
- Format: CSV with columns — review (text), sentiment (positive/negative)

---

## 🧠 Model Performance Summary

| Model                | Accuracy | F1 Score |
|---------------------|----------|----------|
| Logistic Regression | 0.8801   | 0.8829   |
| SVM                 | 0.8731   | 0.8756   |
| Naive Bayes         | 0.8458   | 0.8477   |
| Random Forest       | 0.8429   | 0.8428   |

✅ Final Model: Logistic Regression

---

## 🧮 Confusion Matrices

| Model                | True Neg | False Pos | False Neg | True Pos |
|---------------------|----------|-----------|-----------|----------|
| Logistic Regression | 4281     | 680       | 519       | 4520     |
| Naive Bayes         | 4168     | 793       | 749       | 4290     |
| Random Forest       | 4218     | 743       | 828       | 4211     |
| SVM                 | 4266     | 695       | 574       | 4465     |

---

## 🧪 Classification Report (Logistic Regression)

| Class | Precision | Recall | F1-Score |
|-------|-----------|--------|----------|
| 0     | 0.89      | 0.86   | 0.88     |
| 1     | 0.87      | 0.90   | 0.88     |

- Overall Accuracy: 0.88
- Macro Avg: 0.88
- Weighted Avg: 0.88

---


