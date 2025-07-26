# 🔐 Malicious URL Detection

SafeLink Analyzer is an AI-powered web-based tool designed to detect malicious and phishing URLs with high accuracy. This project combines machine learning models with an interactive Streamlit interface, allowing users to analyze links in real-time while offering features such as PDF report generation, screen sharing, voice and screen recording, and UI customization.

---

## 🚀 Features

- ✅ **Detect Fake or Real URLs** using a trained Machine Learning model.
- 🌐 **Streamlit Web App** for an intuitive and responsive frontend.
- 🧠 **AI-Driven Prediction** for accurate classification of URLs.
- 📄 **Save Results as PDF** to keep a record of predictions and analysis.
- 🔁 **Clear Cache** functionality for fresh sessions.
- 🎨 **Custom Themes & Text Color** options for accessibility and personalization.
- 🖥️ **Screen Sharing** for collaborative analysis or demos.
- 🎙️ **Record Voice & Screen** while interacting with the tool — useful for tutorials, walkthroughs, or training sessions.
- ☁️ **Free Deployment** on platforms like Streamlit Cloud.

---

## 🧠 How It Works

1. The user inputs a URL (e.g., `https://example.com`).
2. Feature extraction is done from the URL (e.g., length, presence of special characters, domain age).
3. The extracted features are passed into a Machine Learning model (e.g., Random Forest, SVM).
4. The model predicts whether the URL is **legitimate** or **malicious**.
5. Users can interact with the prediction results and export them as a **PDF report**.

---

## 📦 Tech Stack

| Layer       | Technologies |
|-------------|--------------|
| 🧠 AI/ML     | Scikit-learn, Pandas, NumPy |
| 🖥️ Frontend  | Streamlit |
| 📁 Backend   | Python |
| 📊 Model     | Trained ML Classifier (e.g., Random Forest) |
| 📃 Output    | PDF generation using `fpdf` / `reportlab` |
| 📺 Extras    | Screen recorder, voice capture (via browser extensions or Python wrappers) |

---

## 📷 Screenshots

| Interface Page | PDF Report | Theme Customization | Output |
|------------------|------------|----------------------| ----------------------|
| ![1](https://github.com/22H51A6675/malicious-url-detector/blob/f1fd4c29e5dec1fe15e17c9a4e5fca141915fd8b/Interface.png) | ![2](https://github.com/22H51A6675/malicious-url-detector/blob/febfde5704f56e008f88ed235654d77a8a0d305d/save_as_pdf.png) | ![3](https://github.com/GunjalaSiddartha/SafeLink-Analyzer/blob/64e21b9aee55ed5cd50f3eab8800881c4a1308ca/features_theme.png) | ![3](https://github.com/22H51A6675/malicious-url-detector/blob/b4682a18c4e214684e32010449df7f921448edb8/output.png) |


---

## 🛠️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com//22H51A6675/malicious-url-detector.git
cd malicious-url-detector

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run Main.py
