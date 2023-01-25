import math
#TODO - Rectify make_prime, add conditions for 0 and 1 length p and q 
def make_closest_prime(number, *exclude):
  i = 2
  while i <= int(number / 2) + 1:
    if number % i == 0:
      number += 1
      while number in exclude:
        number += 1
      i = 2
    else:
      i += 1
  return number

def relatively_prime_finder(totient, *exclude):
  for i in range(2, int(totient / 2) + 1):           # since e has to be less than totient 
    if math.gcd(i, totient) == 1:
      if i not in exclude:
        return i

def extended_euclidean_algorithm(Φn, e):
  exe_table = {'x': [1, 0], 'y': [0, 1], 'r': [Φn, e], 'q': [-1]}         # initial conditions for every extended Euclidean algorithm table
  
  while exe_table['r'][-1] != 1:                                         # The stopping condition in r column whose corr. y is our 'd'  -> (This was a doubt too, why is the answer of y considered as d and what does the value of x signify)
    exe_table['q'].append(int(exe_table['r'][-2] / exe_table['r'][-1]))  # for this column, the current value (one which is just getting appended) is always the division of the pre-previous and previous
    exe_table['x'].append(exe_table['x'][-2] - exe_table['x'][-1] * exe_table['q'][-1])   # for both 'x' and 'y' columns, the current value comes out from the formula xi = xi-2 - xi-1*qi-1 
    exe_table['y'].append(exe_table['y'][-2] - exe_table['y'][-1] * exe_table['q'][-1])
    exe_table['r'].append(exe_table['r'][-2] % exe_table['r'][-1])

  return (exe_table['y'][-1]) % Φn         # taking care of additive inverse if applicable

def RSA():
  PT = int(input("Enter the number to be encrypted: "))
  print("Enter p and q which are public, mutually accepted numbers between the sender and the receiver")
  p = len(input("Enter the string p, (length should be > 3): "))
  if p < 10:
    raise ValueError("Cannot have number lesser than 10 for 'p'")
  while True:
    q = len(input("Enter the passphrase q, (length should be > 10 and not as same as p): "))
    if q < 10:
      raise ValueError("Cannot have number lesser than 10 for 'q'")
    elif q == p:
      print("Length of q cannot be p!")
    else:    
      break
  p = make_closest_prime(p)
  q = make_closest_prime(q, p)

  print(f"p = {p}, q = {q}")
  n = p * q
  Φn = (p - 1) * (q - 1)
  print(f"n = {n}, Φn = {Φn}")
  e = relatively_prime_finder(Φn, p, q)
  print(f"e = {e}")
  d = extended_euclidean_algorithm(Φn, e)
  print("d = ", d)

  PT %= n
  print("Plain Text: ", PT)
  CT = (PT ** e) % n 
  print("Cipher Text: ", CT)

  PT = (CT ** d) % n 
  print("Plain Text: ", PT)

RSA()