
#~ Python program to implement columnar transposition cipher

def columnar_tp():
  plain_text = input("Enter the plain text (preferably ALL CAPS, no SPACE): ").upper().replace(" ", "")
  key = input("Enter the key (preferably shorter than the Plaintext or it will be sliced): ")[:len(plain_text)].upper().replace(" ", "")
  keylen = len(key)
  while True:
    if len(plain_text) % keylen != 0:
      plain_text += 'X'
    else:
      break
  
  enc_mx = []
columnar_tp()