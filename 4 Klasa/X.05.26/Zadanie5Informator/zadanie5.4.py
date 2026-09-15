A = [0, 2, 4, 6, 8, 10, 9, 7, 5, 3, 1]

def W(j):
    v = A[j]
    i = j
    while i > 1 and A[i - 1] > v:
        A[i] = A[i - 1]
        i -= 1
    A[i] = v

print(A)
W(7)
print(A)

W(9)
print(A)