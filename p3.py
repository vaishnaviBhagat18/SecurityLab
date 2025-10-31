# Diffie-Hellman Key Exchange Algorithm

# Step 1: Get public values from user
n = int(input("Enter a prime number (n): "))
g = int(input("Enter a primitive root modulo n (g): "))

# Step 2: Get private keys from Alice and Bob
x = int(input("Alice, enter your private key (x): "))
y = int(input("Bob, enter your private key (y): "))

# Step 3: Calculate public keys
A = pow(g, x, n)  # (g^x) % n
B = pow(g, y, n)  # (g^y) % n

print(f"\nAlice's Public Key (A) = {A}")
print(f"Bob's Public Key (B) = {B}")

# Step 4: Exchange public keys and compute shared secret
k1 = pow(B, x, n)  # (B^x) % n
k2 = pow(A, y, n)  # (A^y) % n

print(f"\nAlice's computed shared secret = {k1}")
print(f"Bob's computed shared secret = {k2}")

# Step 5: Verify
if k1 == k2:
    print(f"\nKey exchange successful! Shared secret = {k1}")
else:
    print("\nKey exchange failed!")
