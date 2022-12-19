
#~ Python program to implement columnar transposition cipher

def ctp_encryption(plain_text: str, key: str):
  keylen = len(key)
  ptlen = len(plain_text)
  cipher_text = ""
  enc_mx = [[plain_text[i: i + keylen]] for i in range(0, ptlen - keylen + 1, keylen)]      #~ +1 because endpoint is excluded but I want it included (NTS: Maybe do it the DES way)

  # 'enumerating' the key's chars. for corresponding columns' chars. to be picked up for cipher text
  keylist = list(key)
  sorted_keylist = sorted(list(key))
  included_indx = []

  # range used to not have to use 'index' function which inevitably returns index of first find   
  for i in range(len(sorted_keylist)):
    for j in range(len(keylist)):
      if sorted_keylist[i] == keylist[j] and j not in included_indx:           # if characters are equal and the index of the char. in the o.g keylist is not already used, use it as the column index for the enc_mx
        for row in range(len(enc_mx)):
          cipher_text += enc_mx[row][0][j]
        included_indx.append(j)
        break

  return cipher_text

def cpt_decryption(cipher_text: str, key: str):
  plain_text = ""

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
  cipher_text = ctp_encryption(plain_text, key)
  print("Cipher Text: ", cipher_text)

columnar_tp()