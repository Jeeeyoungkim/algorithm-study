# 소수 찾기

x = int(input())
arr = list(map(int, input().split()))

import math

def solution(arr):
    count = 0
    
    for elem in arr:
        if elem == 1:
            continue
        
        is_prime = True
        for num in range(2, int(math.sqrt(elem))+1):
            if elem % num == 0:
                is_prime = False
        
        if is_prime:
            count += 1
                
    return count

print(solution(arr))