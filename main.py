
# Python Libraries
import os
from datetime import date
from itertools import combinations, chain

# Third-party
from slack_sdk import WebClient

# Helper functions
from helpers.dates import get_rotation
from helpers.get_users import get_users
from helpers.conversations import Conversations

# Channel ID for #meet-and-greet
channel = os.environ['CHANNEL']
client = WebClient(token=os.environ['BOT_TOKEN'])

def start_conversation(user_pair: (str, str)):
  """
  Start conversation with a pair of users (pair = 2 users)
  Bot sends a welcome message to motivate students to introduce each other.
  """
  conversation = Conversations(client=client, user_pair=user_pair)
  conversation.start()

def create_user_pairs(user_array: [str], rotation: int) -> [[str, str]]:
  rotation_count = rotation % (len(user_array) - 1)
  
  c = combinations(user_array, 2)
  pair_quantity = len(user_array) // 2
  if len(user_array) % 2 != 0:
    pair_quantity += 1

  # This big line basically creates a list of sets of pairs for each week
  # This ensures that there are no repeats for that particular week
  # Everyone gets a chance to meet everyone
  unique_pairings = [list(set(i)) for i in list(combinations(c,pair_quantity)) if (len(set(user_array) & set(chain(*i))) == len(user_array))]
  return unique_pairings[rotation_count]
  

def create_conversations(all_pairings: [[(str, str)]]):
  """
  Start conversation with user pairs of users that will meet up this week
  """
  for user_pair in all_pairings:
      start_conversation(user_pair=user_pair)

def main():
  initial_date = date(2021,9,13)
  rotation = get_rotation(initial_date)
  all_users = get_users(channel)
  user_pairs = create_user_pairs(all_users, rotation)
  create_conversations(user_pairs)

# def test():
#   users = list("ABCDEFG")
#   create_user_pairs(users, 0)

# def test():
#   date1, date2, date3, date4, date5, date6 = date(2021,9,7), date(2021,9,8), date(2021,9,9), date(2021, 9,10), date(2021,9,11), date(2021,9,12)
#   dates = [date1, date2, date3, date4, date5, date6]
#   for d in dates:
#     rotation = get_rotation(d)
#     all_users = get_users(channel)
#     user_pairs = create_user_pairs(all_users, rotation)
#     # print(user_pairs)
#     # create_conversations(user_pairs)

if __name__ == "__main__":
  main()
  # test()

