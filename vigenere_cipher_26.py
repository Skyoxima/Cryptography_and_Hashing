
#~ Implementing Vigenere Cipher for uppercase English alphabets
# https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-Base.html

#* vigenere_table is a list of 26 lists, with each list having 26 chars. starting one step ahead successively
vigenere_table = [[chr((i + j - 65) % 26 + 65) for j in range(26)] for i in range(65, 91)]
"""
Table formation:
As Vigenere table is 26 caesar ciphers essentially, I used that logic to form the table (now, lol) row by row
1. i goes from 65 - 90 i.e the ASCII values for A - Z. 
2. For each i, j goes 0 - 25, so, 
3. (i + j) goes 65 - 90 for i = 65 j = [0, 25]; 66 - 91 for i = 66 and j = [0, 25], and so on
4. For e.g, when (i + j) = 91, (i + j - 65) = 26, (i + j - 65) % 26 = 0 and 0 + 65 would be 65 which is ASCII for A, hence implementing caesar cycle properly (same logic as done in the standalone caesar cipher but with 26 chars. instead of 95)
"""

# print(*vigenere_table, sep="\n")
# alternatively, i think dictionary of dictionaries could've also been used

def vigenere_encryption(plain_text, keyword):
  cipher_text = ""
  for i in range(len(plain_text)):                                                     # range used so that 'i' can be commonly used for both keyword and pt
    cipher_text += vigenere_table[ord(keyword[i]) - 65][ord(plain_text[i]) - 65]       #* The cipher text characters are the characters at the intersection of keyword(X-axis)(rows) and plaintext(Y-axis)(columns), -65 for 65 -> 90 -->> 0 -> 25 for table indices
  return cipher_text

def vigenere_decryption(cipher_text, keyword):
  plain_text = ""
  for i in range(len(cipher_text)):
    plain_text += chr((vigenere_table[ord(keyword[i]) - 65].index(cipher_text[i])) + 65)      #* Plain text is the column index (converted to αß) of the cipher_text char. in the keyword char.'s corresponding row
  return plain_text
  
def vigenere_cipher():
  plain_text = input("Enter the plain text: ").upper()
  keyword = input("Enter the keyword: ")[:len(plain_text)].upper()  # precaution if the len(keyword) entered is > len(plain_text)
  while len(keyword) < len(plain_text):
    keyword += keyword
  keyword = keyword[:len(plain_text)]
  # print(keyword)

  cipher_text = vigenere_encryption(plain_text, keyword)
  print("Encrypted Text: ", cipher_text)
  
  plain_text = vigenere_decryption(cipher_text, keyword)
  print("Decrypted Text: ", plain_text)

vigenere_cipher()