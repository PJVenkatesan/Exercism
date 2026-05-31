def rotate(text, key):
    new_text = ""
    for letter in text:
        val = 0
        if letter.isalpha():
            if letter.islower() and ord(letter)+key > 122:
                val = key-(122-ord(letter))
                letter = chr(97+val-1)
            elif letter.isupper() and ord(letter)+key > 90:
                val = key-(90-ord(letter))
                letter = chr(65+val-1)
            else:
                letter  = chr(ord(letter)+key)
        new_text += letter
    return new_text
