def vigenere_decrypt(encrypted_text, key):
    encrypted_text = encrypted_text.upper()
    key = key.upper()
    decrypted_text = ""
    key_length = len(key)

    for i in range(len(encrypted_text)):
        char = encrypted_text[i]

        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char) - ord('A')
            decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
        else:
            decrypted_char = char

        decrypted_text += decrypted_char

    return decrypted_text

# Example usage for decryption
encrypted_text = "RIJVS GSPVH"
key = "KEY"
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Encrypted text: " + encrypted_text)
print("Decrypted text: " + decrypted_text)
