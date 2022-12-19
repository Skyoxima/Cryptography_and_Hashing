#~ A simple python program to implement caesar cipher encryption and decryption using 95 valid (keyboard type-able) characters

def caesar_encrypt(plain_text: str, key: int):
  cipher_text = ""
  for i in plain_text:
    cipher_text += chr(((ord(i) + key - 32) % 95) + 32)
  return cipher_text

def caesar_decrypt(cipher_text: str, key: int):
  plain_text = ""
  for i in cipher_text:
    plain_text += chr(((ord(i) - key - 32) % 95) + 32)
  return plain_text

def caesar_cipher():
  plain_text = input("Enter the plain text: ")
  key = int(input("Enter the key (shift, preferably 0 < key < 95): "))
  cipher_text = caesar_encrypt(plain_text, key)
  print("Encrypted Text: ", cipher_text)
  plain_text = caesar_decrypt(cipher_text, key)
  print("Decrypted Text: ", plain_text)

caesar_cipher()