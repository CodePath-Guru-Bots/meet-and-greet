import json

class Conversations:
  """"
  This class would integrate the message class to create the text for the conversation

  This class would not be integrating the random function or any other helper functions. This class ideally will be sepcifically used for creating the converstaions when the users have already been derived
  """

  def __init__(self, client, user_pair):
    self.client = client
    self.user_pair = user_pair

  def start(self):
    conversation = self.client.conversations_open(users=self.user_pair,urn_im=True)
    channel_id = conversation["channel"]["id"]
    blocks = self._get_welcome_message()
    
    self.client.chat_postMessage(
      channel=channel_id,
      blocks=blocks
    )
  
  def _get_welcome_message(self):
    with open('helpers/message_block.json') as f:
      data = json.load(f)
      return data['blocks']
  

if __name__ == "__main__":
  print()
