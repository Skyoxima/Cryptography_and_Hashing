
#~ Implementing Vigenere Cipher for uppercase English alphabets

cap_αß_dict = {i:f'{chr(i + 65)}' for i in range(26)}         # used to form the table below

#* vigenere_table is a list of 26 lists, with each list having 26 chars. starting one step ahead successively
vigenere_table = [[cap_αß_dict[(i + j) % 26] for j in range(26)] for i in range(26)]
"""
  How the table is formed (in one line using the dictionary)
  1. From the dictionary cap_αß_dict which has pairs as {0: 'A', 1: 'B',..., 25: 'Z'}, we pick out the characters by using the keys.
  2. We need to form 26 lists, with each list starting from the next char. in the alphabet. 
  3. Adding 'i' does that, For e.g, for i = 4 (i.e the 5th list), j goes 0 to 25 (as defined) but (j + i) will go 4 to 29, i.e E -> Z of the cap_αß_dict, and then A -> D since % 26  
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