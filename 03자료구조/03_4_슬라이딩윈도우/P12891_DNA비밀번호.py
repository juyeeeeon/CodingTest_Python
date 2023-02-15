def delDNA(a:int):
    global arr, count
    if arr[a] == "A":
        count[0]-=1
    elif arr[a] == "C":
        count[1]-=1
    elif arr[a] == "G":
        count[2]-=1
    else:
        count[3]-=1

def addDNA(a:int):
    global arr, count
    if arr[a] == "A":
        count[0]+=1
    elif arr[a] == "C":
        count[1]+=1
    elif arr[a] == "G":
        count[2]+=1
    else:
        count[3]+=1


import sys
input = sys.stdin.readline

S, P = map(int, input().split())
arr = list(map(str, input().rstrip()))
minCnt = list(map(int, input().split()))

startIdx = 0
endIdx = P-1
count = [0]*4

#해당 부분문자열의 DNA count
for i in range(startIdx, endIdx+1):
    addDNA(i)

ans = 0
while endIdx < S:
    findResult = True

    for i in range(4):
        if count[i]<minCnt[i]:
            findResult = False
            break
    
    if findResult:
        ans+=1

    delDNA(startIdx)

    startIdx+=1
    endIdx+=1

    if endIdx >= S:
        break
    
    addDNA(endIdx)
    
print(ans)

