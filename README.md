# Email Harmony: AI-powered Virtual Assistant for Email and Task Management

Email Harmony is a cutting-edge AI-powered virtual assistant designed to help users manage their emails, calendars, and contacts efficiently. In an era of increasing email overload, missed deadlines, and reduced productivity, Email Harmony simplifies the process by utilizing artificial intelligence and automation to streamline daily tasks and boost productivity.

## 🚀 Problem Statement

With the increasing volume of emails, users often face email overload, missed deadlines, and reduced productivity. Current email management tools lack a unified approach and fail to adapt to individual preferences, making it harder to organize and respond efficiently.

## 💡 Solution Overview

**Email Harmony** is here to change that! By leveraging the power of AI, it transforms the way you manage your email, calendar, and contacts, so you can focus on what truly matters.

### Key Features:
- **AI-powered Email Categorization**: Automatically categorize your emails using a third-party API (Nylas) and Natural Language Processing (NLP).
- **Automatic Calendar Management**: Schedule meetings, set reminders, and prevent missed appointments automatically with AI.
- **AI-driven Contact Organization**: Automates adding and deleting contacts based on interactions, reducing manual overhead.
- **Natural Language Processing**: Seamlessly communicate with the virtual assistant, making tasks like managing emails and scheduling events more intuitive.
- **User-friendly Interface**: The simple, clean UI ensures efficient task management and communication, allowing you to manage your inbox with ease.

## 📦 Project Structure

```bash
email-harmony/
│
├── config/                # Configuration files and environment loader
│   ├── secrets.toml       # Stores API keys for deployment (Streamlit Cloud)
│   ├── environment.py     # Handles environment variable loading
│   └── config_loader.py   # Centralized config loader for secrets/env variables
│
├── pages/                 # Streamlit pages for the app
│   ├── askMail.py         # Page for asking questions about emails
│   ├── chat.py            # Page for interacting with the assistant
│   └── Dashboard.py       # Page showing key email statistics
│
├── src/                   # Source folder for logic code (email, AI, embeddings)
│   ├── email_handler.py   # Handles Nylas email operations
│   ├── embedding.py       # Handles embedding operations using Pinecone
│   └── generative_ai.py   # Handles Generative AI logic for task automation
│
├── .env                   # Environment variables (local development)
├── .gitignore             # Ignores sensitive files and unnecessary clutter
├── requirements.txt       # List of Python dependencies
├── streamlit_app.py       # Main Streamlit app entry point
└── README.md              # Documentation for the project
