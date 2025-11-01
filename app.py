import requests
from flask import Flask, jsonify

# App A runs on port 3001
app = Flask(__name__)

# URL for Microservice B (which runs on localhost:3000)
APP_B_URL = 'http://mi-servicio-2.santiago-parraga-dev.svc.cluster.local:3000/'

@app.route('/', methods=['GET'])
def call_app_b():
    """Endpoint for App A (the caller) that connects to App B."""
    try:
        # 1. Make the HTTP GET request to App B
        response_b = requests.get(APP_B_URL)
        response_b.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        # 2. Get the content from App B
        app_b_data = response_b.text

        # 3. Combine the response for the user
        combined_response = f"Hola Mundo from App A (Port 3001)! Successfully called App B. \n\n" \
                            f"--- Response from App B ---\n" \
                            f"{app_b_data}"
        
        return combined_response, 200

    except requests.exceptions.RequestException as e:
        # Handle connection errors (e.g., App B is not running)
        return jsonify({
            "error": "..Failed to connect to Microservice B...",
            "details": str(e)
        }), 500

@app.route('/health', methods=['GET'])
def call_health():
    return 'OK', 200

@app.route('/startup', methods=['GET'])
def call_startup():
    return 'OK', 200
    
@app.route('/readiness', methods=['GET'])
def call_readiness():
    return 'OK', 200

if __name__ == '__main__':
    # Running on 0.0.0.0 and port 3001
    app.run(host='0.0.0.0', port=3000)
