from sentence_transformers import SentenceTransformer
from pinecone_integration import init_pinecone

# Initialize the SentenceTransformer model for embedding generation
model = SentenceTransformer('all-MiniLM-L6-v2')

def search_embeddings(query):
    # Generate the embedding for the query using SentenceTransformer
    query_embedding = model.encode(query).tolist()

    # Initialize Pinecone
    index = init_pinecone()

    # Query Pinecone for the top 1 result
    result = index.query(vector=query_embedding, top_k=1, include_metadata=True)
    
    return result
