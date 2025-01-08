import json
from sentence_transformers import SentenceTransformer
from pinecone_integration import init_pinecone
import os
import time

# Initialize SentenceTransformer model for embedding generation
model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embedding(description):
    # Generate the embedding for the description using SentenceTransformer
    embedding = model.encode(description).tolist()
    return embedding

def upload_embeddings():
    file_path = os.path.join(os.path.dirname(__file__), "../data/departments.json")
    print(f"Loading data from {file_path}")
    
    # Load the department data from the JSON file
    with open(file_path, "r") as f:
        departments = json.load(f)

    # Initialize Pinecone
    index = init_pinecone()

    # Loop through the departments and upload embeddings
    for department in departments:
        description = department["description"]
        print(f"Uploading embedding for department: {department['department']}")

        # Generate embedding for the description using SentenceTransformer
        embedding = generate_embedding(description)

        # Upsert the embedding into Pinecone index
        index.upsert([(department["department"], embedding)])

        # Optional: Add a delay between requests to reduce load on the API
        time.sleep(1)  # Sleep for 1 second between requests to avoid hitting rate limits too quickly

    print("Embeddings uploaded successfully!")

if __name__ == "__main__":
    upload_embeddings()
