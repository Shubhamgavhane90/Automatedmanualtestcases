import streamlit as st
import docx
import pandas as pd
import pytesseract
from openai import OpenAI

# Path to Tesseract for OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\igxb28c\AppData\Local\Programs\Tesseract-OCR'

st.set_page_config(page_title="AI Manual Test Case Generator", layout="wide")
st.title("📄 AI-Powered Manual Test Case Generator from KT Document")

# User input for OpenAI API Key
openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")

# Upload .docx file
uploaded_file = st.file_uploader("Upload your KT Document (.docx)", type=["docx"])

# Extract all text from a .docx file
def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs if para.text.strip() != ""])

# Generate test cases using OpenAI's new SDK format
def generate_test_cases(kt_text, api_key):
    client = OpenAI(api_key=api_key)

    prompt = f"""
You are a QA test engineer. Given the following knowledge transfer (KT) documentation, generate 5 manual test cases. Each test case should include:

1. Test Case Title  
2. Steps to Execute  
3. Expected Result

KT Document:
{kt_text}

Return the test cases in JSON format.
"""

    response = client.chat.completions.create(
        model="gpt-4",  # or "gpt-3.5-turbo" if you prefer
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content

# Main app logic
if uploaded_file and openai_api_key:
    with st.spinner("Reading and analyzing your document..."):
        kt_text = extract_text_from_docx(uploaded_file)
        try:
            ai_output = generate_test_cases(kt_text, openai_api_key)
            st.success("Test cases generated successfully!")

            try:
                df = pd.read_json(ai_output)
                st.dataframe(df)
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button("Download as CSV", csv, "test_cases.csv", "text/csv")
            except:
                st.text_area("Raw Output", ai_output, height=400)
        except Exception as e:
            st.error(f"Error generating test cases: {e}")
