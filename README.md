# 🔐 Malicious URL Detection

 A real-time malicious URL detection system built using Deep Learning (MLP) and Streamlit. This project analyzes structural and lexical features of URLs to predict whether they are safe or malicious, helping protect users from phishing attacks and online threats. Includes a trained model, feature extractor, API logic, and a user-friendly web interface.

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
| ![1](https://github.com/22H51A6675/malicious-url-detector/blob/f1fd4c29e5dec1fe15e17c9a4e5fca141915fd8b/Interface.png) | ![2](https://github.com/22H51A6675/malicious-url-detector/blob/febfde5704f56e008f88ed235654d77a8a0d305d/save_as_pdf.png) | ![3](https://github.com/22H51A6675/malicious-url-detector/blob/be648c21d6065b96a5b5d6a7d4a371a7f86576b0/theme.png) | ![3](https://github.com/22H51A6675/malicious-url-detector/blob/b4682a18c4e214684e32010449df7f921448edb8/output.png) |


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
