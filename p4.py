# md5_example.py
import hashlib

def generate_md5(message: str) -> str:
    """Generate MD5 hex digest for the provided message string."""
    # Create MD5 hash object
    md5_hash = hashlib.md5()
    # Convert string to bytes and update hash object
    md5_hash.update(message.encode('utf-8'))
    # Return hexadecimal digest
    return md5_hash.hexdigest()

if __name__ == "__main__":
    # Take input from user
    text = input("Enter text to hash using MD5: ").strip()
    md5_result = generate_md5(text)
    print("Original Text:", text)
    print("MD5 Hash:", md5_result)
