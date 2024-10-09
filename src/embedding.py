import google.generativeai as genai
import os
from pinecone import Pinecone

# Configure Google Generative AI with the API key from environment variables
genai.configure(api_key=os.environ.get("GENAI_API_KEY"))

# Initialize Pinecone client with API key from environment variables
pinecone_client = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
index = pinecone_client.Index("ask-mail")

# Function to generate an embedding for a given content using Generative AI
def generate_embedding(content):
    result = genai.embed_content(
        model="models/embedding-001",
        content=content,
        task_type="retrieval_query"
    )
    return result['embedding']

# Function to query Pinecone using the generated embedding
def query_pinecone(embedding, top_k=3):
    res = index.query(
        vector=embedding,
        top_k=top_k,
        include_values=False
    )
    return res.matches

# Example usage in another module:
# embedding = generate_embedding("Example content")
# matches = query_pinecone(embedding)
