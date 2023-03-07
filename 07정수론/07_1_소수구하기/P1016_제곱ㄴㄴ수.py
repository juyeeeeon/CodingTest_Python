import sys
import math
input = sys.stdin.readline
#print = sys.stdout.write

min, max = map(int, input().split())

check = [False]*(max-min+1)

for i in range(2, int(math.sqrt(max)+1)):
    pow = i*i
    start_index = int(min/pow)
    if min%pow != 0:
        start_index += 1
    for j in range(start_index, int(max/pow)+1):
        check[int((j*pow)-min)] = True

cnt = 0
for i in range(0, max-min+1):
    if not check[i]:
        cnt+=1

print(cnt)
