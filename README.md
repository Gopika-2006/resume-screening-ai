# 🧠 AI-powered Resume Screening and Ranking System

This project is an AI-driven web application that automates the resume screening process using Natural Language Processing (NLP) and semantic similarity techniques. It helps recruiters identify the most relevant candidates based on job descriptions and resumes.

## 🚀 Features

- 📄 Upload multiple resumes (PDF/DOCX format)
- 🧠 Extract key information using NLP
- 🤖 Match resumes with job descriptions using cosine similarity / BERT
- 📊 Rank candidates based on relevance scores
- 🖥️ Simple web dashboard for recruiters

## 🔧 Technologies Used

- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Python, Flask
- **NLP Libraries:** spaCy, NLTK, scikit-learn, transformers
- **PDF Parsing:** PyMuPDF / pdfminer.six
- **Similarity Calculation:** TF-IDF, cosine similarity, (optional: BERT embeddings)
- **Database (Optional):** SQLite / MongoDB

## 🛠 How to Run the Project Locally

1. **Clone the repository**
```bash
git clone https://github.com/your-username/resume-screening-ai.git
cd resume-screening-ai
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the Flask app**
```bash
python app.py
```

4. **Open in Browser**
```
http://127.0.0.1:5000
```

## 📸 Screenshots

(Add screenshots in a `/screenshots` folder and embed them here)

## 📁 Folder Structure

```
resume-screening-ai/
├── app.py
├── parser.py
├── ranker.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── resumes/
```

## ✅ Future Enhancements

- Use BERT or SBERT for better semantic understanding
- Add login system for recruiters
- Store previous searches and scores in a database
- Resume feedback or score explanation module

## 📬 Contact

- **Author:** [Your Name]
- **Email:** your.email@example.com
- **GitHub:** [https://github.com/your-username](https://github.com/your-username)

## 📃 License

This project is open-source under the [MIT License](LICENSE).
