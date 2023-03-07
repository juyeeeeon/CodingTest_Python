import sys
import math
input = sys.stdin.readline
print = sys.stdout.write

def  isPalindrom(target:int) ->bool:
    target = list(str(target))
    s = 0
    e = len(target)-1

    while s<e:
        if target[s] != target[e]:
            return False
        else:
            s+=1
            e-=1
    
    return True

N = int(input())

#에라토스테네스의 체
arr = [0 for _ in range(10000001)]

for i in range(2, len(arr)):
    arr[i] = i

for i in range(2, int(math.sqrt(len(arr))+1)):
    if arr[i] == 0 : continue

    for j in range(i+i, len(arr), i):
        arr[j] = 0
####################

for i in range(N, len(arr)):
    if arr[i] != 0:
        result = arr[i]
        if isPalindrom(result):
            print(str(result))
            break
