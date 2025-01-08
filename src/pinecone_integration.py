import os
from pinecone import Pinecone, ServerlessSpec

def init_pinecone():
    ap = os.getenv('PINECONE_API_KEY')
    pc = Pinecone(api_key=ap)

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
