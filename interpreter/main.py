import sys

from utils.read_commands import read_commands

from utils.print_error import print_error
from utils.file_system.write_to_file import write_to_file

from utils.file_system.read_from_file import read_from_file
from utils.create_matrix_from_string import create_matrix_from_string

from utils.apply_changes import apply_changes

if __name__ == '__main__':
  ENVIRONMENT_FILE_PATH = './environment.txt'
  COMMANDS_FILE_PATH = './commands.txt'

  try:
    read_data = read_from_file(ENVIRONMENT_FILE_PATH)
    read_data = read_data.splitlines()

    if (len(read_data) < 3):
      raise Exception

    N = int(read_data[0])
    M = int(read_data[1])
    matrix_data = read_data[2]

    matrix = create_matrix_from_string(N, M, matrix_data)

    commands_list = read_commands(COMMANDS_FILE_PATH)

    apply_changes(matrix, commands_list)

  except Exception:
    print_error('Data is missing one of the arguments. N, M or matrix data.')
    sys.exit(0)
