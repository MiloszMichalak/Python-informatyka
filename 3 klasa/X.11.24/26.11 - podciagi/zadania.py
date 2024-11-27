# Zadanie 1
from ipaddress import summarize_address_range
from itertools import count
from turtledemo.chaos import coosys

print("Zadanie 1")

file = open("liczby.txt")
ciag = list(map(int, file.readline().split()))
itemsNumber = len(ciag)
    
# sposobu mojego nie ma
    
#sposob prosty
n = len(ciag)
def prostySposob(n):
    for len in range(1, n + 1):
        for start in range(n - len + 1):
            print(*ciag[start:start + len])
            
            
prostySposob(len(ciag))

file.close()


# Zadanie 2
print("Zadanie 2")
file = open("liczby.txt")
ciag = list(map(int, file.readline().split()))
itemsNumber = len(ciag)
        
def sposobProsty(ciag):
    for i in range(itemsNumber):
        for j in range(i, itemsNumber):
            print(*ciag[i:j + 1])
        
        
sposobProsty(ciag)
        
file.close()

# Zadanie 3
print("Zadanie 3")
file = open("liczby.txt")
ciag = list(map(int, file.readline().split()))


for i in range(len(ciag) - 4):
    podciag = ciag[i:i + 5]
    suma = sum(podciag)
    print(podciag, suma)
    
file.close()

# Zadanie 4
print("Zadanie 4")
file = open("liczby.txt")
ciag = list(map(int, file.readline().split()))

# todo


