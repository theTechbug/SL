def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift_amount) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift_amount) % 26) + ord('A'))
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    return decrypted_text

encrypted_text = "Khoor Zruog!"
shift = 3
decrypted_text = decrypt(encrypted_text, shift)
print("Encrypted text: " + encrypted_text)
print("Decrypted text: " + decrypted_text)
