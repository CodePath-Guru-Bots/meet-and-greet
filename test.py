
# import os 
# import requests

# BOT_TOKEN = os.environ['BOT_TOKEN']

# url = 'https://slack.com/api/usergroups.list'
# headers = {'content-type': 'x-www-form-urlencoded' , 'Authorization': 'Bearer {token}'.format(token=BOT_TOKEN)}

# data = [
#  ('token', BOT_TOKEN),
#  ('usergroup', 'S25EV7UE8'),
# ]

# response = requests.post(url, data, headers)


# print(response.json())

# –––– Using Slack SDK
import os
from slack_sdk import WebClient
# from slack_sdk.errors import SlackApiError

client = WebClient(token=os.environ['BOT_TOKEN'])

user_groups = client.usergroups_list

print(user_groups)