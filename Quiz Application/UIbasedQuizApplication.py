import streamlit as st

# Define questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Paris", "Madrid", "Rome"],
        "answer": "Paris",
        "question_number": 1
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "22"],
        "answer": "4",
        "question_number": 2
    },
    {
        "question": "What is the color of the sky?",
        "options": ["Red", "Green", "Blue", "Yellow"],
        "answer": "Blue",
        "question_number": 3
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Mars", "Earth", "Mercury", "Jupiter"],
        "answer": "Jupiter",
        "question_number": 4
    },
    {
        "question": "What is the process by which plants convert sunlight into energy?",
        "options": ["Photosynthesis", "Respiration", "Transpiration", "Fermentation"],
        "answer": "Photosynthesis",
        "question_number": 5
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["H2O", "O2", "CO2", "H2O2"],
        "answer": "H2O",
        "question_number": 6
    },
    {
        "question": "Which planet is closest to the sun?",
        "options": ["Venus", "Mercury", "Earth", "Mars"],
        "answer": "Mercury",
        "question_number": 7
    },
    {
        "question": "In what country did the first Starbucks open outside of North America?",
        "options": ["Japan", "Germany", "UK", "Australia"],
        "answer": "Japan",
        "question_number": 8
    },
    {
        "question": "What is the largest desert in the world?",
        "options": ["Sahara", "Karakum", "Gobi", "Antarctic"],
        "answer": "Antarctic",
        "question_number": 9
    },
    {
        "question": "What is the national dish of France?",
        "options": ["Boeuf Bourguignon", "Coq au Vin", "Steak Frites", "Ratatouille"],
        "answer": "Steak Frites",
        "question_number": 10
    },
    # Additional Questions
    {
        "question": "What is the tallest mountain in the world?",
        "options": ["Mount Everest", "K2", "Mount Kilimanjaro", "Mount Fuji"],
        "answer": "Mount Everest",
        "question_number": 11
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "Mark Twain", "William Shakespeare", "Homer"],
        "answer": "William Shakespeare",
        "question_number": 12
    },
    {
        "question": "What is the longest river in the world?",
        "options": ["Amazon", "Nile", "Yangtze", "Mississippi"],
        "answer": "Nile",
        "question_number": 13
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean",
        "question_number": 14
    },
    {
        "question": "Who was the first president of the United States?",
        "options": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "John Adams"],
        "answer": "George Washington",
        "question_number": 15
    },
    {
        "question": "What is the main ingredient in guacamole?",
        "options": ["Tomato", "Avocado", "Onion", "Garlic"],
        "answer": "Avocado",
        "question_number": 16
    },
    {
        "question": "In what year did the Titanic sink?",
        "options": ["1912", "1920", "1898", "1935"],
        "answer": "1912",
        "question_number": 17
    },
    {
        "question": "What is the smallest continent by land area?",
        "options": ["Asia", "Europe", "Australia", "Antarctica"],
        "answer": "Australia",
        "question_number": 18
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["Yuan", "Yen", "Won", "Ringgit"],
        "answer": "Yen",
        "question_number": 19
    },
    {
        "question": "What element does 'O' represent on the periodic table?",
        "options": ["Oxygen", "Osmium", "Oganesson", "Ozone"],
        "answer": "Oxygen",
        "question_number": 20
    }
]
# Initialize session state
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "user_answers" not in st.session_state:
    st.session_state.user_answers = [None] * len(questions)
if "show_result" not in st.session_state:
    st.session_state.show_result = False

st.title("🧠 MCQ Quiz App")

# Quiz Logic
if st.session_state.q_index < len(questions) and not st.session_state.show_result:
    current_q = questions[st.session_state.q_index]
    st.subheader(f"Q{st.session_state.q_index + 1}: {current_q['question']}")

    selected = st.radio("Choose your answer:", current_q["options"], key=f"q{st.session_state.q_index}")

    if st.button("Next"):
        st.session_state.user_answers[st.session_state.q_index] = selected
        st.session_state.q_index += 1
        st.rerun()

elif not st.session_state.show_result:
    if st.button("Show Result"):
        st.session_state.show_result = True
        st.rerun()

# Show Results
if st.session_state.show_result:
    st.title("📊 Quiz Results")
    score = 0

    for idx, q in enumerate(questions):
        user_ans = st.session_state.user_answers[idx]
        correct_ans = q["answer"]
        is_correct = user_ans == correct_ans

        st.markdown(f"**Q{idx + 1}: {q['question']}**")
        st.write(f"Your answer: {user_ans}")
        st.write(f"Correct answer: {correct_ans}")
        st.markdown("---")

        if is_correct:
            score += 1

    st.success(f"✅ Your Score: {score} / {len(questions)}")

    if st.button("Restart Quiz"):
        st.session_state.q_index = 0
        st.session_state.user_answers = [None] * len(questions)
        st.session_state.show_result = False
        st.rerun()
