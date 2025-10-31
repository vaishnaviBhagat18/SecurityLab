# Program: Implement SHA-1 Algorithm using Python

import hashlib

# Function to generate SHA-1 hash
def generate_sha1(message):
    # Create SHA-1 hash object
    sha1_hash = hashlib.sha1()
    # Convert string to bytes and update hash object
    sha1_hash.update(message.encode('utf-8'))
    # Return hexadecimal digest
    return sha1_hash.hexdigest()

# Take input from user
text = input("Enter text to hash using SHA-1: ")
sha1_result = generate_sha1(text)

print("Original Text:", text)
print("SHA-1 Hash:", sha1_result)
