user2 = ""

used = []

grid = [
        ["1", "2", "3"],
        ["4", "5", "6"], 
        ["7", "8", "9"]
     ]

def ttt_help(stuff):
    row = 2 if stuff > 6 else 1 if stuff > 3 else 0
    col = 2 if stuff % 3 == 0 else 1 if stuff % 3 == 2 else 0
    return row, col

def al_used(user):
    while user in used:
        user = int(input("That's already taken, try another one: "))
    return user

def detw():
    count = 0
    for items in grid:
        if all(stuff == "X" for stuff in items):
            print("X wins")
            return True
        if all(stuff == "O" for stuff in items):
            print("O wins")
            return True
    for nums in range(3):
        if all(row[nums] == "X" for row in grid):
            print("X wins")
            return True
        if all(row[nums] == "O" for row in grid):
            print("O wins")
            return True
    if all(grid[nums][nums] == "X" for nums in range(3)) or all(grid[nums][len(grid[nums])-nums-1] == "X" for nums in range(3)):
        print("X wins")
        return True
    if all(grid[nums][nums] == "O" for nums in range(3)) or all(grid[nums][len(grid[nums])-nums-1] == "O" for nums in range(3)):
        print("O wins")
        return True
    for rows in grid:
        for cells in rows:
            try:
                cells = int(cells)
            except ValueError:
                count += 1
    if count > 8:
        print("Draw")
        return True
    return False
    

print(*grid, sep="\n")
while True:
    try:
        user1 = int(input("Your X, 1-9?: "))
        if user1 in used:
            user1 = al_used(user1)
        used.append(user1)
    except ValueError:
        print("Please insert num from 1-9")
        continue
    if 0 < user1 < 10:
        row, col = ttt_help(user1)
        grid[row][col] = "X"
        print(*grid, sep="\n")
        if detw():
            break
    while type(user2) != int:
        try:
            user2 = int(input("Your O, 1-9?: "))
            if user2 in used:
                user2 = al_used(user2)
            used.append(user2)
        except ValueError:
            print("Please insert num from 1-9")
    if 0 < user2 < 10:
        row, col = ttt_help(user2)
        grid[row][col] = "O"
        print(*grid, sep="\n")
        user2 = ""
    if detw():
        break