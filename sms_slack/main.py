from flask import Flask, request, jsonify
from twilio.rest import TwilioRestClient

import json, os, requests

try:
    from flask_cors import CORS  # The typical way to import flask-cors
except ImportError:
    # Path hack allows examples to be run without installation.
    parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(0, parentdir)

    from flask_cors import CORS

app = Flask(__name__)

# Twilio credentials
app.config['TWILIO_ACCOUNT_SID'] = os.environ['TWILIO_ACCOUNT_SID']
app.config['TWILIO_AUTH_TOKEN'] = os.environ['TWILIO_AUTH_TOKEN']

# To verify incoming requests
app.config['INCOMING_REQUEST_TOKEN'] = os.environ['INCOMING_REQUEST_TOKEN']

# Slack webhook
app.config['SLACK_WEBHOOK_URL'] = os.environ['SLACK_WEBHOOK_URL']

# Debug mode
app.config['DEBUG'] = os.environ['DEBUG']

@app.route('/')
def hello():
    client = TwilioRestClient(app.config['TWILIO_ACCOUNT_SID'], app.config['TWILIO_AUTH_TOKEN'])
    # message = client.messages.create(to="+15084637343", from_="+12027538383",
                                     # body="Hello there!")
    return 'You are here'

@app.route('/sms_to_slack/<request_token>', methods=['POST'])
def route_to_slack(request_token):
    # Stuff here
    app.logger.debug("Received request with token = %s", request_token)
    app.logger.debug(request.form)

    # payload={"channel": "#ghost-inspector", "username": "webhookbot", "text": "This is posted to #ghost-inspector and comes from a bot named webhookbot.", "icon_emoji": ":ghost:"}

    message = "SMS from %s: %s" % (request.form["From"], request.form["Body"])
    payload = {"channel": "#ghost-inspector", "username": "twilio", "text": message, "icon_emoji": ":phone:"}

    r = requests.post(app.config['SLACK_WEBHOOK_URL'], data = payload)

    return ''
