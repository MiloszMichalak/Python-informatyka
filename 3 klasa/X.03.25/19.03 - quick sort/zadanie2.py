print("Zadanie 2")

file = open("liczby.txt", "r")
numbers = list(map(int, file.read().strip().split("\n")))
file.close()

def quick_sort_new_lists(ciag):
    n = len(ciag)
    if n < 2:
        return ciag
    pivot = ciag[n // 2]
    lewy = [x for x in ciag if x < pivot]
    srodkowy = [x for x in ciag if x == pivot]
    prawy = [x for x in ciag if x > pivot]
    return quick_sort_new_lists(lewy) + srodkowy + quick_sort_new_lists(prawy)

print(quick_sort_new_lists(numbers))
    
    