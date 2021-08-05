
import os
from slack_sdk import WebClient

client = WebClient(token=os.environ['BOT_TOKEN'])

# Channel ID for #meet-and-greet
channel = "C029RN7ARKM"

def get_users():
  """
  Return list of all users in the TF user groups 
  """
  data = client.conversations_members(channel=channel)
  return sorted(data['members'])


if __name__ == '__main__':
  print(get_users())

