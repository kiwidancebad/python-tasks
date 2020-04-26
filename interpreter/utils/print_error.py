def print_error(message):
  if (type(message) != "string"):
    print('Error! Message must be a string.')
    return

  print('\n%s\n'%(message))
