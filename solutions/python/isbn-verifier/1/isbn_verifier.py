def is_valid(isbn):
    val = 0
    is_10 = False
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False
    if isbn[-1] == "X":
        is_10 = True
    for num in range(10,0,-1):
        try:
            val += num * int(isbn[10-num])
        except ValueError:
            if is_10:
                val += 10
            else:
                return False
    return not val % 11
        