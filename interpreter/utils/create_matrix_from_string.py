import sys

def create_matrix_from_string(rows, cols, str):
  try:
    matrix_data = str.split(';')

    if ((rows * cols) != len(matrix_data)):
      raise Exception

    matrix = [[0 for i in range(rows)] for j in range(cols)]
    
    for i in range(rows):
      for j in range(cols):
        matrix[i][j] = matrix_data[0]
        matrix_data.pop(0)

    return matrix

  except Exception:
    print(
      '\nThere is not enough data for the matrix, or they are in abundance.' +
      ' ' + 'Should be %s, got %s.\n'%(rows * cols, len(matrix_data))
    )
    sys.exit(0)
