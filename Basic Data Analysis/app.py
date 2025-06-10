import streamlit as st
import pandas as pd

# Initialize the Streamlit app
st.title("Basic Data Analysis")

# File uploader component
file = st.file_uploader("Upload a CSV file", type=["csv"])

# Check if a file is uploaded
if file is not None:
    df = pd.read_csv(file, encoding='ISO-8859-1')  # or 'latin1'
    st.write("Data Overview:")
    st.write(df.head())
    st.write("Summary Statistics:")
    st.write(df.describe())
else:
    st.write("Please upload a CSV file.")
