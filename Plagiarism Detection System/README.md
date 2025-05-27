# 🕵️ Plagiarism Detection System

A simple yet powerful plagiarism detection tool built using **Streamlit** and **machine learning** techniques. This app allows users to compare two documents (or manually entered texts) and calculates a similarity score using either **TF-IDF** (fast) or **Sentence Transformers** (accurate) models.

---

## 🚀 Features

- 📄 **File Upload Support**: Compare `.txt`, `.docx`, or `.pdf` files.
- ✍️ **Manual Text Entry**: Option to input text manually for comparison.
- 🧠 **Similarity Models**:
  - `TF-IDF`: Fast comparison using vectorized word frequency.
  - `Sentence Transformers`: Semantic comparison using deep learning embeddings.
- 🔍 **Line-by-Line Highlighting**: Visual indication of similar lines with customizable thresholds.
- 📊 **Similarity Score**: Easy-to-understand similarity percentage with interpretation.
- 🛡️ Useful for checking plagiarism, paraphrasing, or content reuse.

---

## 📦 Dependencies

Install the required libraries using `pip`:

```bash
pip install streamlit scikit-learn sentence-transformers python-docx pymupdf
```

---

## 🛠️ How to Run

1. Clone the repository or copy the source code.
2. Ensure all dependencies are installed (see above).
3. Run the Streamlit app:

```bash
streamlit run app.py
```

> Replace `app.py` with the name of your Python file.

---

## 📁 File Support

| Format | Supported | Library Used    |
|--------|-----------|-----------------|
| TXT    | ✅        | Built-in        |
| DOCX   | ✅        | `python-docx`   |
| PDF    | ✅        | `PyMuPDF` (fitz) |

---

## 🔎 Example Use Cases

- Checking similarity between student submissions
- Comparing research papers or articles
- Ensuring originality of written content
- Finding duplicated content in blogs, assignments, or reports

---

## ✅ Output Interpretation

| Similarity Score (%) | Interpretation              |
|----------------------|-----------------------------|
| 0–50%                | ✅ Low similarity            |
| 51–80%               | 🧐 Moderate similarity        |
| 81–100%              | ⚠️ High similarity (possible plagiarism) |

---

## 📌 Notes

- Sentence Transformers require an internet connection the first time to download the model.
- Accuracy of results depends on the quality and structure of the input texts.
- Line-by-line highlighting is based on TF-IDF comparison regardless of model selection.

---

## 📜 License

This project is open-source and available for personal or academic use.

---

## 🙌 Acknowledgments

- [Streamlit](https://streamlit.io/)
- [scikit-learn](https://scikit-learn.org/)
- [SentenceTransformers](https://www.sbert.net/)
- [python-docx](https://github.com/python-openxml/python-docx)
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)