import streamlit as st
from src.embedding import generate_embedding
from src.email_handler import retrieve_email_by_id
from src.generative_ai import answer_question

# Set the title of the page
st.title("Ask Mail")

# Input field for the user's question
user_question = st.text_input("Ask a Question from your Email")

# If the user enters a question, proceed with the following steps
if user_question:
    query = user_question

    # Generate embedding for the query
    query_embedding = generate_embedding(query)

    # Query Pinecone index for similar emails
    res = st.session_state['index'].query(vector=query_embedding, top_k=3, include_values=False)

    # Retrieve emails by matching IDs
    emailresList = [retrieve_email_by_id(match.id) for match in res.matches]

    # Prepare the context for the AI to generate an answer
    context = [{"snippet": email[0].snippet, "from": email[0].from_, "to": email[0].to,
                "subject": email[0].subject, "date": email[0].date, "id": email[0].id}
               for email in emailresList]

    # Generate an answer using the AI model
    answer = answer_question(context, query)

    # Display the reply
    st.write("Reply: ", f"{answer.text}")
