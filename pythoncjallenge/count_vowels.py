# count_vowels.py

def count_vowels(text):
    # Counts the number of vowels (a, e, i, o, u) in the input string, ignoring case
    vowels = 'aeiou'
    text = text.lower()  # Convert the text to lowercase for case-insensitive comparison
    return sum(1 for char in text if char in vowels)
