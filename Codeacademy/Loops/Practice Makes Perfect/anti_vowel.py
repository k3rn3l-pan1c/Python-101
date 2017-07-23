def anti_vowel(text):
    string = ""
    for c in text:
        if c not in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
            string += c

    return string
