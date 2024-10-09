import streamlit as st
from src.email_handler import last_email, mail_reply
from src.generative_ai import answer_question
from datetime import datetime, timedelta
import re

# Set the title of the page
st.title("Harmony Bot")

# Initialize chat history if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from the history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Define date range for email queries
today = datetime.now()
start_date = (today - timedelta(days=1)).strftime('%Y-%m-%d')
end_date = today.strftime('%Y-%m-%d')

# Query the user's unread emails for the given date range
with st.chat_message("assistant"):
    query_params = {"search_query_native": f"after:{start_date} before:{end_date} is:unread"}
    messages = st.session_state['nylas'].messages.list(os.environ.get("NYLAS_EMAIL"), query_params=query_params)

    # Generate an answer to show how many unread emails the user has
    answer = answer_question(messages)
    st.markdown(f"{str(answer.text)}")

# Function to handle user input and identify intent
def handle_intent(prompt):
    response = ""
    email_actions = {
        "check_mail": r"(see|check|get|view)\s*(my|the)\s*(mail|email)s?",
        "compose_mail": r"(send|compose|write|reply)\s*(a|an)?\s*(mail|email)"
    }
    for action, pattern in email_actions.items():
        if re.search(pattern, prompt, re.IGNORECASE):
            # Check mail or compose a reply based on the action detected
            response = last_email(prompt) if action == "check_mail" else mail_reply(prompt)
            break
    else:
        response = "Intent not recognized"
    return response

# React to user input in the chat
if prompt := st.chat_input("What is up?"):
    # Display user message in the chat
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Handle the user's intent and generate a response
    response = handle_intent(prompt)

    # Display the assistant's response
    with st.chat_message("assistant"):
        st.markdown(response)

    # Add the assistant's response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
