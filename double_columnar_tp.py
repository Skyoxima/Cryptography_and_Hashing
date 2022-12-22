
#~ Implementing Double Columnar Transposition symmetric cryptography (See columnar_tp.py for explanation)
def text_padder(text, keylen):
  while True:
    if len(text) % keylen != 0:
      text += '_'
    else:
      break
  return text

def text_unpadder(text, keylen):
  while True:
    if len(text) % keylen != 0 and text[-1] == '_':
      text = text[:len(text) - 1]
    else:
      break
  return text

def key_orderer(key):
  key_list = list(key)
  sorted_key_list = list(sorted(key))
  col_order = [] 
  for i in range(len(sorted_key_list)):
    for j in range(len(key_list)):
      if sorted_key_list[i] == key_list[j] and j not in col_order:
        col_order.append(j)
        break
  return col_order

def columnar_tp_encryption(plain_text, key):
  cipher_text = ""
  keylen = len(key)
  col_order = key_orderer(key)
  plain_text = text_padder(plain_text, keylen)
  ptlen = len(plain_text)                            # length of plaintext should always be taken after padding
  enc_mx = [list(plain_text[i - keylen: i]) for i in range(keylen, ptlen + 1, keylen)]
  for col in col_order:
    cipher_text += "".join([enc_mx[row][col] for row in range(len(enc_mx))])
  return cipher_text

def columnar_tp_decryption(cipher_text, key):
  plain_text = ""
  keylen = len(key)
  col_order = key_orderer(key)
  ctlen = len(cipher_text)                            # length of the cipher_text should be taken before "unpadding"
  dec_mx = [[0 for _ in range(keylen)] for j in range(int(ctlen / keylen))]
  ct_curr_indx = 0
  
  for col in col_order:
    for row in range(len(dec_mx)):
      dec_mx[row][col] = cipher_text[ct_curr_indx]
      ct_curr_indx += 1

  for _ in range(len(dec_mx)):
    plain_text += "".join(dec_mx.pop(0))
  
  return plain_text

def double_columnar_encryption(plain_text: str, key1: str, key2: str):
  intermediate_ct = columnar_tp_encryption(plain_text, key1)
  # print("Intermediate Cipher Text: ", intermediate_ct)
  final_ct = columnar_tp_encryption(intermediate_ct, key2)
  return final_ct

def double_columnar_decryption(cipher_text, key1: str, key2: str):
  intermediate_pt = columnar_tp_decryption(cipher_text, key2)
  # print("Intermediate Plain Text: ", intermediate_pt)
  intermediate_pt = text_unpadder(intermediate_pt, len(key1))
  final_pt = columnar_tp_decryption(intermediate_pt, key1)
  return final_pt
  
def double_columnar():
  plain_text = input("Enter the plain text (preferably all caps, no space): ").upper().replace(" ", "")
  key1 = input("Enter the first key (preferably len(key) < len(plain_text)): ")[:len(plain_text)].upper().replace(" ", "")
  key2 = input("Enter the second key (preferably len(key) < len(plain_text)): ")[:len(plain_text)].upper().replace(" ", "")

  cipher_text = double_columnar_encryption(plain_text, key1, key2)
  print("Cipher Text: ", cipher_text)
  plain_text = double_columnar_decryption(cipher_text, key1, key2)
  print("Deciphered Text: ", plain_text)

double_columnar()