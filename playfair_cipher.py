
#~ Implementing playfair cipher for uppercase English alphabets
def process_pt(text: str):
  chr_inx = 0
  while chr_inx < len(text):
    if chr_inx != len(text) - 1:
      if text[chr_inx + 1] == text[chr_inx]:
        text = text[:chr_inx + 1] + 'X' + text[chr_inx + 1:]
    chr_inx += 1
  
  if len(text) % 2 != 0:
    text += 'X' if text[-1] != 'X' else 'Y'
  return text

def unique_chars(text: str):
  unique = []
  for c in text:
    if c not in unique:
      unique.append(c)
  return unique

def playfair_encryption(plain_text: str, key: str):
  plain_text = process_pt(plain_text)
  key_unique_chars = unique_chars(key)
  enc_mx = [0 for ]  
def playfair():
  plain_text = input("Enter the message: ").upper().replace(" ", "")
  key = input("Enter the key (preferably len(key) < len(plain_text): ")[:len(plain_text)].upper().replace(" ", "")
  playfair_encryption(plain_text, key)

playfair()