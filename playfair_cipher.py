
#~ Implementing playfair cipher for uppercase English alphabets
from itertools import permutations

def process_pt(text: str):
  pairs, idx = [], 2
  while idx <= len(text) + 1:
    pair = text[idx - 2: idx]
    if len(pair) == 1:                          # safeguarding from index out of range errors at the last pair
      text += 'X' if text[-1] != 'X' else 'Y'
      continue      
    if pair[0] == pair[1] or (pair[0] == "I" and pair[1] == "J") or (pair[0] == "J" and pair[1] == "I"):        # Have to especially consider consequent IJ occurences 
      text = text[:idx - 1] + "X" + text[idx - 1:]
      continue
    pairs.append(pair)      
    idx += 2
  return pairs

def unique_chars(text: str):
  unique = []
  for c in text:
    if c not in unique:
      unique.append(c)
  return unique

def make_enc_mx(key: str):
  enc_mx = []
  enc_mx.extend(unique_chars(key))
  for i in range(65, 91):
    if chr(i) not in enc_mx:
      enc_mx.append(chr(i))

  #! This variation of playfair cipher always treats Js as Is
  enc_mx.pop(enc_mx.index('J'))
  return [enc_mx[i - 5: i] for i in range(5, len(enc_mx) + 1, 5)]     # converted to 2D

def give_rc_inx(mx, char):
  char = 'I' if char == 'J' else char
  for row in range(len(mx)):
    for col in range(len(mx[row])):
      if mx[row][col] == char:
        return row, col
  return -1, -1

def playfair_encryption(plain_text: str, key: str):
  cipher_text = ""
  enc_mx = make_enc_mx(key)
  # print(*enc_mx, sep="\n")
  pt_ch_pairs = process_pt(plain_text)
  for pair in pt_ch_pairs:
    r1, c1 = give_rc_inx(enc_mx, pair[0])
    r2, c2 = give_rc_inx(enc_mx, pair[1])
    # print(f"{pair}: {r1, c1}, {r2, c2}")
    if r1 == r2:
      cipher_text += (enc_mx[r1][(c1 + 1) % 5] + enc_mx[r2][(c2 + 1) % 5])
    elif c1 == c2:
      cipher_text += (enc_mx[(r1 + 1) % 5][c1] + enc_mx[(r2 + 1) % 5][c2])
    else:
      cipher_text += (enc_mx[r1][c2] + enc_mx[r2][c1])
  return cipher_text

#! Showing all possible texts to the receiver if the decrypted text contains 'I' (maybe reduces security levels but I feel it enhances receiver's exp)
def all_pt_perms(plain_text: str):
  pt_perms = []
  i_idx_psns = [i for i in range(len(plain_text)) if plain_text[i] == "I"]
  ij_perms = []
  for itr in range(len(i_idx_psns) + 1):    # counts from 0 till all Is i.e no change to all Is as well as all Is changed to J
    ij_perms.extend(list(permutations(i_idx_psns, itr)))
  
  for perm in ij_perms:
    pt_list = list(plain_text)
    for idx in perm:
      pt_list[idx] = 'J'
    pt_perms.append("".join(pt_list))
  return list(set(pt_perms))

def playfair_decryption(cipher_text: str, key: str):
  plain_text = ""
  enc_mx = make_enc_mx(key)
  ct_ch_pairs = process_pt(cipher_text)
  
  for pair in ct_ch_pairs:
    r1, c1 = give_rc_inx(enc_mx, pair[0])
    r2, c2 = give_rc_inx(enc_mx, pair[1])
    if r1 == r2:
      plain_text += (enc_mx[r1][(c1 - 1) % 5] + enc_mx[r2][(c2 - 1) % 5])
    elif c1 == c2:
      plain_text += (enc_mx[(r1 - 1) % 5][c1] + enc_mx[(r2 - 1) % 5][c2])
    else:
      plain_text += (enc_mx[r1][c2] + enc_mx[r2][c1])
  
  pt_perms = all_pt_perms(plain_text)
  return pt_perms

def playfair():
  plain_text = input("Enter the message: ").upper().replace(" ", "")
  key = input("Enter the key (preferably len(key) < len(plain_text): ")[:len(plain_text)].upper().replace(" ", "")
  cipher_text = playfair_encryption(plain_text, key)
  print("Cipher Text:\033[38;5;197m", cipher_text,"\033[0m\n")
  all_pt = playfair_decryption(cipher_text, key)
  for i in range(len(all_pt)):
    print(f"\033[38;2;{255 if i % 2 != 0 else 0};{255 if i % 2 == 0 else 75};{220 if i % 2 == 0 else 130}m{i}: {all_pt[i]}")
  print("\033[0m")
playfair()