import os
from slack_sdk import WebClient

# Helper functions
from helpers.dates import get_rotation, tf_initial_date
from helpers.get_users import get_users
from helpers.conversations import Conversations

client = WebClient(token=os.environ['BOT_TOKEN'])

all_users = get_users()


def start_conversation(user_pair: (str, str)):
  """
  Start conversation with a pair of users (pair = 2 users) + bot user.
  Bot sends a welcome message to motivate students to introduce each other.
  """
  conversation = Conversations(client=client, user_pair=user_pair)
  conversation.start()


def rotate_users():
  """
  Rotate users so that we prevent them from meeting with the same people again.
  We accomplish this by shifting the first student to the end of the line.
  """
  rotation = get_rotation(tf_initial_date)
  for n in range(rotation):
      # Rotate meetups (i.e. shift student 'John' to the end of array)
      all_users.append(all_users.pop(0))


def main():
  """
  Create pairs of users that will meet up this week
  """
  pairs = [ [all_users[x], all_users[-x - 1]] for x in range(len(all_users) // 2) ]

  for user_pair in pairs:
      start_conversation(user_pair=user_pair)


if __name__ == "__main__":
    main()
