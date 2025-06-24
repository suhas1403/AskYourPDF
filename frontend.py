import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000" 

st.title("📄 Ask Your PDF")

# Upload PDF section
st.header("1. Upload your PDF")
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("Uploading and indexing PDF..."):
        response = requests.post(
            f"{API_URL}/upload_pdf",
            files={"file": (uploaded_file.name, uploaded_file, "application/pdf")}
        )
        if response.status_code == 200:
            st.success("✅ PDF uploaded and indexed successfully!")
        else:
            st.error(f"❌ Upload failed: {response.text}")

# Ask a question
st.header("2. Ask a question about the PDF")
question = st.text_input("Your question")

if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating answer..."):
            response = requests.post(
                f"{API_URL}/ask",
                data={"question": question}
            )
            if response.status_code == 200:
                answer = response.json()["answer"]
                st.success("🧠 Answer:")
                st.markdown(answer)
            else:
                st.error(f"❌ Failed to get answer: {response.text}")
