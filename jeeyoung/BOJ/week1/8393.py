# 백준 8393번 - 합

num = int(input())

def solution(n):
    answer = sum([a for a in range(1, n+1)])
    return answer

print(solution(num))