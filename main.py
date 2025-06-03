 #Functions with input

#

def calculate_love_score(name1, name2):
    T = 0
    R = 0
    U = 0
    E = 0

    L = 0
    O = 0
    V = 0
    E = 0

    resultName = name1 + name2
    placeholder = ""
    for letter in resultName.upper():
        if letter == "T":
            T += 1
        elif letter == "R":
            R += 1
        elif letter == "U":
            U += 1
        elif letter == "E":
            E += 1
        elif letter == "L":
            L += 1
        elif letter == "O":
            O += 1
        elif letter == "V":
            V += 1
        elif letter == "E":
            E += 1
        else:
            placeholder += "_"

        totalResult = T + R +U +E + L+ O + V+ E

    print(f"The results as below T = {T} R = {R} U = {U} E = {E} L = {L} O = {O} V = {V} E = {E} ")
    print(f"Total love score = {totalResult}")


firstName = input("Enter first person name: "
)
calculate_love_score(name1="Adenis Ahmeti", name2="Dua Lipa")