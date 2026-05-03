import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Groq Client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Streamlit Page Configuration
st.set_page_config(
    page_title="AI Code Explainer",
    page_icon="💻",
    layout="wide"
)

# App Title
st.title("💻 AI Code Explainer")

# Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar Settings
with st.sidebar:

    st.header("Explanation Settings")

    language = st.selectbox(
        "Programming Language",
        [
            "Python",
            "Java",
            "JavaScript",
            "C++",
            "C",
            "Go",
            "SQL"
        ]
    )

    mode = st.selectbox(
        "Explanation Mode",
        [
            "Beginner",
            "Advanced"
        ]
    )

    bug_detection = st.checkbox(
        "Enable Bug Detection Suggestions"
    )

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Display Previous Messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
prompt = st.chat_input(
    "Paste your code here..."
)

if prompt:

    # Store User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Display User Message
    with st.chat_message("user"):
        st.code(prompt, language=language.lower())

    # System Prompt
    system_prompt = f"""
    You are an expert AI Code Explainer.

    Programming Language: {language}

    Explanation Mode: {mode}

    Bug Detection Enabled: {bug_detection}

    Your tasks:
    - first mention what topic it is and explain definitions of the code
    - Explain the code in simple language
    - Provide step-by-step explanation
    - Explain logic clearly
    - Help beginners understand the code
    """

    if bug_detection:
        system_prompt += """
        - Detect possible bugs
        - Suggest code improvements
        - Recommend best practices
        """

    # Generate AI Response
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            }
        ] + st.session_state.messages,
        temperature=0.7,
        max_tokens=2048
    )

    reply = response.choices[0].message.content

    # Store Assistant Response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

    # Display Assistant Response
    with st.chat_message("assistant"):
        st.markdown(reply)