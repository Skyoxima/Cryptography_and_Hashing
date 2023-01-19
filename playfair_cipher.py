
#~ Implementing playfair cipher for uppercase English alphabets
def process_pt(text: str):
  pairs, idx = [], 2
  while idx <= len(text) + 1:
    pair = text[idx - 2: idx]
    if len(pair) == 1:            # safeguarding from index out of range errors at the last pair
      text += 'X' if text[-1] != 'X' else 'Y'
      continue      
    if pair[0] == pair[1]:
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

  #! This variation of playfair cipher always pairs I and J no matter the occurence in the key (cause on the net I've seen J getting omitted or paired both)
  enc_mx.pop(enc_mx.index('J'))
  enc_mx[enc_mx.index('I')] = 'IJ'
  return [enc_mx[i-5: i] for i in range(5, len(enc_mx) + 1, 5)]     # 2Ded

def give_rc_inx(mx, char):
  if char == 'I' or char == 'J':
    char = 'IJ'
  for row in range(len(mx)):
    for col in range(len(mx[row])):
      if mx[row][col] == char:
        return row, col
  return -1, -1

def playfair_encryption(plain_text: str, key: str):
  cipher_text = ""
  enc_mx = make_enc_mx(key)
  print(*enc_mx, sep="\n")
  pt_ch_pairs = process_pt(plain_text)
  for pair in pt_ch_pairs:
    r1, c1 = give_rc_inx(enc_mx, pair[0])
    r2, c2 = give_rc_inx(enc_mx, pair[1])
    print(f"{pair}: {r1, c1}, {r2, c2}")

    if r1 == r2:
      cipher_text += (enc_mx[r1][(c1 + 1) % 5] + enc_mx[r2][(c2 + 1) % 5]).replace('IJ','I')
    elif c1 == c2:
      cipher_text += (enc_mx[(r1 + 1) % 5][c1] + enc_mx[(r2 + 1) % 5][c2]).replace('IJ', 'I')
    else:
      cipher_text += (enc_mx[r1][c2] + enc_mx[r2][c1]).replace("IJ", "I") 
  return cipher_text

def playfair():
  plain_text = input("Enter the message: ").upper().replace(" ", "")
  key = input("Enter the key (preferably len(key) < len(plain_text): ")[:len(plain_text)].upper().replace(" ", "")
  cipher_text = playfair_encryption(plain_text, key)
  print("Cipher Text:", cipher_text)
playfair()