
# ⏱️ Real-Time Stopwatch App

This is a simple **Real-Time Stopwatch** web application built using [Streamlit](https://streamlit.io/) in Python.

It allows you to:
- Start the stopwatch
- Pause the stopwatch
- Reset the stopwatch  
The timer updates dynamically in real time.

## Features

✅ Start/Stop the stopwatch  
✅ Reset the stopwatch  
✅ Real-time updates of minutes, seconds, and milliseconds  
✅ Minimal, centered layout  

---

## Installation

1. Clone this repository:

\`\`\`bash
git clone https://github.com/your-username/streamlit-stopwatch.git
cd streamlit-stopwatch
\`\`\`

2. Install the required dependencies:

\`\`\`bash
pip install streamlit
\`\`\`

---

## Usage

Run the app using:

\`\`\`bash
streamlit run stopwatch.py
\`\`\`

Then open the provided `localhost` link in your browser.

---

## Code Structure

\`\`\`python
# Main steps:
1️⃣ Initialize session state variables (start_time, elapsed, running)
2️⃣ Create Start, Stop, Reset buttons
3️⃣ Update elapsed time while running
4️⃣ Display timer dynamically
\`\`\`

### Key Components

- **Session State**  
Used to persist stopwatch state across Streamlit reruns.
\`\`\`python
st.session_state.start_time
st.session_state.elapsed
st.session_state.running
\`\`\`

- **Dynamic Display**  
A \`st.empty()\` placeholder is used to update the timer display inside a loop.

- **Loop**  
When running, the loop updates the elapsed time every 0.05 seconds:
\`\`\`python
while st.session_state.running:
    ...
    time.sleep(0.05)
\`\`\`

---

## Limitations

⚠️ Since Streamlit is not designed for continuous loops, this app relies on simple hacks using session state and \`st.empty()\`. It is best for small utilities but not a high-precision stopwatch.

---

## License

MIT License.  
Feel free to use and modify.

---

## Author

Built by Ali huzaifa using Python & Streamlit.
