from flask import Flask, render_template, request
from parser import extract_resume_text
from ranker import calculate_similarity
import os

app = Flask(__name__)
UPLOAD_FOLDER = "resumes"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        jd_text = request.form['job_description']
        files = request.files.getlist('resumes')
        scores = []

        for file in files:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            resume_text = extract_resume_text(filepath)
            score = calculate_similarity(jd_text, resume_text)
            scores.append((file.filename, round(score * 100, 2)))

        scores.sort(key=lambda x: x[1], reverse=True)
        return render_template('index.html', scores=scores)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
