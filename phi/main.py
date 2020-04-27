from utils.phi import phi

testArr = [
  1245,
  7544,
  7935,
  6278,
  3405,
  4176,
  5972,
  9045,
  6712,
  5972,
  6735,
  7914,
  7842,
  6375,
  9145,
  3366,
  7912,
  6734,
]

for item in testArr:
  print("\nEuler's totient function for %s: "%(item) + str(phi(item)))
