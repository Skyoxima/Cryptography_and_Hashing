vigenere_table = [chr(j + ord('A')) for j in range(0, 26)]
def vigenere_cipher():
  plain_text = input("Enter the plain text: ")
  keyword = input("Enter the keyword: ")[:len(plain_text)]  # precaution if the len(keyword) entered is > len(plain_text)
  while len(keyword) < len(plain_text):
    keyword += keyword
  keyword = keyword[:len(plain_text)]

  

vigenere_cipher()