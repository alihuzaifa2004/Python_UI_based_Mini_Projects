# 📊 Basic Data Analysis with Streamlit

This is a simple Streamlit web application that allows users to upload a CSV file and instantly view an overview of the data, including the first few rows and summary statistics.

## 🚀 Features

* Upload a CSV file (`.csv` format)
* Display the first five rows of the dataset
* Show basic descriptive statistics using `pandas.describe()`

## 🛠️ Technologies Used

* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/)
* [Pandas](https://pandas.pydata.org/)

## 📦 Installation

1. **Clone the repository** (if applicable):

   ```bash
   git clone https://github.com/your-username/basic-data-analysis.git
   cd basic-data-analysis
   ```

2. **Create a virtual environment (optional but recommended)**:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages**:

   ```bash
   pip install streamlit pandas
   ```

## ▶️ How to Run the App

Run the following command in your terminal:

```bash
streamlit run app.py
```

Make sure your script is saved as `app.py`, or replace `app.py` with your script's filename.

## 📂 File Structure

```
.
├── app.py
├── README.md
└── requirements.txt  # Optional: for specifying dependencies
```

## 📝 Example

When you upload a CSV file, you'll see:

* The first five rows of the dataset
* Summary statistics such as count, mean, std, min, and max

## 🧩 Notes

* The CSV is read with `encoding='ISO-8859-1'` to handle non-UTF-8 files.
* You can adjust the encoding as needed (e.g., `utf-8`, `latin1`).

## 📃 License

This project is licensed under the MIT License.

