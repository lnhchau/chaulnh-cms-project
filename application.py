"""
This script runs the FlaskWebProject application using a development server.
"""
from dotenv import load_dotenv
import os
from FlaskWebProject import app
import logging

load_dotenv()

if __name__ == '__main__':
    app.debug = True
    HOST = os.environ.get('SERVER_HOST')
    try:
        PORT = int(os.environ.get('SERVER_PORT'))
    except ValueError:
        PORT = 443
    app.run(HOST, PORT, ssl_context='adhoc')