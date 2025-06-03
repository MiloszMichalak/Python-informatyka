print("Zadanie 4")

file = open("liczby.txt", "r")
ciag = list(map(int, file.read().strip().split("\n")))
file.close()

def quick_sort_hoare(lewy, prawy):
    n = len(ciag)
    i = (lewy + prawy) // 2
    pivot = ciag[i]
    ciag[i] = ciag[prawy]
    i = j = lewy
    for j in range(lewy, prawy):
        if ciag[i] < pivot:
            ciag[i], ciag[j] = ciag[j], ciag[i]
            j += 1
    ciag[prawy] = ciag[j]
    ciag[j] = pivot
    if lewy < j - 1:
        quick_sort_hoare(lewy, j - 1)
    if j + 1 < prawy:
        quick_sort_hoare(j + 1, prawy)
        
        
quick_sort_hoare(0, len(ciag) - 1)
print(ciag)
    