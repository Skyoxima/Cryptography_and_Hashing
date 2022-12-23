def DHKE():
  g, p = 5, 23
  a, b = 4, 3
  Xa = (g ** a) % p
  Xb = (g ** b) % p
  SSA = (Xb ** a) % p
  SSB = (Xa ** b) % p
  if SSA == SSB:
    print("Connection Established")

DHKE()