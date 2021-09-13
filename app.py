import os
import json

from models.user import User
from blocks.blocks import get_block
from slack_sdk import WebClient
from flask import Flask, request

admin = WebClient(token=os.environ['ADMIN_TOKEN'])
client = WebClient(token=os.environ['BOT_TOKEN'])

app = Flask(__name__)

meet_greet_channel = os.environ['CHANNEL']
user = {}

@app.route("/")
def index():
    return "Working!"


@app.route("/interact", methods=["POST"])
def interact():
  """
  Handle the payload from the user depending on what action they want to do. 
  The actions available are:
  - Remove: remove user from meet-greet channel
  - Add: add user to meet-greet channel
  """

  request_data = request.form.get('payload')
  data = json.loads(request_data)
  action = data['actions'][0]['action_id']
  user = User(data)

  if action == 'remove':
    return remove_user(user)
  elif action == 'add':
    return add_user(user)
  else:
    return "NOTHING HAPPENED"

  

def remove_user(user):
  """
  Get user's info and remove them from the #meet-and-greet channel
  """
  kicked_message_block = get_block("kicked_block.json")
  # kick user from channel
  admin.conversations_kick(
    channel=meet_greet_channel, 
    user=user.id
  )

  # Post ephemeral message
  client.chat_postEphemeral(
    user=user.id,
    channel=user.channel_from,
    text="Sorry to see you go {user}".format(user=user.name),
    blocks=kicked_message_block
  )
  return "success"


def add_user(user):
  """
  Get user's info and add them from the #meet-and-greet channel
  """
  admin.conversations_invite(
    channel=meet_greet_channel, 
    users=[user.id]
  )

  client.chat_postEphemeral(
    user=user.id,
    channel=user.channel_from,
    text="You were added back to #meet-and-greet! Yay!"
  )

  return "success"

  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)