# AI Code Explainer Tool

## Project Overview

This project is an AI-powered Code Explainer Tool built using Python and Streamlit.  
The application helps users understand programming code in simple language using Large Language Models (LLMs).

Users can paste code snippets and receive:

- Step-by-step explanations
- Logic breakdowns
- Beginner-friendly explanations
- Advanced technical explanations
- Bug detection suggestions
- Code improvement recommendations

The application supports multiple programming languages and provides a ChatGPT-style interactive experience.

---

# Features

- AI-powered code explanation
- Multi-language support
- Beginner mode and advanced mode
- Step-by-step code breakdown
- Bug detection suggestions
- Code optimization recommendations
- Interactive chat interface
- Real-time AI responses
- Session-based conversation history

---

# Problem Statement

Many students and beginner developers struggle to:

- understand programming logic
- debug errors
- read complex code
- learn new programming languages

Traditional learning methods can be time-consuming and difficult for beginners.

This project solves these problems by using AI to explain code in a simple and interactive way.

---

# Use Cases

- Programming learning assistant
- Beginner coding education
- Code debugging support
- Developer onboarding
- Code review assistance
- Technical interview preparation

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Streamlit | Web application interface |
| Groq API / OpenAI API | AI-powered code explanation |
| python-dotenv | Secure API key management |
| Session State | Maintain conversation history |

---

# Project Structure

```plaintext
code_explainer/
│
├── app.py
├── requirements.txt
├── .env
└── README.md
````
---
#Steps to run the app
# Steps to Run the Project

1. Clone the repository using `git clone <your_repo_link>` and move into the project folder using `cd code_explainer`.

2. Create a virtual environment using `python -m venv venv`.

3. Activate the virtual environment using `venv\Scripts\activate` for Windows or `source venv/bin/activate` for Mac/Linux.

4. Install all required libraries using `pip install -r requirements.txt`.

5. Create a `.env` file inside the project folder and add your API key as `GROQ_API_KEY=your_api_key`.

6. Run the application using `streamlit run app.py`.

7. Open the browser and visit `http://localhost:8501` to use the application.


