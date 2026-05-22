from flask import Flask
import socket
import platform
import datetime

app = Flask(__name__)

@app.route('/')
def home():

    return f"""
    <h1>DevOps EKS Platform</h1>

    <p><b>Hostname:</b> {socket.gethostname()}</p>

    <p><b>OS:</b> {platform.system()}</p>

    <p><b>OS Version:</b> {platform.release()}</p>

    <p><b>Machine:</b> {platform.machine()}</p>

    <p><b>Execution Time:</b> {datetime.datetime.now()}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
