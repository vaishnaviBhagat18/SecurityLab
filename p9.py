# Exp9: Implement Python program to illustrate Playfair Cipher technique

# Step 1: Create the 5x5 key matrix
def generate_key_matrix(key):
    key = key.lower().replace('j', 'i')  # Replace 'j' with 'i'
    matrix = []
    used = set()
    
    for char in key:
        if char.isalpha() and char not in used:
            used.add(char)
            matrix.append(char)
    
    # Fill remaining letters (excluding 'j')
    for char in 'abcdefghiklmnopqrstuvwxyz':
        if char not in used:
            used.add(char)
            matrix.append(char)
    
    # Convert list into 5x5 matrix
    return [matrix[i*5:(i+1)*5] for i in range(5)]

# Step 2: Preprocess plaintext into digraphs
def preprocess_text(text):
    text = text.lower().replace('j', 'i').replace(' ', '')
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = 'x'
        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:
                pairs.append((a, 'x'))
                i += 1
            else:
                pairs.append((a, b))
                i += 2
        else:
            pairs.append((a, 'x'))
            i += 1
    return pairs

# Step 3: Find character position in matrix
def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

# Step 4: Encrypt each pair using Playfair rules
def encrypt_pair(pair, matrix):
    a, b = pair
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:
        # Same row → shift right
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        # Same column → shift down
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        # Rectangle rule → swap columns
        return matrix[row1][col2] + matrix[row2][col1]

# Step 5: Full encryption function
def playfair_encrypt(plaintext, key):
    matrix = generate_key_matrix(key)
    print("Key Matrix:")
    for row in matrix:
        print(row)
    
    pairs = preprocess_text(plaintext)
    print("\nDigraphs:", pairs)
    
    ciphertext = ''
    for pair in pairs:
        encrypted = encrypt_pair(pair, matrix)
        print(f"{pair[0]}{pair[1]} → {encrypted}")
        ciphertext += encrypted
    
    return ciphertext.upper()

# Main program
plaintext = input("Enter text to encrypt: ")
key = input("Enter key: ")
ciphertext = playfair_encrypt(plaintext, key)
print("\nCiphertext:", ciphertext)
