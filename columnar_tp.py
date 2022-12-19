
#~ Python program to implement columnar transposition cipher

# enumeration approach is required to handle repeated characters in the key as well... for repeated characters the one coming first is given more priority
def key_enumerator(key):
  keylist = list(key)
  sorted_keylist_enum = list(enumerate(sorted(keylist)))
  # print(sorted_keylist_enum)


def ctp_encryption(plain_text: str, key: str):
  keylen = len(key)
  ptlen = len(plain_text)
  enc_mx = [[plain_text[i: i + keylen]] for i in range(0, ptlen - keylen + 1, keylen)]      #~ +1 because endpoint is excluded but I want it included (NTS: Maybe do it the DES way)
  print(*enc_mx, sep="\n")
  key_enumerator(key)



def columnar_tp():
  print("Columnar Transposition")
  plain_text = input("Enter the plain text (preferably ALL CAPS, no SPACE): ").upper().replace(" ", "")
  key = input("Enter the key (preferably shorter than the Plaintext or it will be sliced): ")[:len(plain_text)].upper().replace(" ", "")
  keylen = len(key)
  while True:
    if len(plain_text) % keylen != 0:
      plain_text += 'X'
    else:
      break
  ctp_encryption(plain_text, key)
columnar_tp()