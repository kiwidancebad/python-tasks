def read_from_file(path):
  try:
    with open(path, 'r') as f:
      return f.read()

  except IOError:
    print('Cannot open file from ' + path)
