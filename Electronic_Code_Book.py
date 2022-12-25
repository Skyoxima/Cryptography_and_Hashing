
#~ Implementing Electronic Code Book Block Cipher Technique

import copy
def text_padder(text):
  while len(text) % 16 != 0:
    text += '_'
  return text

def dec_to_binary(dec_num):
  def mechanism(num):
    if num >= 1:
      mechanism(num // 2)
      bin_list.append(num % 2)
  bin_list = []
  mechanism(dec_num)
  return bin_list

# the -izer suffix just sounds funny to me so used it lol
def ascii_list_binarizer(ascii_list):
  binary_list = []
  for num in ascii_list:
    pad_to_8 = dec_to_binary(num)           # dec to bin only returns significant bits, have to pad for uniform 8 bit representation, 8 bits can represent till 255(included) and that's okay for 1 left shift of any english keyboard char ~(126) x 2 = 252 < 255
    while(len(pad_to_8) != 8):
      pad_to_8.insert(0, 0)
    binary_list.extend(pad_to_8)
  return binary_list

# both list_a and list_b are lists of 128 bits
def list_XOR(list_a, list_b):
  XORed = []
  for x, y in zip(list_a, list_b):
    XORed.append(x ^ y)     # shorthand for XOR in python is ^, don't confuse it with power!
  return XORed

def binary_to_ascii(eight_bits):
  dec_number = 0
  for i in range(len(eight_bits) - 1, -1, -1):
    if eight_bits[i] == 1:
      dec_number += 2 ** (len(eight_bits) - 1 - i)
  return dec_number

def bin_list_asciirizer(bin_list):
  ascii_list = []
  for eight_indx in range(8, len(bin_list) + 1, 8):
    ascii_list.append(binary_to_ascii(bin_list[eight_indx - 8: eight_indx]))
  return ascii_list

def electronic_code_book_encryption(plain_text, key):
  # A list of lists containing 16 ascii values representing 16 chars. splits (blocks) of plain text
  pt_ascii_blocks = [list(map(lambda x: ord(x), list(plain_text[i - 16: i]))) for i in range(16, len(plain_text) + 1, 16)]       
  # list of lists containing 128 binary bits for 16 ascii values (1 ascii value -> 8 bits of binary digits, 16 x 8 = 128 bits)
  pt_128_blocks = []
  for block in pt_ascii_blocks:
    pt_128_blocks.append(ascii_list_binarizer(block))

  # converting the 16 char. key string to 128 bits similarly
  key_128 = ascii_list_binarizer(list(map(lambda x: ord(x), list(key))))

  # circular left shift each block of pt_128 individually (that's what block cipher wants to achieve, separated encryption)
  for block in pt_128_blocks:
    block.append(block.pop(0))  
  
  # XORing each 128 bits block with key's 128 bits
  for b_indx in range(len(pt_128_blocks)):
    pt_128_blocks.append(list_XOR(pt_128_blocks[b_indx], key_128))
  pt_128_blocks = pt_128_blocks[len(pt_128_blocks) // 2:]

  # forming the cipher_text in string format (which will be equal to the length of plain_text) from the blocks of bits
  cipher_text = ""
  for block in pt_128_blocks:
    cipher_text += "".join(list(map(lambda x: chr(x), bin_list_asciirizer(block))))
  return cipher_text

def electronic_code_book_decryption(cipher_text, key):
  # getting the required setup of blocks of 128 bits (same as plain_text)
  key_128 = ascii_list_binarizer(list(map(lambda x: ord(x), list(key))))
  ct_ascii_blocks = [list(map(lambda x: ord(x), list(cipher_text[i - 16: i]))) for i in range(16, len(cipher_text) + 1, 16)]
  ct_128_blocks = []
  for block in ct_ascii_blocks:
    ct_128_blocks.append(ascii_list_binarizer(block))

  # Since XOR was the last thing done when encrypting, it will be the first thing done when decrypting (also XOR because XORing an XOR brings us back to the starting bits)
  for b_indx in range(len(ct_128_blocks)):
    ct_128_blocks.append(list_XOR(ct_128_blocks[b_indx], key_128))
  ct_128_blocks = ct_128_blocks[len(ct_128_blocks) // 2:]
  
  # now the XOR'ed bits are to be circular right shifted, i.e the reverse direction
  for block in ct_128_blocks:
    block.insert(0, block.pop(-1))
  
  plain_text = ""
  for block in ct_128_blocks:
    plain_text += "".join(list(map(lambda x: chr(x), bin_list_asciirizer(block))))
  return plain_text

def electronic_code_book():
  plain_text = "Dolore commodo nulla fugiat proident.Id sit dolore proident aliquip laboris aliqua fugiat ullamco cupidatat duis eiusmod occaecat nostrud cupidatat."
  print("\033[38;5;85mOriginal Plain Text:", plain_text, "\033[0m")
  plain_text = text_padder(plain_text)
  key = input("Enter the 16 character key string: ")[:16]
  cipher_text = electronic_code_book_encryption(plain_text, key)
  print("\033[38;5;197mCipher Text:", cipher_text, "\033[0m", len(cipher_text))
  plain_text = electronic_code_book_decryption(cipher_text, key)
  print("\033[38;5;209mDeciphered Text:", plain_text, "\033[0m", len(plain_text))
  
electronic_code_book()