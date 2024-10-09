from nylas import Client
import os

# Initialize Nylas client using environment variables
nylas = Client(os.environ.get("NYLAS_API_KEY"), os.environ.get("NYLAS_API_URI"))

# Function to retrieve an email by its ID
def retrieve_email_by_id(id):
    return nylas.messages.find(os.environ.get("NYLAS_EMAIL"), id)

# Function to get events for a specific calendar and date range
def get_events(start_date, end_date):
    return nylas.events.list(
        os.environ.get("NYLAS_EMAIL"),
        query_params={"calendar_id": os.environ.get("NYLAS_CALENDAR_ID")}
    )

# Function to get unread emails for a specific date range
def get_unread_emails(start_date, end_date):
    query_params = {"search_query_native": f"after:{start_date} before:{end_date} is:unread"}
    return nylas.messages.list(os.environ.get("NYLAS_EMAIL"), query_params=query_params)

# Function to retrieve the most recent email
def last_email(query):
    messages = nylas.messages.list(
        os.environ.get("NYLAS_EMAIL"),
        query_params={"limit": 1, "search_query_native": 'is:inbox'}
    )
    if messages:
        return messages[0]  # Return the latest message
    return None

# Function to send an email reply using Nylas
def mail_reply(prompt, email_id):
    message = retrieve_email_by_id(email_id)
    if message:
        # Prepare the metadata of the email
        metadata = {
            "snippet": message.snippet,
            "from": message.from_,
            "to": message.to,
            "subject": message.subject,
            "date": message.date,
            "id": message.id
        }
        # Logic for generating a reply based on the prompt and metadata
        # This will interact with the Generative AI model in src/generative_ai.py
        from src.generative_ai import answer_question
        response = answer_question(metadata, prompt)
        
        # Send the email reply
        nylas.messages.send(
            os.environ.get("NYLAS_EMAIL"),
            request_body={
                "to": [{"name": response[0], "email": message.from_[0]['email']}],
                "reply_to": [{"name": response[0], "email": message.from_[0]['email']}],
                "subject": response[2],
                "body": response[3],
            }
        )
        return f"{response[3]} \n The email content has been sent successfully"
    return "No matching email found for the provided ID."
