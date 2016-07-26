# SMS-to-Slack relay
A simple relay in Flask to route Twilio SMS messages to Slack. Ready to deploy to Heroku.

## Installation: Slack

In Slack, create an [API access token](https://api.slack.com/tokens).

## Installation: Heroku

After creating the app and deploying this code, set these config values:

<img width="912" alt="heroku-config" src="https://cloud.githubusercontent.com/assets/149811/17123224/098880da-52b0-11e6-91eb-df84114d87fd.png">

`INCOMING_REQUEST_TOKEN` is an arbitrary string that you'll also set in the Twilio webhook, below.

`SLACK_CHANNEL` is the channel, obv. Include the `#`.

`SLACK_TOKEN` is the API access token you created above.

## Installation: Twilio

You'll need some incoming SMS long- or short-code that routes to Twilio. Configure the "Messaging" Webhook to send to

`https://my-app.herokuapp.com/sms_to_slack/INCOMING_REQUEST_TOKEN`

Where `my-app.herokuapp.com` is the domain of your deployed app, and `SOME_TOKEN` is the token you set in the Heroku settings, above.
