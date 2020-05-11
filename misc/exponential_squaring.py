def power(g_base, a, p_mod):
  x=1
  bits = "{0:b}".format(a)

  for i, bit in enumerate(bits):
    if bit == '1': x = (((x**2) * g_base) % p_mod)
    elif bit == '0': x = ((x**2) % p_mod)

  return x % p_mod

print (power(2, 8, 10))
