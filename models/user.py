

class User:

  def __init__(self, data):
    self.id   = data['user']['id']
    self.name = data['user']['name']
    self.channel_from = data['container']['channel_id']