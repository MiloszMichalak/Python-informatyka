print("Zadanie 3")

file = open("liczby.txt", "r")
numbers = list(map(int, file.read().strip().split("\n")))
file.close()

def quick_sort_new_lists_one_for(ciag):
    n = len(ciag)
    if n < 2:
        return ciag
    pivot = ciag[n // 2]
    lewy = []
    srodkowy = []
    prawy = []
    for x in ciag:
        if x < pivot:
            lewy.append(x)
        elif x == pivot:
            srodkowy.append(x)
        else:
            prawy.append(x)
    return quick_sort_new_lists_one_for(lewy) + srodkowy + quick_sort_new_lists_one_for(prawy)


print(quick_sort_new_lists_one_for(numbers))
