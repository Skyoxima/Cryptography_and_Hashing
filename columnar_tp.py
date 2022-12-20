
#~ Python program to implement columnar transposition cipher

# Encryption -> Encryption_mx => PLaintext filled row-wise; According to the alphabetic order of the key's chars. pick columns in enc_mx and append those chars. in cipher_text
def ctp_encryption(plain_text: str, key: str):
  keylen, ptlen = len(key), len(plain_text)
  cipher_text = ""
  enc_mx = [list(plain_text[i: i + keylen]) for i in range(0, ptlen - keylen + 1, keylen)]      #~ +1 because endpoint is excluded but I want it included (NTS: Maybe do it the DES way)(Another NTS: Don't keep it as list of single strings, keep it as list of chars.)

  keylist = list(key)
  sorted_keylist = sorted(list(key))
  included_indx = []

  # range used to not have to use 'index' function which inevitably returns index of first find   
  for i in range(len(sorted_keylist)):
    for j in range(len(keylist)):
      if sorted_keylist[i] == keylist[j] and j not in included_indx:           # if characters are equal and the index of the char. in the o.g keylist is not already used, use it as the column index for the enc_mx
        for row in range(len(enc_mx)):
          cipher_text += enc_mx[row][j]
        included_indx.append(j)
        break

  return cipher_text

# Decryption -> fill the columns with slices of cipher_text based on the same ascending-arrangement of the key
def ctp_decryption(cipher_text: str, key: str):
  plain_text = ""
  keylen, ctlen = len(key), len(cipher_text)
  dec_mx = [[0 for i in range(keylen)] for j in range(int(ctlen / keylen))]
  ct_curr_indx = 0
  
  keylist, sorted_keylist = list(key), sorted(list(key))      # I've not imported this from the encryption block to keep the essence of messaging between 2 users, receiver will have to process the key on their own
  included_indx = []

  for i in range(len(sorted_keylist)):
    for j in range(len(keylist)):
      if sorted_keylist[i] == keylist[j] and j not in included_indx:           
        for row in range(len(dec_mx)):
          dec_mx[row][j] = cipher_text[ct_curr_indx]
          ct_curr_indx += 1
        included_indx.append(j)
        break

  for _ in range(len(dec_mx)):
    plain_text += "".join(dec_mx.pop(0))

  return plain_text

def columnar_tp():
  print("Columnar Transposition")
  plain_text = input("Enter the plain text (preferably ALL CAPS, no SPACE): ").upper().replace(" ", "")
  key = input("Enter the key (preferably shorter than the Plaintext or it will be sliced): ")[:len(plain_text)].upper().replace(" ", "")
  keylen = len(key)
  while True:
    if len(plain_text) % keylen != 0:
      plain_text += '_'
    else:
      break
  cipher_text = ctp_encryption(plain_text, key)
  print("Cipher Text: ", cipher_text)
  plain_text = ctp_decryption(cipher_text, key)
  print("Plain Text: ", plain_text)

columnar_tp()