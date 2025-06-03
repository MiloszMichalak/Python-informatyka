print("Zadanie 1")

file = open("liczby.txt", "r")
numbers = list(map(int, file.read().strip().split("\n")))

file.close()

def quick_sort(ciag, lewy, prawy):
    i = lewy
    j = prawy
    pivot = ciag[(i + j) // 2]
    while i <= j:
        while ciag[i] < pivot:
            i += 1
        while ciag[j] > pivot:
            j -= 1
        if i <= j:
            ciag[i], ciag[j] = ciag[j], ciag[i]
            i += 1
            j -= 1
    if j > lewy:
        quick_sort(ciag, lewy, j)
    if i < prawy:
        quick_sort(ciag, i, prawy)
    return ciag
        
print(quick_sort(numbers, 0, len(numbers) - 1))
