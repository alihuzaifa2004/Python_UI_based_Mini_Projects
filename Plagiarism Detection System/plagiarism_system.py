import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import fitz  # PyMuPDF
import docx
import os

# ---------------------- Config ----------------------
st.set_page_config(page_title="Plagiarism Checker", layout="centered")

st.title("🕵️ Plagiarism Detection System")

st.markdown("""
Upload two documents or enter text manually. The app compares them and calculates a **similarity score** using either **TF-IDF** or **Sentence Transformers**.
""")

# ---------------------- File Readers ----------------------
def read_txt(file):
    return file.read().decode("utf-8")

def read_docx(file):
    doc = docx.Document(file)
    return "\n".join([p.text for p in doc.paragraphs])

def read_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    return "\n".join(page.get_text() for page in doc)

def extract_text(upload):
    if upload is None:
        return ""
    ext = os.path.splitext(upload.name)[1].lower()
    if ext == ".txt":
        return read_txt(upload)
    elif ext == ".docx":
        return read_docx(upload)
    elif ext == ".pdf":
        return read_pdf(upload)
    else:
        return ""

# ---------------------- Similarity Functions ----------------------
def compute_tfidf_similarity(text1, text2):
    text1 = text1.strip()
    text2 = text2.strip()
    if not text1 or not text2:
        return 0.0
    try:
        tfidf = TfidfVectorizer().fit_transform([text1, text2])
        return cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    except ValueError:
        return 0.0

def compute_transformer_similarity(text1, text2):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode([text1, text2])
    return cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]

# ---------------------- UI: File Uploads / Manual Input ----------------------
col1, col2 = st.columns(2)

with col1:
    file1 = st.file_uploader("Upload Document 1", type=["txt", "docx", "pdf"])
with col2:
    file2 = st.file_uploader("Upload Document 2", type=["txt", "docx", "pdf"])

manual_mode = st.checkbox("✍️ Use manual text input instead")

if manual_mode:
    text1 = st.text_area("Enter Text 1", height=150)
    text2 = st.text_area("Enter Text 2", height=150)
else:
    text1 = extract_text(file1)
    text2 = extract_text(file2)

model_option = st.radio("Choose Similarity Model", ["TF-IDF (Fast)", "Sentence Transformers (Accurate)"])

# ---------------------- Highlight Helper ----------------------
def highlight_similar_lines(text_a, text_b, threshold=0.8):
    lines_a = [line.strip() for line in text_a.split('\n') if line.strip()]
    lines_b = [line.strip() for line in text_b.split('\n') if line.strip()]

    highlighted_a = ""
    highlighted_b = ""

    for line1 in lines_a:
        if len(line1.split()) < 3:
            highlighted_a += f"<div>{line1}</div>\n"
            continue
        max_sim = 0
        for line2 in lines_b:
            if len(line2.split()) < 3:
                continue
            sim = compute_tfidf_similarity(line1, line2)
            max_sim = max(max_sim, sim)
        if max_sim > threshold:
            highlighted_a += f"<div style='background-color: #564F1B'>{line1}</div>\n"
        else:
            highlighted_a += f"<div>{line1}</div>\n"

    for line2 in lines_b:
        if len(line2.split()) < 3:
            highlighted_b += f"<div>{line2}</div>\n"
            continue
        max_sim = 0
        for line1 in lines_a:
            if len(line1.split()) < 3:
                continue
            sim = compute_tfidf_similarity(line2, line1)
            max_sim = max(max_sim, sim)
        if max_sim > threshold:
            highlighted_b += f"<div style='background-color: #564F1B'>{line2}</div>\n"
        else:
            highlighted_b += f"<div>{line2}</div>\n"

    return highlighted_a, highlighted_b

# ---------------------- Comparison Trigger ----------------------
if st.button("🔍 Compare"):
    if not text1.strip() or not text2.strip():
        st.error("Both documents/text inputs are required.")
    else:
        with st.spinner("Analyzing..."):
            if model_option == "TF-IDF (Fast)":
                score = compute_tfidf_similarity(text1, text2)
            else:
                score = compute_transformer_similarity(text1, text2)

        st.subheader("🔢 Similarity Score:")
        st.code(f"{score * 100:.2f}%")

        if score > 0.8:
            st.warning("⚠️ High similarity! Potential plagiarism.")
        elif score > 0.5:
            st.info("🧐 Moderate similarity. Needs review.")
        else:
            st.success("✅ Low similarity. Likely original.")

        # ---------------------- Line-by-Line Highlight ----------------------
        st.markdown("### 🟨 Line-by-Line Highlighting")

        col1, col2 = st.columns(2)
        highlighted_text1, highlighted_text2 = highlight_similar_lines(text1, text2)

        with col1:
            st.markdown("**Document 1:**", unsafe_allow_html=True)
            st.markdown(highlighted_text1, unsafe_allow_html=True)

        with col2:
            st.markdown("**Document 2:**", unsafe_allow_html=True)
            st.markdown(highlighted_text2, unsafe_allow_html=True)
