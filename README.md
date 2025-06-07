# 🤖 Resu Genius

**Resu Genius** is an AI-powered resume analysis and enhancement platform built using **Google Generative AI (Gemini)** and **Streamlit**. It helps users evaluate their resumes against job descriptions, generate professional summaries, identify missing keywords, and rewrite resumes to make them **ATS-optimized** and job-ready.

---

## 🚀 Features

- ✅ **ATS Evaluator**  
  Upload your resume and job description to:
  - Get a **JD Match %**
  - Identify **missing keywords**
  - Receive a concise **Profile Summary**

- 🧠 **Resume Rewriter**  
  Enhance your resume with:
  - Tailored formatting and structure
  - Grouped skill categories (e.g., Programming Languages, Tools)
  - ATS optimization with keyword embedding
  - Professionally written summaries and project entries

- 📄 **Supports Multiple Formats**
  - Resume upload in **PDF**, **DOCX**, or plain text
  - Job descriptions in plain text

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **AI Backend**: [Google Generative AI (Gemini)](https://ai.google.dev/)
- **PDF Handling**: `PyPDF2`, `fpdf`
- **DOCX Parsing**: `python-docx`
- **Environment Management**: `python-dotenv`

---

## 📂 Project Structure

```
Resu-Genius/
│
├── pages/
│   ├── ats.py             # ATS evaluator logic
│   └── resume_writer.py   # Resume rewriting logic
│
├── .env                   # Stores your API key securely
├── requirements.txt       # Python dependencies
└── main.py                # Streamlit app entry point
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Praj-2808/Resu-Genius.git
cd Resu-Genius
```

### 2. Create and Activate a Virtual Environment (optional)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add Your API Key
Create a `.env` file in the root folder and add your Gemini API key:
```
GOOGLE_API_KEY=your_google_genai_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run main.py
```

---

## 🧪 Example Use Case

1. Upload your resume and job description.
2. Get a JD match score, profile summary, and list of missing keywords.
3. Rewrite your resume professionally with grouped skills and formatted project entries.

---

## 📈 Output Highlights

### Grouped Skills Example:
```
Programming Languages: Python, SQL, R  
Tools & Libraries: Power BI, Pandas, NumPy  
Databases: MySQL, PostgreSQL  
```

### Project Format Example:
```
Energy Drink, Market Analysis for Energy Drink Launch Using Power BI | [Link]  
Conducted market research on survey data from 10,000+ respondents across 10 cities. Built interactive dashboards and validated marketing metrics to guide product launch strategy.
```

---

## 👩‍💻 Author

Built with ❤️ by [Prajakta Mishra](https://github.com/Praj-2808)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
