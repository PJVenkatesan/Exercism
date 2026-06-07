"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def is_sublist(sub, dom):
    for slice in range(len(dom)+1-len(sub)):
        if dom[slice:slice+len(sub)] == sub:
            return True
        continue
    return False

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if not list_one and list_two:
        return SUBLIST
    if not list_two and list_one:
        return SUPERLIST
    if len(list_one) > len(list_two) and is_sublist(list_two,list_one):
        return SUPERLIST
    if len(list_one) < len(list_two) and is_sublist(list_one,list_two):
        return SUBLIST
    return UNEQUAL
