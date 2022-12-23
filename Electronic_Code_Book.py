
#~ Implementing Electronic Code Book Encryption Method

def dec_to_binary(dec_num):
  def mechanism(num):
    if num >= 1:
      mechanism(num // 2)
      bin_list.append(num % 2)
  
  bin_list = []
  mechanism(dec_num)
  return bin_list

def ascii_list_binarizer(ascii_list):
  binary_list = []
  for num in ascii_list:
    pad_to_8 = dec_to_binary(num)           # dec to bin only returns significant bits, have to pad for uniform 8 bit representation, 8 bits can represent till 255(included) and that's okay for 1 left shift of any keyboard char ~(126) x 2 = 252 < 255
    while(len(pad_to_8) != 8):
      pad_to_8.insert(0, 0)
    binary_list.extend(pad_to_8)
  return binary_list

def XOR(list_a, list_b):
  for i, (x, y) in enumerate(zip(list_a, list_b)):
    list_a[i] = x ^ y
  
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
  print(ascii_list)
  return ascii_list

def electronic_code_book_encryption():
  cipher_text = "Dolore commodo nulla fugiat proident.Id sit dolore proident aliquip laboris aliqua fugiat ullamco cupidatat duis eiusmod occaecat nostrud cupidatat."[:80]
  # first makes list of 16 chars. from substrings(len = 16) from the whole text and then maps each character to be ascii
  pt_ascii_blocks = [list(map(lambda x: ord(x), list(cipher_text[i - 16: i]))) for i in range(16, len(cipher_text) + 1, 16)]      
  # to make 16 ascii vals to 128 binary digits (for each block)
  pt_128_blocks = []
  for block in pt_ascii_blocks:
    pt_128_blocks.append(ascii_list_binarizer(block))

  #circular left shift each block
  for i in range(len(pt_128_blocks)):
    pt_128_blocks[i].append(pt_128_blocks[i].pop(0))
  
  # key = input("Enter the 16 character key: ")
  key = "aaaaaaaaaaaaaaaa"
  key_ascii = list(map(lambda x: ord(x), list(key)))
  key_128 = ascii_list_binarizer(key_ascii)
  # XOR with key's 128 bits
  for block in pt_128_blocks:
    XOR(block, key_128)
  cipher_text = ""
  for block in pt_128_blocks:
    cipher_text += "".join(list(map(lambda x: chr(x), bin_list_asciirizer(block))))
  print("Cipher Text: ",cipher_text, len(cipher_text))
electronic_code_book_encryption()