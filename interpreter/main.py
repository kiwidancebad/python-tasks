from utils.file_system.read_from_file import read_from_file
from utils.file_system.write_to_file import write_to_file

from utils.create_matrix_from_string import create_matrix_from_string

if __name__ == '__main__':
  read_data = read_from_file('environment.txt')
  read_data = read_data.splitlines()

  try:
    if (len(read_data) < 3):
      raise Exception

  except Exception:
    print('Data is missing one of the arguments. N, M or matrix data.')

  N = int(read_data[0])
  M = int(read_data[1])
  matrix_data = read_data[2]
