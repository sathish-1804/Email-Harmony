import google.generativeai as genai
import os

# Configure Google Generative AI with the API key from environment variables
genai.configure(api_key=os.environ.get("GENAI_API_KEY"))

# Initialize the Generative AI model (Gemini Pro in this case)
model = genai.GenerativeModel('gemini-pro')

# Function to answer a question using the Generative AI model
def answer_question(context, question=None):
    # Prepare the prompt based on context and question (if provided)
    prompt = f"Context: {context}\n"
    if question:
        prompt += f"User Question: {question}\n"
    prompt += "Provide a detailed answer."

    # Generate the response using the model
    response = model.generate_content(prompt)
    return response

# Example for generating email replies based on context and user prompt
def generate_email_reply(context, user_prompt):
    prompt = f"Context: {context}\n"
    prompt += f"User Query: {user_prompt}\n"
    prompt += "Generate a professional email reply based on the user's query."

    # Generate the email reply using the model
    response = model.generate_content(prompt)
    return response

# Example usage in another module:
# context = {"subject": "Meeting Reminder", "snippet": "Don't forget our meeting at 3 PM"}
# question = "Can you reply to this email?"
# answer = answer_question(context, question)
