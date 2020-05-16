# _ - symbolizing an argument for command
COMMANDS = [
  {
    'name': 'create object',
    'code': 'cco',
    'pattern': 'cco',
    'hasArguments': False
  },
  {
    'name': 'create subject',
    'code': 'ccs',
    'pattern': 'ccs',
    'hasArguments': False
  },
  {
    'name': 'destroy object',
    'code': 'cdo',
    'pattern': 'cdo _',
    'hasArguments': True
  },
  {
    'name': 'destroy subject',
    'code': 'cds',
    'pattern': 'cds _',
    'hasArguments': True
  },
  {
    'name': 'enter p into matrix',
    'code': 'cer',
    'pattern': "cer '_' _ _",
    'hasArguments': True
  },
  {
    'name': 'delete p from matrix',
    'code': 'cdr',
    'pattern': "cdr '_' _ _",
    'hasArguments': True
  }
]
