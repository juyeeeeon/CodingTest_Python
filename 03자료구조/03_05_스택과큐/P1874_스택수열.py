import sys
input = sys.stdin.readline

N = int(input().rstrip())

whatWeWant = []
for i in range(N):
    whatWeWant.append(int(input().rstrip()))

stack = []
idx = 0
now = 1
output = []
resultExist = True
while now<=N:
    while now <= whatWeWant[idx] :
        stack.append(now)
        output.append("+")
        now+=1
    
    while stack and (stack[-1] == whatWeWant[idx]):
        stack.pop()
        output.append("-")
        idx+=1

    if stack and whatWeWant[idx]<stack[-1]: 
        resultExist = False
        print("NO")
        break

if resultExist:
    for i in range(len(output)):
        print(output[i])