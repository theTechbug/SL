def vigenere_encrypt(plain_text, key):
    plain_text = plain_text.upper()
    key = key.upper()
    encrypted_text = ""
    key_length = len(key)

    for i in range(len(plain_text)):
        char = plain_text[i]

        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char) - ord('A')
            encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted_char = char

        encrypted_text += encrypted_char

    return encrypted_text

# Example usage
plain_text = "HELLO WORLD"
key = "KEY"
encrypted_text = vigenere_encrypt(plain_text, key)
print("Plain text: " + plain_text)
print("Encrypted text: " + encrypted_text)
