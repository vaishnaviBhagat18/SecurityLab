# Expl_A: Implement Python program to illustrate Caesar Cipher Technique

def encrypt(text, s):
    result = ""
    # Traverse text
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():  # Added elif to explicitly check for lowercase
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            # If it's not an alphabet, keep it as is (spaces, numbers, symbols)
            result += char
    return result


# Check the function
text = input("Enter text to encrypt: ")
try:
    s = int(input("Enter shift (0-25): "))
    print("Cipher: " + encrypt(text, s))
except ValueError:
    print("Enter a valid integer between 0 to 25")
