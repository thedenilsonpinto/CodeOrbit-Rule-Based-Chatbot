import streamlit as st
from datetime import datetime

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Rule-Based AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ---------------------------
# Title
# ---------------------------
st.title("🤖 Rule-Based AI Chatbot")
st.caption("Built using Python + Streamlit")

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.title("📌 About")

st.sidebar.info("""
**Project:** Rule-Based AI Chatbot

**Developer:** Denilson Pinto B

**Internship:** Artificial Intelligence Intern

**Technologies Used**
- Python
- Streamlit
""")

# ---------------------------
# Chat History
# ---------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        (
            "Bot",
            """👋 Hello!

Welcome to the Rule-Based AI Chatbot.

You can ask me about:

• Artificial Intelligence
• Machine Learning
• Deep Learning
• Python
• Current Time
• Current Date

Happy Chatting! 😊"""
        )
    ]

# ---------------------------
# Clear Chat Button
# ---------------------------
if st.sidebar.button("🗑️ Clear Chat"):

    st.session_state.chat_history = [
        (
            "Bot",
            """👋 Hello!

Welcome back!

How can I help you today? 😊"""
        )
    ]

    st.rerun()

# ---------------------------
# Chatbot Logic
# ---------------------------
def get_bot_response(user_input):

    text = user_input.lower()

    # Greetings
    if text in ["hi", "hello", "hey"]:
        return "Hello! 👋 How can I help you today?"

    elif "how are you" in text:
        return "I'm doing great! Thanks for asking 😊"

    elif "your name" in text:
        return "I'm a Rule-Based AI Chatbot."

    elif "who created you" in text:
        return "I was developed by Denilson Pinto B using Python and Streamlit."

    # AI
    elif "what is ai" in text or text == "ai":
        return "Artificial Intelligence (AI) is the simulation of human intelligence by machines."

    elif "machine learning" in text:
        return "Machine Learning is a branch of AI that enables computers to learn from data."

    elif "deep learning" in text:
        return "Deep Learning is a subset of Machine Learning based on neural networks."

    # Python
    elif "python" in text:
        return "Python is a powerful and beginner-friendly programming language."
    
    elif "internship" in text:
        return "This chatbot was developed as part of an Artificial Intelligence Internship project."

    elif "streamlit" in text:
        return "Streamlit is a Python framework used to build interactive web applications."

    elif "developer" in text:
        return "This chatbot was developed by Denilson Pinto B."

    elif "help" in text:
        return """You can ask me about:
    • AI
    • Machine Learning
    • Deep Learning
    • Python
    • Time
    • Date"""

    # Time
    elif "time" in text:
        return f"🕒 Current Time: {datetime.now().strftime('%H:%M:%S')}"

    # Date
    elif "date" in text:
        return f"📅 Today's Date: {datetime.now().strftime('%d-%m-%Y')}"

    # Thanks
    elif "thank" in text:
        return "You're welcome! 😊"

    # Bye
    elif text in ["bye", "exit", "quit"]:
        return "Goodbye! 👋 Have a wonderful day."

    else:
        return "Sorry 😔 I don't understand that. Please try another question."
    
    

# ---------------------------
# Display Chat History
# ---------------------------
for sender, message in st.session_state.chat_history:

    if sender == "You":

        with st.chat_message("user"):
            st.write(message)

    else:

        with st.chat_message("assistant"):
            st.write(message)

# ---------------------------
# Chat Input
# ---------------------------
prompt = st.chat_input("Type your message here...")

if prompt:

    with st.chat_message("user"):
        st.write(prompt)

    response = get_bot_response(prompt)

    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.chat_history.append(("You", prompt))
    st.session_state.chat_history.append(("Bot", response))

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.caption("© 2026 | Developed by Denilson Pinto B | AI Internship Project")