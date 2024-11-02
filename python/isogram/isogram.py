def is_isogram(string):
    
    # Remove hyphens and spaces, and convert to lowercase
    clean_string = string.replace("-", "").replace(" ", "").lower()

    # Check if the number of unique characters matches the length of the cleaned string
    return len(set(clean_string)) == len(clean_string)

