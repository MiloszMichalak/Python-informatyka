# Zadanie 1
from traceback import print_tb
from turtledemo.penrose import start

print("Zadanie 1")

file = open("liczby.txt")
# ciag = list(map(int, file.readline().split()))
ciag = [3, 2, 5, 1]

itemsNumber = len(ciag)
#moj sposob
def sposobTrudny(itemsNumber, n = 1, start = 0):
    for i in range(itemsNumber):
        for j in range(itemsNumber):
            if start + n <= itemsNumber:
                print(ciag[start:start + n])
            start += 1
    n += 1
    start = 0
    
    
#sposob prosty
n = len(ciag)
def prostySposob(n):
    for len in range(1, n+1):
        for start in range(n-len+1):
            print(*ciag[start:start+len])
            
sposobTrudny(len(ciag))
prostySposob(len(ciag))