import os
from slack_sdk import WebClient
# from slack_sdk.errors import SlackApiError

client = WebClient(token=os.environ['BOT_TOKEN'])

user_groups = client.usergroups_list

print(user_groups)
