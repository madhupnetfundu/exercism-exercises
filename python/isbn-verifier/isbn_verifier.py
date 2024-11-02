def is_valid(isbn):
    # Remove hyphens
    isbn = isbn.replace("-", "")
    
    # ISBN-10 should have exactly 10 characters
    if len(isbn) != 10:
        return False
    
    # Check that all characters except possibly the last one are digits
    if not isbn[:-1].isdigit():
        return False
    
    # The last character can be a digit or 'X' (representing 10)
    if not (isbn[-1].isdigit() or isbn[-1] == "X"):
        return False

    # Calculate the checksum with special handling for 'X' in the last position
    total = 0
    for i, char in enumerate(isbn):
        if char == "X" and i == 9:  # 'X' at last position represents 10
            value = 10
        else:
            value = int(char)
        
        # Multiply the value by its weight (10 down to 1)
        total += value * (10 - i)

    # ISBN-10 is valid if the checksum is divisible by 11
    return total % 11 == 0
