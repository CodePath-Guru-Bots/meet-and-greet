
class User:
  """
  User model contains the user id, name, and the channel where they made a request from
  """
  def __init__(self, data):
    self.id   = data['user']['id']
    self.name = data['user']['name']
    self.channel_from = data['container']['channel_id']