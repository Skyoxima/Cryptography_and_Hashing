
#~ Implementing a simplified version of Data Encryption Standard (DES) (64 bits (8 chars.) input)

from copy import deepcopy
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
    bin_num = dec_to_binary(num)
    while len(bin_num) != 8:        # regulation -> compulsorily 8 bits to represent every number
      bin_num.insert(0, 0)
    binary_list.extend(bin_num)
  return binary_list

def dynamic_list_pooler(list_, pool_size):
  pooled_list = []
  for i in range(pool_size, len(list_) + 1, pool_size):
    pooled_list.append(list_[i-pool_size: i])
  return pooled_list

def bin_to_decimal(eight_bits):
  dec_number = 0
  for i in range(len(eight_bits) - 1, -1, -1):
    if eight_bits[i] == 1:
      dec_number += 2 ** (len(eight_bits) - 1 - i)
  return dec_number

def bin_list_asciirizer(bin_list, poolrange = 8):
  ascii_list = []
  for block_inx in range(poolrange, len(bin_list) + 1, poolrange):
    ascii_list.append(bin_to_decimal(bin_list[block_inx-poolrange: block_inx]))
  return ascii_list

def expansion_permutation(RPT):
  RPT_8_4 = dynamic_list_pooler(RPT, 4)
  RPT_8_6 = []
  for i in range(len(RPT_8_4)):
    RPT_8_6.append(deepcopy(RPT_8_4[i]))
    RPT_8_6[-1].insert(0, RPT_8_4[(i - 1) % 8][-1])
    RPT_8_6[-1].append(RPT_8_4[(i + 1) % 8][0])
  
  # flattening
  RPT_48 = []
  [(RPT_48.extend(i)) for i in RPT_8_6]
  return RPT_48

def s_box_substitution(RPT_48, s_box):
  RPT_8_6 = dynamic_list_pooler(RPT_48, 6)
  RPT_8_4 = []
  for block in RPT_8_6:
    RPT_8_4.append(dec_to_binary(s_box[bin_to_decimal([block[0], block[-1]])][bin_to_decimal(block[1:5])]))
    while len(RPT_8_4[-1]) != 4:    # regulation -> since there is gonna be numbers from 0 - 15 in any of the s_box cell, 4 bits compulsion enforced on binary repr. of these numbers to make 4 x 8 = 32 bits
      RPT_8_4[-1].insert(0, 0)
  
  RPT_32 = []
  [RPT_32.extend(i) for i in RPT_8_4]
  return RPT_32

def function_block(RPT_32, key_48, s_box):
  #~ Expanded RPT which is a list(8 members) of lists(6 members) which total upto 48 bits (This will be the naming convention throughout the program for 2D lists)
  RPT_48 = expansion_permutation(RPT_32)
  
  #~ XOR with the key's 48 bits
  for i in range(len(RPT_48)):
    RPT_48[i] = RPT_48[i] ^ key_48[i]

  #~ Reducing the 48 RPT bits to 32
  RPT_32 = s_box_substitution(RPT_48, s_box)  
  return RPT_32

def simplified_DES_encryption(pt_64, keys_48, s_box, noofrounds = 2):
  cipher_text = ""
  curr_round = 1
  LPT, RPT = pt_64[:32], pt_64[32:]
  while curr_round <= noofrounds:
    # do the crisscross
    pRPT = function_block(RPT, keys_48[curr_round - 1], s_box[curr_round - 1])
    xRPT = [x ^ y for x, y in zip(LPT, pRPT)]
    LPT = RPT
    RPT = xRPT
    curr_round += 1
  # now do the final "straight" output
  ct_64 = RPT + LPT
  cipher_text = "".join(list(map(lambda x: chr(x), bin_list_asciirizer(ct_64))))
  return cipher_text, ct_64

def simplified_DES():
  s_box_1 = [[14,	4, 13, 1,	2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7], 
  [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8], 
  [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0], 
  [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

  s_box_2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
  [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
  [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
  [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

  plain_text = input("Enter the 8 character text: ")[:8]
  pt_64 = ascii_list_binarizer(list(map(lambda x: ord(x), list(plain_text))))
  key_1 = input("Enter the first key: ")[:6]
  key_1_48 = ascii_list_binarizer(list(map(lambda x: ord(x), list(key_1))))
  key_2 = input("Enter the second key: ")[:6]
  key_2_48 = ascii_list_binarizer(list(map(lambda x: ord(x), list(key_2))))

  cipher_text, ct_64 = simplified_DES_encryption(pt_64, keys_48 = (key_1_48, key_2_48), s_box = (s_box_1, s_box_2))
  print("\033[38;5;197mCipher Text:", cipher_text, "\033[0m")
  plain_text, pt_64 = simplified_DES_encryption(ct_64, keys_48 = (key_2_48, key_1_48), s_box = (s_box_2, s_box_1))
  print("\033[38;5;197mDeciphered Text:", plain_text, "\033[0m")

simplified_DES()