# 🛡️ Malicious URL Detection Using Deep Learning and Streamlit

This project is a real-time malicious website URL detector built using **deep learning (MLP)** and **Streamlit**. It predicts whether a given URL is **safe or malicious** based on its structure and character patterns.

> 📌 Hosted App (optional): *[Add your Streamlit Cloud or GitHub Pages link here]*  
> 📁 Repository: [github.com/22H51A6675/malicious-url-detector](https://github.com/22H51A6675/malicious-url-detector)

---

## 🎯 Objective

Phishing attacks are a common cybersecurity threat where attackers trick users using fake websites. The objective of this project is to:
- Detect malicious URLs using machine learning
- Build a user-friendly web app to scan URLs in real-time
- Help users avoid phishing websites

---

## ⚙️ Project Workflow

1. **Data Collection** – Gather safe and malicious URLs (labelled as 0 and 1)
2. **Feature Extraction** – Extract numeric features from each URL (length, digits, IP use, etc.)
3. **Model Training** – Train a Multilayer Perceptron (MLP) neural network
4. **Evaluation** – Use metrics like accuracy, precision, and recall
5. **Deployment** – Create a Streamlit-based web interface for real-time prediction

---
s
## 🧠 Machine Learning Models Used

| Model               | Accuracy |
|---------------------|--------- |
| Decision Tree       | 95%      |
| Random Forest       | 97%      |
| **Multilayer Perceptron (MLP)** | ✅ **99%** (Best performer) |

---

## 📁 Project Structure

<pre><code> malicious-url-detector/
│
├── API.py # Prediction logic
├── Url_Features.py # Functions to extract features from URL
├── Feature_Extractor.py # Assembles features from raw URL
├── Malicious_URL_Prediction.h5 # Trained deep learning model
├── Main.py or app.py # Streamlit user interface
├── README.md # Project documentation
└── requirements.txt # Python dependencies</code></pre>