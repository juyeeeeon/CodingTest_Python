import sys
input = sys.stdin.readline

N = int(input().rstrip()) #한 개의 정수를 받을 때 map을 쓰면 map object임
score = list(map(int, input().split()))
M = max(score)

print(sum(score)/M*100/N)