import streamlit as st
from config.config_loader import load_config
from pinecone import Pinecone
from nylas import Client
import google.generativeai as genai

# Load configurations (either from secrets.toml or environment variables)
config = load_config()

# Initialize session state with API configurations for global access in the app
if 'config' not in st.session_state:
    st.session_state['config'] = config

# Initialize Google Generative AI
genai.configure(api_key=config['GENAI_API_KEY'])

# Initialize Pinecone
if 'index' not in st.session_state:
    pinecone_client = Pinecone(api_key=config['PINECONE_API_KEY'])
    st.session_state['index'] = pinecone_client.Index("ask-mail")

# Initialize Nylas
if 'nylas' not in st.session_state:
    nylas_client = Client(config['NYLAS_API_KEY'], config['NYLAS_API_URI'])
    st.session_state['nylas'] = nylas_client

# Set up sidebar navigation
st.sidebar.title("Harmony Email Assistant")
page = st.sidebar.selectbox("Select a page", ["Ask Mail", "Chat", "Dashboard"])

# Navigate between pages
if page == "Ask Mail":
    st.experimental_set_page_config(page_title="Ask Mail")
    import pages.askMail  # Loads the askMail page
elif page == "Chat":
    st.experimental_set_page_config(page_title="Chat")
    import pages.chat  # Loads the chat page
elif page == "Dashboard":
    st.experimental_set_page_config(page_title="Dashboard")
    import pages.Dashboard  # Loads the dashboard page

# Footer or additional global components (optional)
st.sidebar.markdown("### Harmony Bot v1.0")
st.sidebar.markdown("Developed with ❤️ using Nylas, Pinecone, and Google Generative AI")
