
#~ A simple Python program to implement Hill Cipher (Encryption and Decryption)
import numpy as np

def dynamic_list_slicer(list_, slice_size):
  return [list_[i - slice_size: i] for i in range(slice_size, len(list_) + 1, slice_size)]

def hill_cipher_encryption(plain_text: str, key: str):
  char_decimal_eqv = {chr(i): i - 65 for i in range(65, 91)}
  decimal_char_eqv = {i - 65: chr(i) for i in range(65, 91)}
  cipher_text = ""
  pt_blocks = dynamic_list_slicer(plain_text, 9)    # each block is of len = 9, 3 x 3 matrices will be formed for each block
  pt_matrices = [[list(map(lambda x: char_decimal_eqv[x], list(block[i - 3: i]))) for i in range(3, len(block) + 1, 3)] for block in pt_blocks]
  
  key_mx = dynamic_list_slicer(list(map(lambda x: char_decimal_eqv[x], list(key))), 3)
  encrypted_matrices = []
  for pt_mx in pt_matrices:
    encrypted_matrices.append((np.dot(key_mx, pt_mx) % 26).tolist())
  
  for ct_mx in encrypted_matrices:
    cipher_text += "".join([decimal_char_eqv[j] for i in ct_mx for j in i])
  return cipher_text
  
def hill_cipher():
  plain_text = input("Enter the plain text (uppercase English Alphabets only): ").upper().replace(" ", "")
  while len(plain_text) % 9 != 0:
    plain_text += 'X'
  key = input("Enter the 9-letter key: ")[:10].upper().replace(" ", "")
  while len(key) != 9:
    key += 'X'
  
  cipher_text = hill_cipher_encryption(plain_text, key)
  print("\033[38;2;240;10;10mCipher Text: ", cipher_text, "\033[0m")
hill_cipher()