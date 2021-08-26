import json
from slack_sdk.errors import SlackApiError

class Conversations:
  """"
  This class would integrate the message class to create the text for the conversation

  This class would not be integrating the random function or any other helper functions. This class ideally will be sepcifically used for creating the converstaions when the users have already been derived
  """

  introduction_message = "Welcome to CodePath's Meet and Greet bot 👋🏻! Every week, we pair up TFs from all courses so they can get to know each other and share their stories! Feel free to start the converstaion 💬 by introducing yourselves (i.e. what school you go to, hobbies, what inspired you to get into tech, or anything new that you learned this week)!\n\nWe also encourage you all to schedule a time to meet using calendly.com, when2meet.com, or lettucemeet.com \n\nIf you wish to not participate anymore on weekly pairing meetups, you may remove yourself by pressing the \"Remove Me\" button or by leaving the #meet-and-greet channel and the bot will stop pairing you with other TFs."

  def __init__(self, client, user_pair):
    self.client = client
    self.user_pair = user_pair

  def start(self):
    try:
      conversation = self.client.conversations_open(users=self.user_pair,return_im=True)
      channel_id = conversation["channel"]["id"]
      blocks = self._get_welcome_message()
      
      self.client.chat_postMessage(
        channel=channel_id, 
        blocks=blocks,
        text=Conversations.introduction_message
      )

      print("\nConversation created for {self.user_pair}".format(self=self))
    except SlackApiError as e:
      print("\nError creating conversation for {self.user_pair} \n{e}".format(e=e,self=self))
  
  def _get_welcome_message(self):
    with open('helpers/message_block.json') as f:
      data = json.load(f)
      return data['blocks']

  def __str__(self):
    return "User pair: {self.user_pair}".format(self=self)
  

if __name__ == "__main__":
  print()
