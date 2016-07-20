from flask import Flask, request, jsonify

import json, os

try:
    from flask.ext.cors import CORS  # The typical way to import flask-cors
except ImportError:
    # Path hack allows examples to be run without installation.
    parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(0, parentdir)

    from flask.ext.cors import CORS

app = Flask(__name__)

app.config['TWILIO_ACCOUNT_SID'] = os.environ['TWILIO_ACCOUNT_SID']
app.config['TWILIO_AUTH_TOKEN'] = os.environ['TWILIO_AUTH_TOKEN']

# To verify incoming requests
app.config['INCOMING_REQUEST_TOKEN'] = os.environ['INCOMING_REQUEST_TOKEN']

@app.route('/')
def hello():
    return 'You are here'
