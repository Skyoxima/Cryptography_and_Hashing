
#~ A simple Python program to implement Hill Cipher (Encryption and Decryption)
import numpy as np
import math
from typing import List

def dynamic_list_slicer(list_, slice_size):
  return [list_[i - slice_size: i] for i in range(slice_size, len(list_) + 1, slice_size)]

def return_reqd_matrices(text, key, return_pt_matrices = True):
  char_decimal_eqv = {chr(i): i - 65 for i in range(65, 91)}
  key_mx = dynamic_list_slicer(list(map(lambda x: char_decimal_eqv[x], list(key))), 3)
  if return_pt_matrices:
    text_blocks = dynamic_list_slicer(list(map(lambda x: char_decimal_eqv[x], list(text))), 9)    # each block is of len = 9, 3 x 3 matrices will be formed for each block
    text_cde_matrices = [[block[i - 3: i] for i in range(3, len(block) + 1, 3)] for block in text_blocks]
    return text_cde_matrices, key_mx
  else:
    return key_mx
  
def hill_cipher_encryption(plain_text, key):
  decimal_char_eqv = {i - 65: chr(i) for i in range(65, 91)}
  cipher_text = ""
  
  pt_matrices, key_mx = return_reqd_matrices(plain_text, key)
  print("Key matrix: ", key_mx)
  print("Plain Text Matrices: ", pt_matrices)
  
  encrypted_matrices = []
  for pt_mx in pt_matrices:
    enc_mx = (np.dot(key_mx, pt_mx) % 26).tolist()
    encrypted_matrices.append(enc_mx)
  
  print("Encrypted Matrices: ", encrypted_matrices)
  for ct_mx in encrypted_matrices:
    cipher_text += "".join([decimal_char_eqv[col] for row in ct_mx for col in row])
  return cipher_text

# !for a multiplicative inverse to exist, the terms a and b must be co-prime... and in range 2-26 here
def extended_euclidean_algorithm(b, a = 26):
  exe_table = {'x': [1, 0], 'y': [0, 1], 'r': [a, b], 'q': [-1]} 
  # print(exe_table)        
  while exe_table['r'][-1] != 1:                                         
    exe_table['q'].append(math.floor(exe_table['r'][-2] / exe_table['r'][-1]))  
    exe_table['x'].append(exe_table['x'][-2] - exe_table['x'][-1] * exe_table['q'][-1])    
    exe_table['y'].append(exe_table['y'][-2] - exe_table['y'][-1] * exe_table['q'][-1])
    exe_table['r'].append(exe_table['r'][-2] % exe_table['r'][-1])
    # print(exe_table, end="\n\n")
  return (exe_table['y'][-1]) % a         # taking care of additive inverse if applicable

def find_key_adj_mx(key_mx):
  indices = [(i, j) for i in range(3) for j in range(3)]
  cofactor_key_mx = [[0 for i in range(len(key_mx))] for j in range(len(key_mx))]
  for i in range(len(cofactor_key_mx)):
    for j in range(len(cofactor_key_mx)):
      # print(i, j, key_mx[i][j], end = "  ")
      minor_mx = dynamic_list_slicer([key_mx[inx[0]][inx[1]] for inx in indices if inx[0] != i and inx[1] != j], 2)     # follows the exact logic in finding minor matrix manually
      # print(minor_mx)
      cofactor_key_mx[i][j] = ((-1) ** (i + j)) * round(np.linalg.det(minor_mx))
  adj_key_mx = (np.transpose(np.array(cofactor_key_mx)) % 26).tolist()
  return adj_key_mx

def hill_cipher_decryption(cipher_text, key):
  decimal_char_eqv = {i - 65: chr(i) for i in range(65, 91)}
  plain_text = ""
  ct_matrices, key_mx = return_reqd_matrices(cipher_text, key)
  print("Key matrix: ", key_mx)
  print("Cipher Text Matrices: ", ct_matrices)

  #! Finding key_inv_mx (base 26)
  #~ Finding Determinant of key matrix, cannot have a singular matrix i.e det = 0 cause those are not invertible
  det_key_mx = round(np.linalg.det(np.array(key_mx))) % 26
  print("Determinant of Key Matrix: ", det_key_mx)
  #~ Modulo multiplicative inverse of the det (base 26)
  inverted_det = extended_euclidean_algorithm(det_key_mx)
  print("Inverted Key Matrix Determinant: ", inverted_det)
  
  #~ getting the adjoint matrix
  adj_key_mx = find_key_adj_mx(key_mx)
  print("Adjoint Key Matrix: ", adj_key_mx)
  
  #~ getting the inverse key matrix by inv_key_mx = adj_key_mx / det(key_mx)
  inv_key_mx = ((np.array(adj_key_mx) * inverted_det) % 26).tolist()
  print("Inverse Key Matrix: ", inv_key_mx)

  decrypted_matrices = []
  for ct_mx in ct_matrices:
    decrypted_matrices.append((np.dot(inv_key_mx, ct_mx) % 26).tolist())
  
  for dct_mx in decrypted_matrices:
    plain_text += "".join([decimal_char_eqv[col] for row in dct_mx for col in row])
  
  return plain_text

def suggest_valid_keys(key_mx: list):
  decimal_char_eqv = {i - 65: chr(i) for i in range(65, 91)} 
  for row_i in range(len(key_mx)):
    for col_i in range(len(key_mx)):
      og_value = key_mx[row_i][col_i]
      for i in range(26):
        key_mx[row_i][col_i] = (key_mx[row_i][col_i] + i) % 26
        # print(*key_mx)
        if math.gcd(round(np.linalg.det(key_mx)) % 26, 26) == 1:
          # print(round(np.linalg.det(key_mx)) % 26, "".join([decimal_char_eqv[j] for i in key_mx for j in i]))
          print("".join([decimal_char_eqv[j] for i in key_mx for j in i]))
      key_mx[row_i][col_i] = og_value

# passing plain_text just so I can call the return_reqd_matrices function
def validate_key(plain_text, key):
  key_mx = return_reqd_matrices(plain_text, key, False)
  det_key_mx = round(np.linalg.det(np.array(key_mx))) % 26
  # print(det_key_mx)
  if det_key_mx == 0 or math.gcd(26, det_key_mx) != 1:
    while det_key_mx == 0 or math.gcd(26, det_key_mx) != 1:
      suggest_valid_keys(key_mx)
      key = input("Key was invalid, please use one of the suggested keys based on your key(if no suggestions, try another random key): ")[:9].upper().replace(" ", "")
      key_mx = return_reqd_matrices(plain_text, key, False)
      det_key_mx = round(np.linalg.det(np.array(key_mx))) % 26
  
  return key

def hill_cipher():
  plain_text = input("Enter the plain text (uppercase English Alphabets only): ").upper().replace(" ", "")
  while len(plain_text) % 9 != 0:
    plain_text += 'X'
  key = input("Enter the 9-letter key: ")[:9].upper().replace(" ", "")
  while len(key) != 9:
    key += 'X'
  
  key = validate_key(plain_text, key)
  
  cipher_text = hill_cipher_encryption(plain_text, key)
  print("\033[38;2;240;10;10mCipher Text: ", cipher_text, "\033[0m")
  plain_text = hill_cipher_decryption(cipher_text, key)
  print("\033[38;2;10;240;10mDeciphered Text: ", plain_text, "\033[0m")

hill_cipher()