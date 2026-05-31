def is_isogram(string):
    count = 0
    string = string.replace(" ", "")
    string = string.replace("-", "")
    for s1 in range(len(string)):
        for s2 in range(len(string)):
            if string[s1].lower() == string[s2].lower():
                count += 1
    if count == len(string):
        return True
    return False
                