def Flames(n1, n2):
    namestr = n1 + n2

    for c in namestr:
        if namestr.count(c) != 1:
            namestr = namestr.replace(c,"")

    print("!!!!....Flames....!!!!")
    print(" F = Friends \nL = Love, \nA = Affection, \nM = Marriage, \nE = Enemy, \nS = Sibling")

    number = len (namestr) %6

    rel = ""

    if number == 1:
        rel += "Friends"
    elif number == 2:
        rel += "Love"
    elif number == 3:
        rel += "Affection"
    elif number == 4:
        rel += "Marriage"
    elif number == 5:
        rel += "Enemy"
    elif number == 6:
        rel += "Sibling"
    else:
        pass

    return rel


n1 = input("Enter the first name: ").upper()
n2 = input("Enter the second name: ").upper()
print(f"Your relationship is: {Flames(n1,n2)}")