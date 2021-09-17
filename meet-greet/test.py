import os
from slack_sdk import WebClient

client = WebClient(token=os.environ['BOT_TOKEN'])

bot_id = client.api_call("auth.test")["user_id"]

print("Bot id:", bot_id)

user_pair = ['U014YGS282Y', 'UDT3NN32B']

print(user_pair)

conversation = client.conversations_open(users=user_pair,return_im=True)
print(conversation)
channel_id = conversation["channel"]["id"]
text = "New test"

client.chat_postMessage(
  channel=channel_id, 
  text=text
)