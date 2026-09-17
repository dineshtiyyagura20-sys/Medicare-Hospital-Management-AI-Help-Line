import streamlit as st

from utils.llm_helper import ask_medicare_ai


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="MediCare AI Help Line",
    page_icon="🧠",
    layout="wide"
)


# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        font-size: 38px;
        font-weight: bold;
        color: #0F766E;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #64748B;
        margin-bottom: 25px;
    }

    .info-box {
        background-color: #ECFDF5;
        border-left: 5px solid #10B981;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 20px;
    }

    .warning-box {
        background-color: #FFF7ED;
        border-left: 5px solid #F97316;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown(
    '<div class="main-title">🧠 MediCare 24×7 AI Help Line</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Your intelligent assistant for the MediCare Hospital Management System'
    '</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# INFORMATION
# ---------------------------------------------------------

st.markdown(
    """
    <div class="info-box">

    <b>👋 Welcome to MediCare AI Help Line!</b>

    <br><br>

    I can help you understand and use the MediCare application.

    <br><br>

    You can ask me about:

    <ul>
        <li>👨‍⚕️ Patients</li>
        <li>🩺 Doctors</li>
        <li>📅 Appointments</li>
        <li>💰 Billing</li>
        <li>📊 Reports</li>
        <li>📁 CSV data</li>
        <li>🏠 Dashboard</li>
        <li>💻 How the project works</li>
    </ul>

    </div>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# MEDICAL DISCLAIMER
# ---------------------------------------------------------

st.markdown(
    """
    <div class="warning-box">

    ⚠️ <b>Important:</b>

    This AI assistant is designed to help users with the
    MediCare application.

    It is not a doctor and should not be used for diagnosis,
    medication or emergency medical advice.

    For medical concerns, please contact a qualified healthcare
    professional.

    </div>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.header("🧠 AI Help Line")

    st.write(
        "Ask questions about the MediCare Hospital "
        "Management System."
    )

    st.divider()

    st.subheader("💡 Example Questions")

    examples = [
        "How do I register a patient?",
        "How can I book an appointment?",
        "How do I cancel an appointment?",
        "How can I create a bill?",
        "How do I mark a bill as paid?",
        "What information is shown on the dashboard?",
        "How does CSV storage work?",
        "What is the purpose of the Patient class?"
    ]

    for question in examples:

        if st.button(
            question,
            use_container_width=True
        ):
            st.session_state.selected_question = question

    st.divider()

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    ):
        st.session_state.chat_history = []

        if "selected_question" in st.session_state:
            del st.session_state.selected_question

        st.rerun()


# ---------------------------------------------------------
# DISPLAY CHAT HISTORY
# ---------------------------------------------------------

for message in st.session_state.chat_history:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ---------------------------------------------------------
# USER INPUT
# ---------------------------------------------------------

selected_question = st.session_state.get(
    "selected_question",
    ""
)

prompt = st.chat_input(
    "Ask MediCare AI anything about the application..."
)


# ---------------------------------------------------------
# HANDLE EXAMPLE QUESTION
# ---------------------------------------------------------

if selected_question and not prompt:

    prompt = selected_question

    del st.session_state.selected_question


# ---------------------------------------------------------
# PROCESS USER QUESTION
# ---------------------------------------------------------

if prompt:

    # Display user message
    with st.chat_message("user"):

        st.markdown(prompt)

    # Save user message
    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Ask AI
    with st.chat_message("assistant"):

        with st.spinner("🧠 MediCare AI is thinking..."):

            response = ask_medicare_ai(
                prompt,
                st.session_state.chat_history[:-1]
            )

        st.markdown(response)

    # Save AI response
    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": response
        }
    )