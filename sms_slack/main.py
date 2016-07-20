from flask import Flask, request, jsonify
# from twilio.rest import TwilioRestClient
from slacker import Slacker

import json, os, requests

app = Flask(__name__)

# Slack credentials
app.config['SLACK_TOKEN'] = os.environ['SLACK_TOKEN']
# This is assumed to inlude the '#'
app.config['SLACK_CHANNEL'] = os.environ['SLACK_CHANNEL']

# Request token (set in env vars, and passed as /sms_to_slack/<request_token>)
app.config['REQUEST_TOKEN'] = os.environ['INCOMING_REQUEST_TOKEN']

# Debug mode
app.debug = False
if 'DEBUG' in os.environ and os.environ['DEBUG'] == 'True':
    app.debug = True

@app.route('/')
def hello():
    return 'You are here'

@app.route('/sms_to_slack/<request_token>', methods=['POST'])
def route_to_slack(request_token):

    if app.debug:
        app.logger.debug("Received request with token = %s", request_token)
        app.logger.debug(request.form)

    # Check token -- should match env var INCOMING_REQUEST_TOKEN
    if request_token != app.config['REQUEST_TOKEN']:
        app.logger.error("Incorrect token %s", request_token)
        return json.dumps({
            'meta': {
                'code': 401,
                'errorType': 'token_error',
                'errorDetail': 'Incorrect request token'
            },
        }), 401

    # payload={"channel": "#ghost-inspector", "username": "webhookbot", "text": "This is posted to #ghost-inspector and comes from a bot named webhookbot.", "icon_emoji": ":ghost:"}

    message = "SMS from %s: %s" % (request.form["From"], request.form["Body"])
    payload = {"channel": app.config['SLACK_CHANNEL'], "username": "twilio", "text": message, "icon_emoji": ":phone:"}

    # r = requests.post(app.config['SLACK_WEBHOOK_URL'], data = payload)

    slack = Slacker(app.config['SLACK_TOKEN'])

    slack.chat.post_message('#ghost-inspector', message)

    return ''
