def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Uppercase letters
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            # Keep other characters unchanged
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# User input
def main():
    print("Caesar Cipher Encryption/Decryption")
    choice = input("Choose 'e' to encrypt or 'd' to decrypt: ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g., 3): "))

    if choice == 'e':
        encrypted = caesar_encrypt(message, shift)
        print(f"Encrypted message: {encrypted}")
    elif choice == 'd':
        decrypted = caesar_decrypt(message, shift)
        print(f"Decrypted message: {decrypted}")
    else:
        print("Invalid option. Choose 'e' or 'd'.")

if __name__ == "__main__":
    main()
