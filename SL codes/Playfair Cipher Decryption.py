def generate_playfair_matrix(key):
    key = key.replace("J", "I")  # Replace 'J' with 'I'
    key = "".join(dict.fromkeys(key))  # Remove duplicate characters
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_matrix = [[''] * 5 for _ in range(5)]
    key = key + alphabet
    key = key[:25]

    row, col = 0, 0

    for char in key:
        key_matrix[row][col] = char
        col += 1
        if col == 5:
            col = 0
            row += 1

    return key_matrix

def find_char_positions(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return (row, col)
    return None

def playfair_decrypt(encrypted_text, key):
    key_matrix = generate_playfair_matrix(key)
    encrypted_text = encrypted_text.replace(" ", "")  # Remove spaces
    encrypted_text = encrypted_text.upper()

    decrypted_text = ""
    i = 0

    while i < len(encrypted_text):
        char1 = encrypted_text[i]
        char2 = None

        if i + 1 < len(encrypted_text):
            char2 = encrypted_text[i + 1]

        if char2 is None or char1 == char2:
            char2 = 'X'
            i -= 1

        pos1 = find_char_positions(key_matrix, char1)
        pos2 = find_char_positions(key_matrix, char2)

        if pos1 is not None and pos2 is not None:
            (row1, col1) = pos1
            (row2, col2) = pos2

            if row1 == row2:  # Same row
                decrypted_text += key_matrix[row1][(col1 - 1) % 5]
                decrypted_text += key_matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:  # Same column
                decrypted_text += key_matrix[(row1 - 1) % 5][col1]
                decrypted_text += key_matrix[(row2 - 1) % 5][col2]
            else:  # Form a rectangle
                decrypted_text += key_matrix[row1][col2]
                decrypted_text += key_matrix[row2][col1]

        i += 2

    return decrypted_text

# Example usage for decryption
key = "KEYWORD"
encrypted_text = "DAUVPFDEAQ"
decrypted_text = playfair_decrypt(encrypted_text, key)
print("Encrypted text: " + encrypted_text)
print("Decrypted text: " + decrypted_text)