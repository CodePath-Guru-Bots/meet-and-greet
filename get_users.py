
import os
from slack_sdk import WebClient

client = WebClient(token=os.environ['BOT_TOKEN'])


def _get_user_list_name():

  # user_group_name = [
  #   "Fall 2021 iOS New Tech Fellows",
  #   "Fall 2021 Cybersecurity Returning Tech Fellows",
  #   "Fall 2021 Android New Tech Fellows",
  #   "Fall 2021 Returning Tech Fellows",
  #   "Fall 2021 iOS Returning Tech Fellows",
  #   "Fall 2021 Android Returning Tech Fellows",
  #   "Fall 2021 New Tech Fellows",
  #   "Fall 2021 Cybersecurity New Tech Fellows",
  #   "Gurus"
  #   ]

  user_group_name = [
    "Guru - iOS"
    ]

  return user_group_name

#Helper function to get the user group ids
def _get_user_group_ids()-> list:
  """
  Returns a list of dict items that contain the name and id of a particular group
  """
  user_group_name = _get_user_list_name()

  user_groups_list = []
  user_groups_object = client.usergroups_list(include_users=True)
  user_groups = user_groups_object["usergroups"]
  for group in user_groups:
    if group["name"] in user_group_name:
      user_groups_list.append({"name": group["name"] , "id": group["id"]})
  return user_groups_list


# Final Function that should be called to get a list of usersids from group ids that willbe matched
def get_users():
  """
  Return list of all users in the TF user groups
  """
  all_users = set()
  group_ids = _get_user_group_ids()
  for group in group_ids:
    user_group_id = group["id"]
    group = client.usergroups_users_list(usergroup=user_group_id)
    users = set(group["users"])
    all_users.update(users)
  return sorted(list(all_users))

print(get_users())
