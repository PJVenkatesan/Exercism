def translate(text):
    new_text = ""
    for words in text.split():
        vowels = ["a", "e", "i", "o", "u"]
        if words[0] in vowels or words[0:2] in ("xr", "yt"):
            words += "ay"
        elif "qu" in words and all(vowel not in words[0:words.find("qu")] for vowel in vowels):
            qu = words.find("qu")
            qu_part = words[0:qu+2]
            words = words[qu+2:len(words)]
            words += qu_part
            words += "ay"
        elif words[0] != "y" and all(vowel not in words[0:words.find("y")] for vowel in vowels):
            y_part = words[0:words.find("y")]
            words = words[words.find("y"):len(words)]
            words += y_part
            words += "ay"
        elif words[0] not in vowels:
            first_v = 0
            for index, letter in enumerate(words):
                if letter in vowels:
                    first_v = index
                    break
            consonant_part = words[0:first_v]
            words = words[first_v:len(words)]
            words += consonant_part
            words += "ay"
        new_text += (words + " ")
    return new_text[0:-1]
