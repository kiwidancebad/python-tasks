from constants.commands import COMMANDS

def is_command_valid(command):
  if len(command) < 3:
    return False 

  for i in COMMANDS:
    if i.get('code') == command[0:3]:
      print('valid')

  return True
