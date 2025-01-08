import json
from sentence_transformers import SentenceTransformer
from pinecone_integration import init_pinecone
import os

# Initialize SentenceTransformer model for embedding generation
model = SentenceTransformer('all-MiniLM-L6-v2')

def search_embeddings(query):
    # Generate the embedding for the query using SentenceTransformer
    query_embedding = model.encode(query).tolist()

    # Initialize Pinecone
    index = init_pinecone()

    # Query the Pinecone index and get the top 1 result
    result = index.query(vector=query_embedding, top_k=1, include_metadata=True)
    
    return result

def display_results(query, results):
    print(f"Query: {query}")
    # Display the top result
    match = results['matches'][0]
    print(f"Department: {match['id']}, Score: {match['score']}")

if __name__ == "__main__":
    query = input("Enter your query: ")  
    results = search_embeddings(query)
    display_results(query, results)
