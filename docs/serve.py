#!/usr/bin/env python3
"""
Simple local server for the static site
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

def serve_site(port=8000):
    """Serve the static site on localhost"""

    # Change to the docs directory
    os.chdir(Path(__file__).parent)

    # Create server
    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"🌐 Serving static site at http://localhost:{port}")
        print(f"📁 Serving files from: {os.getcwd()}")
        print("🔄 Press Ctrl+C to stop the server")
        print("🌍 Opening browser...")

        # Open browser automatically
        webbrowser.open(f"http://localhost:{port}")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.server_close()
            print("\n👋 Server stopped")
            

if __name__ == "__main__":
    serve_site()
