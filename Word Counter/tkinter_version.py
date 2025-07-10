import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
import os

def extract_text_from_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".txt":
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    elif ext == ".pdf":
        text = ""
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
        return text
    else:
        messagebox.showerror("Unsupported File", "Only .txt and .pdf files are supported.")
        return ""

def count_text_statistics(text):
    words = text.split()
    characters = len(text)
    sentences = text.count('.') + text.count('!') + text.count('?')
    paragraphs = text.count('\n\n') + 1 if '\n\n' in text else 1
    return len(words), characters, sentences, paragraphs

def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("PDF Files", "*.pdf")])
    if file_path:
        content = extract_text_from_file(file_path)
        text_input.delete("1.0", tk.END)
        text_input.insert(tk.END, content)

def analyze_text():
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Empty Input", "Please paste text or upload a file first.")
        return

    words, characters, sentences, paragraphs = count_text_statistics(text)
    
    result_label.config(
        text=f"Words: {words}\nCharacters: {characters}\nSentences: {sentences}\nParagraphs: {paragraphs}"
    )

# Initialize window
root = tk.Tk()
root.title("Word Counter App")
root.geometry("700x600")
root.config(padx=20, pady=20)

# Heading
tk.Label(root, text="📝 Word Counter (Tkinter)", font=("Arial", 18, "bold")).pack(pady=10)

# Upload Button
tk.Button(root, text="📂 Upload .txt or .pdf File", command=upload_file, bg="lightblue").pack(pady=5)

# Text Input
text_input = tk.Text(root, height=15, wrap=tk.WORD)
text_input.pack(fill=tk.BOTH, expand=True, pady=10)

# Analyze Button
tk.Button(root, text="🔍 Analyze Text", command=analyze_text, bg="lightgreen").pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12), justify=tk.LEFT)
result_label.pack()

root.mainloop()
