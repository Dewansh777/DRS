from flask import Flask, request, jsonify
from flask_cors import CORS
from model import search_embeddings
import logging
import os
# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app,origins=[
    'https://healthsync-alpha.vercel.app',
    'http://localhost:3000'
])

# Add a test endpoint for GET requests
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Doctor Recommendation API is running"}), 200

@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Test endpoint is working"}), 200

@app.route('/recommendation', methods=['POST'])
def get_recommendation():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        
        if not data:
            logger.error("No JSON data received")
            return jsonify({"error": "No data provided"}), 400
            
        query = data.get("query")
        
        if not query:
            logger.error("No query field in JSON data")
            return jsonify({"error": "No query provided"}), 400

        logger.info(f"Processing query: {query}")
        
        # Get recommendation from the model
        result = search_embeddings(query)
        
        logger.info(f"Search result: {result}")

        # Process the result and send back as JSON response
        if result and result.get('matches'):
            match = result['matches'][0]
            response = {
                'department': match.get('id', 'Unknown'),
                'score': match.get('score', 'N/A')
            }
            logger.info(f"Returning match: {response}")
            return jsonify(response)
            
        logger.warning("No matches found in search results")
        return jsonify({'error': 'No match found'}), 404
    
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    logger.info("Starting Flask application...")
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)