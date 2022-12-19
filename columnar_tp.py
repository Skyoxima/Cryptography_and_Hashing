
#~ Python program to implement columnar transposition cipher

def ctp_encryption(plain_text: str, key: str):
  keylen = len(key)
  ptlen = len(plain_text)
  enc_mx = [[plain_text[i: i + keylen]] for i in range(0, ptlen - keylen + 1, keylen)]

  print(enc_mx, sep="\n")

def columnar_tp():
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