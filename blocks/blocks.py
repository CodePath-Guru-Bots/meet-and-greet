
import json

def get_block(block_file: str):
   """
   Get slack block message using the file name
   """

   with open('blocks/{file}'.format(file=block_file)) as f:
      data = json.load(f)
      return data['blocks']