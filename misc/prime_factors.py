def prime_factors(n):
  i = 2
  prime_factors_list = []

  while i * i <= n:
    while n % i == 0:
      prime_factors_list.append(i)
      n = n / i
    i = i + 1

  if n > 1:
    prime_factors_list.append(n)

  return prime_factors_list

tests = [108, 77, 65, 30, 159]

for i in range(0, len(tests)):
  print (prime_factors(tests[i]))
