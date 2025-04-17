"""
Written by tipsy + gepetto.

Server which passes files to file enabled framebyframe, allowing app like access with exe opening url

Changelog:
17/04/25 Init.
"""

from flask import Flask, request, send_file, render_template, abort
import os

app = Flask(__name__)

PORT = 1704
ALLOWED_EXTENSIONS = {'mp4', 'webp', 'gif'}  # Only allow these file types

def allowed_file(filename):
    # Check if the file has an allowed extension
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Serve the frontend
@app.route("/")
def home():
    file_path = request.args.get("file")  # Get ?file=C:\test.jpg
    
    if file_path and os.path.exists(file_path) and allowed_file(file_path):
        return render_template("index.html", file_path=file_path)
    
    return "Invalid file or not allowed", 400

# Safely send the requested file
@app.route("/get_file")
def get_file():
    file_path = request.args.get("path")
    
    if not file_path or not os.path.isfile(file_path):
        return "File not found", 404
    
    if not allowed_file(file_path):
        return "File type not allowed", 400

    # Optional paranoia check: disallow any sneaky '../' even in an absolute path
    if '..' in file_path.replace('\\', '/'):
        return "No sneaky paths", 400

    return send_file(file_path)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=PORT)
    print("FIN")
    