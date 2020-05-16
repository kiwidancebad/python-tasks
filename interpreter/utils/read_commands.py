from .file_system.read_from_file import read_from_file

from constants.commands import COMMANDS

def read_commands(path):
  return read_from_file(path).splitlines()
