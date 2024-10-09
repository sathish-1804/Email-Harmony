import streamlit as st
import pandas as pd
from src.email_handler import get_events, get_unread_emails
from datetime import timedelta

# Set the title of the page
st.title("Email Dashboard")

# Columns for selecting start and end dates
col1, col2 = st.columns(2)

# Date input for selecting the start date
with col1:
    start_date = st.date_input("Select start date", pd.to_datetime('today') - pd.to_timedelta(1, 'd'))

# Date input for selecting the end date
with col2:
    end_date = st.date_input("Select end date", pd.to_datetime('today'))

# Get events and unread emails for the selected date range
events = get_events(start_date, end_date)
unread_emails = get_unread_emails(start_date, end_date)

# Calculate the number of important emails
important_emails = len([msg for msg in unread_emails if msg['important']])

# Display metrics in columns
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Events Till Date", len(events))
with col2:
    st.metric("Important Mails", important_emails)
with col3:
    st.metric("Unread Emails", len(unread_emails))

# Create a dataframe to display the total and unread emails
data = {'Category': ['Total Emails', 'Unread Emails'], 'Value': [len(unread_emails), len(events)]}
df = pd.DataFrame(data, index=[1, 2])

# Display the data as a table
st.dataframe(df)

# Plot a bar chart for the email statistics
st.bar_chart(df.set_index('Category'))
