def is_simple(num):
  lst = [2]

  for i in range(3, num + 1, 2):
    if (i > 10) and (i % 10 == 5):
      continue
    for j in lst:
      if j*j - 1 > i:
        lst.append(i)
        break
      if (i % j == 0):
        break
    else:
      lst.append(i)

  return lst

def mutually_simple(list1, list2):
  return list(set(list1).intersection(list2))

test = [[25, 12], [25, 15], [13, 39], [40, 27]]

for i in range(0, len(test)):
  print ('For %d and %d: '%(test[i][0], test[i][1]) + str((mutually_simple(is_simple(test[i][0]), is_simple(test[i][1]))))) 
