
#~ An attempt to have a spin of my own on caesar cipher
import copy

def text_padder(text, pad_len, criteria = 0):
  if criteria == 1:             # exact padding
    while len(text) != pad_len:
      text += 'X'     
  else:                         # conditional padding
    while len(text) % pad_len != 0:
      text += 'X'
  return text

def dec_to_binary(dec_num):
  bin_num = []
  def recursive_bin_mechanism(num):
    if num >= 1:
      recursive_bin_mechanism(num // 2)
      bin_num.append(num % 2)

  recursive_bin_mechanism(dec_num)  
  return bin_num

def ascii_list_binarizer(ascii_list):
  all_nums_bin_repr = []
  for num in ascii_list:
    single_num = dec_to_binary(num)
    while len(single_num) != 8:
      single_num.insert(0, 0)
    all_nums_bin_repr.extend(single_num)
  return all_nums_bin_repr

def XOR(list_a, list_b):
  for i, (x, y) in enumerate(zip(list_a, list_b)):
    list_a[i] = x ^ y

def own_cipher_encryption(plain_text: str, key: str):
  ptlen = len(plain_text)
  padded_key = text_padder(copy.deepcopy(key), ptlen, 1)
  #TODO: Apply XOR then check for caesar_cipher's max limit (1024?)

def own_cipher_decryption(cipher_text: str, key: str):
  pass

def own_cipher():
  plain_text = input("Enter the Plain Text: ")
  key = input("Enter the key(preferably len(key) < len(plain_text)): ")[:len(plain_text)]
  print("\033[38;5;87mEntered text:", plain_text,"\033[0m")
  cipher_text = own_cipher_encryption(plain_text, key)
  print("\033[38;5;197mCipher Text:", cipher_text,"\033[0m")
  plain_text = own_cipher_decryption(cipher_text, key)
  print("\033[38;5;159mDeciphered Text:", plain_text,"\033[0m")

own_cipher()