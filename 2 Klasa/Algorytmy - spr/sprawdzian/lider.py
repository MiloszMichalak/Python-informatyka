def Leader(T) -> int | None:
    check = T[0]
    ile = 1
    for i in range(1, len(T)):
        if ile == 0:
            check = T[i]
            ile = 1
        else:
            if T[i] == check:
                ile += 1
            else:
                ile -= 1
    if ile == 0:
        return None
    else:
        iloscCheckow = 0
        for i in range(len(T)):
            if T[i] == check:
                iloscCheckow += 1
    if iloscCheckow > len(T) / 2:
        return check


T1 = [1, 1, 1, 1, 2, 3, 4, 5, 1, 1, 1]
T2 = [1, 2, 2, 3, 3, 3, 3, 2, 3]
print(Leader(T1))
print(Leader(T2))
