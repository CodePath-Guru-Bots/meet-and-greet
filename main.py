import os
from slack_sdk import WebClient

# Helper functions
from helpers.dates import get_rotation, tf_initial_date
from helpers.get_users import get_users
from helpers.conversations import Conversations

# Channel ID for #meet-and-greet
channel = os.environ['CHANNEL']
client = WebClient(token=os.environ['BOT_TOKEN'])
rotation = get_rotation(tf_initial_date)

def rotate(array: [str]) -> [str]:
  """
  Rotate users so that we prevent them from meeting with the same people again.
  We accomplish this by shifting the first student to the end of the line.
  """
  for n in range(rotation):
      # Rotate meetups (i.e. shift student 'John' to the end of array)
      array.append(array.pop(0))
  return array

def start_conversation(user_pair: (str, str)):
  """
  Start conversation with a pair of users (pair = 2 users) + bot user.
  Bot sends a welcome message to motivate students to introduce each other.
  """
  conversation = Conversations(client=client, user_pair=user_pair)
  conversation.start()

def create_user_pairs(array: [str]) -> [[str, str]]:
    return [ [array[x], array[-x - 1]] for x in range(len(array) // 2) ]

def main():
  """
  Create pairs of users that will meet up this week
  """
  rotated = rotate(all_users)
  user_pairs = create_user_pairs(rotated)

  for user_pair in user_pairs:
      start_conversation(user_pair=user_pair)


if __name__ == "__main__":
  all_users = get_users(channel)
  rotated = rotate(all_users)
  user_pairs = create_user_pairs(rotated)
  print("All users:", user_pairs)
  main()
