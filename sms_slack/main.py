from flask import Flask, request, jsonify
from twilio.rest import TwilioRestClient

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
    client = TwilioRestClient(app.config['TWILIO_ACCOUNT_SID'], app.config['TWILIO_AUTH_TOKEN'])
    message = client.messages.create(to="+15084637343", from_="+12027538383",
                                     body="Hello there!")
    return 'You are here'

@app.route('/sms_to_slack', methods=['POST'])
def route_to_slack():
    # Stuff here
