def write_to_file(fileName, value):
  try:
    f = open(fileName, 'a')
    try:
      s = str(value)
      f.write(s)

    finally:
      f.close()
    
  except IOError:
    print('Cannot write to file %s. Value %s is not written.'%(fileName, str(value)))
