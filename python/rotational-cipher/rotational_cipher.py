def rotate(text, key):
    """Encrypts or decrypts a text using Caesar cipher with a given key."""

    # Create a rotation map for lowercase and uppercase letters
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    rotated_lower = lower[key % 26:] + lower[:key % 26]
    rotated_upper = upper[key % 26:] + upper[:key % 26]

    # Build translation tables for each case
    translation_table = str.maketrans(lower + upper, rotated_lower + rotated_upper)

    # Apply translation using the table
    return text.translate(translation_table)
