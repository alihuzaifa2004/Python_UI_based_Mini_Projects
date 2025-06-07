import streamlit as st
import time

st.set_page_config(page_title="Stopwatch", layout="centered")
st.title("⏱️ Real-Time Stopwatch")

# Initialize session state variables
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "elapsed" not in st.session_state:
    st.session_state.elapsed = 0.0
if "running" not in st.session_state:
    st.session_state.running = False

# Control buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("▶️ Start"):
        if not st.session_state.running:
            st.session_state.start_time = time.time() - st.session_state.elapsed
            st.session_state.running = True

with col2:
    if st.button("⏸️ Stop"):
        if st.session_state.running:
            st.session_state.elapsed = time.time() - st.session_state.start_time
            st.session_state.running = False

with col3:
    if st.button("🔄 Reset"):
        st.session_state.start_time = None
        st.session_state.elapsed = 0.0
        st.session_state.running = False

# Display stopwatch dynamically
timer_placeholder = st.empty()

while st.session_state.running:
    st.session_state.elapsed = time.time() - st.session_state.start_time
    mins, secs = divmod(int(st.session_state.elapsed), 60)
    millis = int((st.session_state.elapsed - int(st.session_state.elapsed)) * 100)
    timer_placeholder.markdown(f"## ⏰ {mins:02d}:{secs:02d}.{millis:02d}")
    time.sleep(0.05)

# Show final time if stopped
if not st.session_state.running:
    mins, secs = divmod(int(st.session_state.elapsed), 60)
    millis = int((st.session_state.elapsed - int(st.session_state.elapsed)) * 100)
    timer_placeholder.markdown(f"## ⏰ {mins:02d}:{secs:02d}.{millis:02d}")
