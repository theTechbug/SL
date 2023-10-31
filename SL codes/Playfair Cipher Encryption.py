def generate_playfair_matrix(key):
    key = key.replace("J", "I")  # Replace 'J' with 'I'
    key = "".join(dict.fromkeys(key))  # Remove duplicate characters
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_matrix = [[None] * 5 for _ in range(5)]
    key = key + alphabet
    key = key[:25]

    row = 0
    col = 0

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

def playfair_encrypt(plain_text, key):
    key_matrix = generate_playfair_matrix(key)
    plain_text = plain_text.replace("J", "I")
    plain_text = plain_text.replace(" ", "")  # Remove spaces
    plain_text = plain_text.upper()

    encrypted_text = ""
    i = 0

    while i < len(plain_text):
        char1 = plain_text[i]
        char2 = None

        if i + 1 < len(plain_text):
            char2 = plain_text[i + 1]

        if char2 is None or char1 == char2:
            char2 = 'X'
            i -= 1

        pos1 = find_char_positions(key_matrix, char1)
        pos2 = find_char_positions(key_matrix, char2)

        if pos1 is not None and pos2 is not None:
            (row1, col1) = pos1
            (row2, col2) = pos2

            if row1 == row2:  # Same row
                encrypted_text += key_matrix[row1][(col1 + 1) % 5]
                encrypted_text += key_matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:  # Same column
                encrypted_text += key_matrix[(row1 + 1) % 5][col1]
                encrypted_text += key_matrix[(row2 + 1) % 5][col2]
            else:  # Form a rectangle
                encrypted_text += key_matrix[row1][col2]
                encrypted_text += key_matrix[row2][col1]

        i += 2

    return encrypted_text

# Example usage
key = "KEYWORD"
plain_text = "HELLO WORLD"
encrypted_text = playfair_encrypt(plain_text, key)
print("Plain text: " + plain_text)
print("Encrypted text: " + encrypted_text)
