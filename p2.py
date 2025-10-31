# simple_rsa_sympy.py
from sympy import isprime, gcd, mod_inverse

#key generation
def generate_keys(p: int, q: int, e: int):
    if not (isprime(p) and isprime(q)):
        raise ValueError("Both numbers must be prime.")
    if p == q:
        raise ValueError("p and q should not be the same.")
    
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    if gcd(e, phi_n) != 1:
        raise ValueError(f"e = {e} is not coprime with phi(n) = {phi_n}. Choose a different e.")
    
    d = mod_inverse(e, phi_n)
    
    print("\nComputed values:")
    print(f"n = {n}")
    print(f"phi(n) = {phi_n}")
    print(f"Private key d = {d}")
    
    return (e, d, n)

# encryption function
def encrypt(message, e, n):
    if not (0 <= message < n):
        raise ValueError("Message integer must satisfy 0 <= message < n.")
    return pow(message, e, n)

#decryption function
def decrypt(cipher, d, n):
    return pow(cipher, d, n)


#main
if __name__ == "__main__":
    try:
        # User input for primes and exponent
        p = int(input("Enter a prime number p: "))
        q = int(input("Enter a different prime number q: "))
        e = int(input("Enter public exponent e (coprime with phi(n)): "))

        # Key generation
        e, d, n = generate_keys(p, q, e)

        #message input
        message = int(input("\nEnter integer message to encrypt (0 <= m < n): "))

        #encrypt
        cipher = encrypt(message, e, n)
        print(f"Encrypted message (integer): {cipher}")

        #decrypt
        decrypted = decrypt(cipher, d, n)
        print(f"Decrypted integer: {decrypted}")

    except ValueError as ve:
        print(f"Error: {ve}")
        
