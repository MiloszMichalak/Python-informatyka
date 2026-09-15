A = [0,2,4,6,8,10,9,7,5,3,1]

def W(j):
    if j > 1:
        if A[j] < A[j - 1]:
            A[j], A[j - 1] = A[j - 1], A[j]
            W(j - 1)

print(A)
W(7)
print(A)

W(9)
print(A)