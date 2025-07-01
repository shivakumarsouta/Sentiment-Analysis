# 🧠 Sentiment Analyzer Web App

A simple yet effective web application built with **Flask** and **TextBlob** that analyzes the sentiment of user-provided text. This app evaluates whether the sentiment is **Positive**, **Negative**, or **Neutral**, and displays it with a matching emoji.

---

## 🚀 Features

* 🌐 User-friendly web interface (HTML frontend via `index.html`)
* 🧾 Analyzes sentiment using `TextBlob`'s polarity scoring
* 🤖 Returns a clear sentiment classification:

  * Positive 😊
  * Negative 😠
  * Neutral 😐
* 📝 Accepts input via a form and dynamically displays results on the same page

---

## 🛠️ Technologies Used

* **Python 3.x**
* **Flask** – Micro web framework for handling HTTP routes
* **TextBlob** – NLP library for sentiment analysis
* **HTML (Jinja2)** – For rendering the frontend

---

## 📂 File Structure

```
project/
│
├── app.py               # Main Flask app
├── requirements.txt     # List of requirements
├── templates/
│   └── index.html       # HTML template for the web interface
├── static/
│   └── background.png
│   └── favicon.ico
└── README.md            # You're reading it!
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/shivkumars005/Sentiment-Analysis.git
cd sentiment-analysis
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist yet, just run:

```bash
pip install flask textblob
python -m textblob.download_corpora
```

### 4. Run the App

```bash
python app.py
```

Visit: `http://127.0.0.1:5000` in your browser.

---

## 🧪 Example Usage

**Input**:

> "I absolutely love this new phone!"

**Output**:

> Sentiment: Positive 😊
> Polarity: 0.625

---

## 📌 Notes

* `TextBlob` uses a simple rule-based sentiment analyzer; it's great for small demos and educational tools.
* For production-grade NLP, consider more advanced models (like BERT or GPT-based sentiment analysis via HuggingFace).

---

## 📬 Feedback

Got suggestions or improvements? Open an issue or fork the project and create a pull request!

---
