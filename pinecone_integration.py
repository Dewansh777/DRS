import os
from pinecone import Pinecone, ServerlessSpec

def init_pinecone():
    
    pc = Pinecone(api_key="pcsk_6q59Gh_DKs6cepjWantsk5G96CmEMpWhUSurpYehQ4R1kquqzq2QyRMmXsYChWpvH62DCJ")

    # Check if the index exists, and create it if not
    if 'doctors-recommendation' not in pc.list_indexes().names():
        pc.create_index(
            name='doctors-recommendation',
            dimension=384,  
            metric='cosine', 
            spec=ServerlessSpec(
                cloud='aws',  
                region='us-east-1'  
            )
        )

    
    index = pc.Index("doctors-recommendation")
    return index
