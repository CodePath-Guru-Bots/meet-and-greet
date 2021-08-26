
import json

def get_block(block_file: str):
   with open('blocks/{file}'.format(file=block_file)) as f:
      data = json.load(f)
      return data['blocks']