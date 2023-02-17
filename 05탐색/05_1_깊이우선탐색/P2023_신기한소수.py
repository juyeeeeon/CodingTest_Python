import sys
input = sys.stdin.readline
print = sys.stdout.write

def isPrime(number:int) -> bool:
    
    for i in range(2, int(number/2+1)):
        if number%i == 0:
            return False
    return True
    
    """
    for i in range(2, number):
        if number%i == 0:
            return False
    
    return True
    """

def DFS(number:int, jarisu:int):
    if jarisu == N:
        if isPrime(number):
            print(str(number)+'\n')
        return
    
    for i in range(1,10):
        if i%2 == 0: continue
        elif isPrime(number*10+i):
            DFS(number*10+i, jarisu+1)

N = int(input())

DFS(2,1)
DFS(3,1)
DFS(5,1)
DFS(7,1)


