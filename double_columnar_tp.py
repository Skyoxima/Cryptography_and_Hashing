
#~ Implementing Double Columnar Transposition symmetric cryptography (See columnar_tp.py for explanation)
#!NTS at the end ↓

#TODO - make it work for all types of combos of keys- done
def text_padding(text, keylen):
  while len(text) % keylen != 0:
      text += '_'
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

def columnar_tp_encryption(plain_text, key, other_key):
  cipher_text = ""
  keylen = len(key)
  col_order = key_orderer(key)
  if len(plain_text) % len(key) != 0:           # if padding required then only call the padding function 
    plain_text = text_padding(plain_text, keylen)
  ptlen = len(plain_text)                            # length of plaintext should always be taken after padding
  enc_mx = [list(plain_text[i - keylen: i]) for i in range(keylen, ptlen + 1, keylen)]
  
  for col in col_order:
    cipher_text += "".join([enc_mx[row][col] for row in range(len(enc_mx))])
  return cipher_text, f"{ptlen}"

def columnar_tp_decryption(cipher_text, key):
  plain_text = ""
  keylen = len(key)
  col_order = key_orderer(key)
  ctlen = len(cipher_text)                    
  dec_mx = [[0 for _ in range(keylen)] for _ in range(int(ctlen / keylen))]
  ct_curr_indx = 0
  
  for col in col_order:
    for row in range(len(dec_mx)):
      dec_mx[row][col] = cipher_text[ct_curr_indx]
      ct_curr_indx += 1

  for _ in range(len(dec_mx)):
    plain_text += "".join(dec_mx.pop(0))
  
  return plain_text

def double_columnar_encryption(plain_text: str, key1: str, key2: str):
  intermediate_ct, intermediate_ptlen = columnar_tp_encryption(plain_text, key1, key2)
  final_ct = columnar_tp_encryption(intermediate_ct, key2, key1)[0] + "≥" + intermediate_ptlen
  return final_ct 

def double_columnar_decryption(cipher_text, key1: str, key2: str):
  intermediate_ptlen = int(cipher_text[cipher_text.index("≥") + 1:])
  cipher_text = cipher_text[:cipher_text.index("≥")]
  intermediate_pt = columnar_tp_decryption(cipher_text, key2)
  intermediate_pt = intermediate_pt[:intermediate_ptlen]
  final_pt = columnar_tp_decryption(intermediate_pt, key1)
  return final_pt
  
def double_columnar():
  plain_text = input("Enter the plain text (preferably all caps, no space): ").upper().replace(" ", "")
  key1 = input("Enter the first key (preferably len(key) < len(plain_text)): ")[:len(plain_text)].upper().replace(" ", "")
  key2 = input("Enter the second key (preferably len(key) < len(plain_text)): ")[:len(plain_text)].upper().replace(" ", "")
  print("\033[38;5;149mEntered Text:", plain_text, "\033[0m")

  cipher_text = double_columnar_encryption(plain_text, key1, key2)
  print("\033[38;5;197mCipher Text:", cipher_text, "\033[0m")
  plain_text = double_columnar_decryption(cipher_text, key1, key2)
  print("\n\033[38;5;205mDeciphered Text:", plain_text, "\033[0m")

double_columnar()


#!
#! CTP -> Columnar TransPosition, DCTP -> Double columnar transposition
"""
1. So the issue with this code for DCTP is when particular pairs of keys (w.r.t length) is used the cipher doesn't work.
2. For e.g, when key of length 5 and 6 (order matters) are used and the plain text is 21 chars. long, the 5 key length will have the p.t padded to 25 chars. then do one CTP on it.
Later these 25 chars. will again be padded to 30 chars. to be divisible by 6 i.e the second key length. The 2nd CTP will be done and c.t will be formed with no issue.
But while decryption, 6 chars. key will decipher the 30 chars. correctly BUT so will the 5 chars. which it shouldn't have (5 chars. was used for 25 chars. encryption) and we don't have a clear idea on receiver's end if the intermediate plain_text was 25 chars. or 30 chars.

3. To mitigate this discrepancy, I've taken the approach of appending the intermediate cipher text's length to the final cipher text, and retrieve it at the very first step while decryption...
...Carry on with the first round of decryption to get intermediate plain_text (which should be the same as int_ct but with potentially extra padding) which is then unpadded using the length retrieved earlier.
4. I think this approach doesn't harm the security of this cipher as much while making it more robust (with availability of using two unequal length keys)
"""