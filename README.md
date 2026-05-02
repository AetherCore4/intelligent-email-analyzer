# 📩 Intelligent Email Analyzer

### 🚀 AI-Powered Spam Detection System

An intelligent web application that analyzes email content and classifies it as **Spam 🚨 or Not Spam (Ham) ✅** using Machine Learning.

Designed with a clean UI and built to demonstrate **end-to-end ML deployment** — from training → backend → live web app.

---

## 🌐 Live Demo

🔗 **Try it here:**
👉 https://intelligent-email-analyzer-ovjx.onrender.com

---

## 📸 Preview

<img width="1895" height="944" alt="image" src="https://github.com/user-attachments/assets/bb8ceaf7-8505-46bd-85cf-ead2f370a728" />
<img width="1890" height="947" alt="image" src="https://github.com/user-attachments/assets/ab63b746-832d-4912-a865-f2984a384f05" />

---

## ✨ Key Highlights

* 🧠 Machine Learning–based spam detection
* ⚡ Real-time analysis with instant results
* 📊 Confidence score visualization
* 🔍 Keyword insights (important words detected)
* 🎨 Modern, responsive UI
* 🌍 Fully deployed web application

---

## 🧠 How It Works (Behind the Scenes)

1. **Input Processing**
   User enters email/message text

2. **Text Cleaning**

   * Lowercasing
   * Removing special characters
   * Normalizing spaces

3. **Feature Extraction**

   * TF-IDF vectorization converts text → numerical form

4. **Prediction Engine**

   * Trained ML model classifies message

5. **Result Display**

   * Spam / Ham label
   * Confidence score
   * Key indicator words

---

## 🛠️ Tech Stack

| Layer      | Technology            |
| ---------- | --------------------- |
| Frontend   | HTML, CSS, JavaScript |
| Backend    | Flask (Python)        |
| ML Model   | Scikit-learn          |
| NLP        | TF-IDF Vectorizer     |
| Deployment | Render                |

---

## 📂 Project Structure

```text id="projstruct1"
Intelligent_Email_Analyzer/
│
├── app.py                 # Flask backend server
├── model.pkl             # Trained ML model
├── vectorizer.pkl        # TF-IDF vectorizer
├── requirements.txt      # Dependencies
├── Procfile              # Deployment config
├── runtime.txt           # Python version (for Render)
│
└── templates/
    └── index.html        # Frontend UI
```

---

## ⚙️ Local Setup

Clone the repository and run locally:

```bash id="setup1"
git clone https://github.com/YOUR_USERNAME/intelligent-email-analyzer.git
cd intelligent-email-analyzer
pip install -r requirements.txt
python app.py
```

Open in browser:

```text id="setup2"
http://127.0.0.1:5000
```

---

## 🚀 Deployment

This project is deployed on **Render**.

### Steps:

1. Push project to GitHub
2. Connect repository to Render
3. Set:

   * Build Command → `pip install -r requirements.txt`
   * Start Command → `python app.py`
4. Add `runtime.txt` for Python version
5. Deploy 🚀

---

## 📊 Features in Action

* Detects spam patterns like:

  * “win money”, “free tickets”, “lottery”
* Handles normal conversational text
* Provides confidence level for transparency

---

## ⚠️ Limitations

* Model accuracy depends on training dataset
* May misclassify ambiguous messages
* Uses traditional ML (not deep learning yet)

---

## 🔮 Future Improvements

* 🤖 Upgrade to transformer-based models (BERT)
* 📧 Email inbox integration
* 📈 Continuous learning from user feedback
* 🌐 REST API for external usage
* 📊 Advanced analytics dashboard

---

## ⭐ Support

If you found this project useful:

👉 Star the repository
👉 Share with others
👉 Build on top of it

---

## 💡 Inspiration

This project was built to understand how **AI models connect with real-world applications**, bridging the gap between theory and deployment.

---

## 📜 License

This project is licensed under the MIT License.
