
#~ An attempt to implement a spin of my own (XOR) on caesar cipher
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

def bin_list_asciirizer(eight_bin_dgts):
  dec_num = 0
  for i in range(len(eight_bin_dgts)):
    if eight_bin_dgts[i] == 1:
      dec_num += 2 ** ((len(eight_bin_dgts) - 1) - i)
  return dec_num

def own_cipher_encryption(plain_text: str, key: str):
  ptlen = len(plain_text)
  padded_key = text_padder(key, ptlen, 1)
  padded_key_bin = ascii_list_binarizer(list(map(lambda x: ord(x), list(padded_key))))

  # list of all plain_text's characters ascii representation, I am using stream cipher approach for now instead of block cipher approach
  pt_bin = ascii_list_binarizer(list(map(lambda x: ord(x), list(plain_text))))
  XOR(pt_bin, padded_key_bin)
  
  pt_ascii = []
  for i in range(8, len(pt_bin) + 1, 8):
    pt_ascii.append(bin_list_asciirizer(pt_bin[i-8: i]))
  
  cipher_text = ""
  for num in pt_ascii:
    cipher_text += chr((num + len(key)) % 1024)
  return cipher_text

def own_cipher_decryption(cipher_text: str, key: str):
  ctlen = len(cipher_text)
  ct_ascii = list(map(lambda x: ord(x), list(cipher_text)))
  padded_key = text_padder(key, ctlen, 1)
  padded_key_bin = ascii_list_binarizer(list(map(lambda x: ord(x), list(padded_key))))

  # First reversing the caesar cipher shift
  for i in range(len(ct_ascii)):
    ct_ascii[i] = (ct_ascii[i] - len(key)) % 1024
  
  # Then reverting the XOR because it had happened first during encryption
  ct_bin = ascii_list_binarizer(ct_ascii)
  XOR(ct_bin, padded_key_bin)

  plain_text = ""
  for i in range(8, len(ct_bin) + 1, 8):
    plain_text += chr(bin_list_asciirizer(ct_bin[i-8: i]))
  return plain_text

def own_cipher():
  plain_text = input("Enter the Plain Text: ")
  key = input("Enter the key(preferably len(key) < len(plain_text)): ")[:len(plain_text)]
  print("\033[38;5;154mEntered text:", plain_text,"\033[0m")
  cipher_text = own_cipher_encryption(plain_text, key)
  print("\033[38;5;197mCipher Text:", cipher_text,"\033[0m")
  plain_text = own_cipher_decryption(cipher_text, key)
  print("\033[38;5;157mDeciphered Text:", plain_text,"\033[0m")

own_cipher()