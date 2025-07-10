import streamlit as st
import PyPDF2

st.set_page_config(page_title="Word Counter", layout="centered")
st.title("📝 Word Counter App")

# Function to extract text from uploaded file
def extract_text(file):
    if file.type == "text/plain":
        return file.read().decode("utf-8")
    elif file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    else:
        return "Unsupported file format."

# Function to count statistics
def count_stats(text):
    words = text.split()
    characters = len(text)
    sentences = text.count('.') + text.count('!') + text.count('?')
    paragraphs = text.count('\n\n') + 1 if '\n\n' in text else 1
    return len(words), characters, sentences, paragraphs

# Input Mode Selection
input_mode = st.radio("Select input method:", ["Paste Text", "Upload File"])

text_data = ""

# Input area based on selected mode
if input_mode == "Paste Text":
    text_data = st.text_area("✏️ Paste your text here:", height=250)
else:
    uploaded_file = st.file_uploader("📄 Upload a .txt or .pdf file", type=["txt", "pdf"])
    if uploaded_file:
        text_data = extract_text(uploaded_file)
        st.text_area("📖 Extracted Text:", text_data, height=250, disabled=True)

# Submit button
if st.button("✅ Submit"):
    if text_data.strip():
        words, characters, sentences, paragraphs = count_stats(text_data)

        st.subheader("📊 Text Statistics")
        st.markdown(f"**Total Words:** {words}")
        st.markdown(f"**Total Characters:** {characters}")
        st.markdown(f"**Total Sentences:** {sentences}")
        st.markdown(f"**Total Paragraphs:** {paragraphs}")
    else:
        st.warning("❗ No text found. Please paste or upload a file first.")
