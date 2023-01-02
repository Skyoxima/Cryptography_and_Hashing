
#~ Implementing playfair cipher for uppercase English alphabets
def process_pt(text: str):
  ch_inx = 0
  while ch_inx < len(text):
    if ch_inx != len(text) - 1:
      if text[ch_inx + 1] == text[ch_inx]:
        text = text[:ch_inx + 1] + 'X' + text[ch_inx + 1:]
    ch_inx += 1
  
  if len(text) % 2 != 0:
    text += 'X' if text[-1] != 'X' else 'Y'
  return text

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
  # print(enc_mx, len(enc_mx))
  # tried keeping the enc_mx 1D but it's not feasible
  return [enc_mx[i-5: i] for i in range(5, len(enc_mx) + 1, 5)]

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
  plain_text = process_pt(plain_text)
  enc_mx = make_enc_mx(key)
  print(*enc_mx, sep="\n")
  pt_ch_pairs = [plain_text[i - 2: i] for i in range(2, len(plain_text) + 1, 2)]
  for pair in pt_ch_pairs:
    r1, c1 = give_rc_inx(enc_mx, pair[0])
    # print(pair[0], r1, c1)
    r2, c2 = give_rc_inx(enc_mx, pair[1])
    # print(pair[1], r2, c2)
    if r1 == r2:
      cipher_text += enc_mx[r1][(c1 + 1) % 5] + enc_mx[r2][(c2 + 1) % 5]
    elif c1 == c2:
      cipher_text += enc_mx[(r1 + 1) % 5][c1] + enc_mx[(r2 + 1) % 5][c2]
    else:
      # there are two diff. kinds of diagonals ("forward" and "backward") and they will have to be handled differently 
      pass
  return cipher_text

def playfair():
  plain_text = input("Enter the message: ").upper().replace(" ", "")
  key = input("Enter the key (preferably len(key) < len(plain_text): ")[:len(plain_text)].upper().replace(" ", "")
  cipher_text = playfair_encryption(plain_text, key)
  print("Cipher Text:", cipher_text)
playfair()