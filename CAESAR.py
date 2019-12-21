def func():
  startup = input("Encode or decode with key or decode without key? (ed/dwok)\n> ").lower()
  if startup == "dwok":
    caesar_cipher_hiddenkey_decode()
  elif startup == "ed":
    caesar_cipher()
  else:
    print("It looks like you didn't input ed or dwok. Try again please.")
    func()

def isInt_(x):
  try:
    int(x)
    return True
  except ValueError:
    return False

def caesar_cipher():
  text = input("\nInput your message.\n> ")
  key = int(input("\nInput your integer key.\n> "))
  mode = input("\nEncode or decode?\n> ")
  alphabet = "abcdefghijlmnopqrstuvwxyz"
  newText = ""
  if mode == "decode":
    key = -key
    print("\nDecoding...\n")
  else:
    print("\nEncoding...\n")

  for char in range(len(text)):
    if text[char].isupper():
      alphabet = alphabet.upper()
    elif text[char].islower():
      alphabet = alphabet.lower()
    if text[char].isalpha() == False:
      if isInt_(text[char]):
        newLetter = str((int(text[char]) + key)%10)
      else:
        newLetter = text[char]
    else:
      newLetter = alphabet[((alphabet.index(text[char])+key)%25)]
    newText += newLetter
  print("Result:", newText)

def caesar_cipher_hiddenkey_decode():
  text = input("\nInput your message to decode.\n> ")
  alphabet = "abcdefghijlmnopqrstuvwxyz"
  key = 1
  not_done = ""
  while not_done == "":
    newText = ""
    print("\nDecoding...\n")
    for char in range(len(text)):
      if text[char].isupper():
        alphabet = alphabet.upper()
      elif text[char].islower():
        alphabet = alphabet.lower()
      if text[char].isalpha() == False:
        if isInt_(text[char]):
          newLetter = str((int(text[char]) - key)%10)
        else:
          newLetter = text[char]
      else:
        newLetter = alphabet[((alphabet.index(text[char])-key)%25)]
      newText += newLetter
    key += 1
    print("Result: " + newText)
    not_done = input("\nInput something if done.\n> ")
  print("\nDone!\n\nThe final result is: " + newText)



func()