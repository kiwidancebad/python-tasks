def print_error(message):
  if (type(message) != "string"):
    print('Print error error! Message must be a string.')
    return

  print('\nERROR! Message: %s\n'%(message))
