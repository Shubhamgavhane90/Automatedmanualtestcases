# Automated Manual Test Case Generator

This Streamlit app reads a `.docx` document, extracts text, and uses OpenAI GPT to generate test cases in structured JSON format. The test cases are converted to a CSV download.

## 🔧 Features

- Upload `.docx` file containing KT/requirement document
- Automatically generates test cases using GPT-4
- Outputs test cases in a downloadable CSV format

## 📦 Technologies Used

- Python
- Streamlit
- OpenAI GPT-4 API
- pandas

▶️ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/Shubhamgavhane90/Automatedmanualtestcases.git
   cd Automatedmanualtestcases
   pip install -r requirements.txt
   streamlit run app.py
