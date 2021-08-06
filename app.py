import os
import json

from flask import Flask, request
from main import client

app = Flask(__name__)
meet_greet_channel = os.environ['CHANNEL']

@app.route("/")
def index():
    return "Working!"

@app.route("/kick", methods=["POST"])
def interact():
    request_data = request.form.get('payload')
    data = json.loads(request_data)
    user = data['user']['id']
    user_name = data['user']['name']
    channel_from = data['container']['channel_id']

    client.conversations_kick(
      channel=meet_greet_channel, 
      user=user
    )

    client.chat_postMessage(
      text="Sorry to see you go {user}".format(user=user_name), channel=channel_from
    )
    return   

app.run(host='0.0.0.0', debug=True)