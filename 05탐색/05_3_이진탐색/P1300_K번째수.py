import sys
input = sys.stdin.readline

N = int(input())
k = int(input())

start = 1
end = k
ans = 0

while start <= end:
    pivot = int((start+end)/2)
    cnt = 0

    for i in range(1,N+1):
        cnt += min(int(pivot/i), N)
    
    #pivot은 cnt번째에 해당
    
    if cnt<k:
        start = pivot + 1
    else:
        ans = pivot
        end = pivot - 1

print(ans)

