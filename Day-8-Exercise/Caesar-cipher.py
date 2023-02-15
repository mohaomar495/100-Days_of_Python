alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




#here below is a function that decodes and encodes a given word or sentence by using the alphabet list above.
"""
if direction == "encode":
  def encrypt(text, shift):
    encoded_text = ""
    for i in text:
      position = alphabet.index(i)
      new_position = position + shift
      if new_position >= 1 and new_position <= 25:
        encoded_text += alphabet[new_position]
      else:
        encoded_text += alphabet[new_position - 26]
    print("the encoded text is ", end="")
    return encoded_text
  print(encrypt(text, shift))
elif direction == "decode":
  def decrypt(text, shift):
    decoded_text = ""
    for i in text:
      position = alphabet.index(i)
      new_position = position - shift
      if new_position >= 1 and new_position <= 25:
        decoded_text += alphabet[new_position]
      else:
        decoded_text += alphabet[new_position + 26]
    print("the encoded text is ", end="")
    return decoded_text
  print(decrypt(text, shift)) 
"""

"""
#here is a functions that takes a text and shift or key to shift to encode or decode by using ascii values of the alphabets and also using functions like ord and chr.
if direction == "encode":
  def encrypt(text, shift):
    encoded = ""
    for i in text:
      c = int(ord(i)) + shift
      if c >= 97 and c <= 122:
        encoded += chr(c)
      elif c > 122:
        c = int(ord(i)) - 26
        encoded += chr(c + shift)
      else:
        print(f"{i}", end="")
    print("encoded message is ", end="")
    return encoded
  print(encrypt(text, shift))

elif direction == "decode":
  def decrypt(text, shift):
    decoded = ""
    for i in text:
      c = int(ord(i)) - shift
      if c >= 97 and c <= 122:
        decoded += chr(c)
      elif c > 122:
        c = int(ord(i)) + 26
        decoded += chr(c - shift)
      else:
        print(f"{i}", end="")
    print("decoded message is ", end="")
    return decoded
  print(decrypt(text, shift))
"""

def caesar(text, shift, direction):
    cipher_text = ""
    if direction == "decode":
      shift *= -1
    for i in text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = position + shift
            if new_position >= 0 and  new_position <= 25:
                cipher_text += alphabet[new_position]
            else:
                cipher_text += alphabet[(new_position - 26)]
        else:
            cipher_text += i
    print(f"the {direction}d is {cipher_text}")


should_continue = True

while should_continue:
    direction = input("to encrypt type 'encode', to decrypt type 'decode': ").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    
    shift = shift % 26
    caesar(text, shift, direction)
    
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    
    if result == "no":
        should_continue = False
        print("Goodbye")

#function above works well if u try encrypt or decrypt a word.