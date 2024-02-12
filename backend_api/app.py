import time
import random
from flask import Flask, jsonify
import requests

app = Flask(__name__)

def generate_log():
    logs = [
        "Success",
        "Created",
        "Failed",
    ]
    return random.choice(logs)

@app.route('/api_1')
def api_call():
    log_message = generate_log()
    print(f"Operation log: {log_message}")
    time.sleep(0.5)  # Wait for half a second
    return f"completed: {log_message}"

@app.route('/download_external_logs', methods=['GET'])
def download_external_logs():
    # please think this parts as logs it is dummy but real :) 
    external_api_url = "https://dummyjson.com/auth/me"
    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTUsInVzZXJuYW1lIjoia21pbmNoZWxsZSIsImVtYWlsIjoia21pbmNoZWxsZUBxcS5jb20iLCJmaXJzdE5hbWUiOiJKZWFubmUiLCJsYXN0TmFtZSI6IkhhbHZvcnNvbiIsImdlbmRlciI6ImZlbWFsZSIsImltYWdlIjoiaHR0cHM6Ly9yb2JvaGFzaC5vcmcvYXV0cXVpYXV0LnBuZz9zaXplPTUweDUwJnNldD1zZXQxIiwiaWF0IjoxNjM1NzczOTYyLCJleHAiOjE2MzU3Nzc1NjJ9.n9PQX8w8ocKo0dMCw3g8bKhjB8Wo7f7IONFBDqfxKhs"}
    
    response = requests.get(external_api_url, headers=headers)
    
    if response.status_code == 200:
        return jsonify({"message": "External logs downloaded successfully"}), 200
    else:
        return jsonify({"error": "Failed to download external logs"}), response.status_code

@app.route('/health_check')
def health_check():
    return f"healthy"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
