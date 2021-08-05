class Conversations:
  """"
  This class would integrate the message class to create the text for the conversation

  This class would not be integrating the random function or any other helper functions. This class ideally will be sepcifically used for creating the converstaions when the users have already been derived
  """

  welcome_message = "Welcome to CodePath's Meet and Greet bot 👋🏻! Every week, we pair up TFs from all courses so they can get to know each other and share their stories ! Feel free to start the converstaion 💬 by introducing yourselves (i.e. what school you go to, hobbies, what inspired you to get into tech, or anything new that you learned this week)! We also encourage you all to schedule a time to meet using calendly.com, when2meet.com, or lettucemeet.com"

  def __init__(self, client, user_pair):
    self.client = client
    self.user_pair = user_pair

  def start(self):
    conversation = self.client.conversations_open(users=self.user_pair,urn_im=True)
    channel_id = conversation["channel"]["id"]
    self.client.chat_postMessage(channel=channel_id, text=Conversations.welcome_message)


# conv = Conversations(client=client, user_pair=users)
# conv.start()
