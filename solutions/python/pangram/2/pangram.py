def is_pangram(sentence):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    """ for stuff in range(len(sentence)):
        for index, stuff1 in enumerate(alphabet):
            if sentence[stuff].lower() == alphabet[index]:
                alphabet.remove(stuff1)
    if not alphabet:
        return True
    return False """
    return all(letters in sentence.lower() for letters in alphabet)
