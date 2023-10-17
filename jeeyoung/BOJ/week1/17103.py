# 17103

import math
import itertools

def get_primary_list(n):
    array = [1 for _ in range(n+1)]
    array[0], array[1] = 0, 0  # 0 and 1 are not prime numbers


    for i in range(2, int(n**0.5) + 1):
        if array[i]:
            j = 2
            
            while i * j <= n:
                array[i * j] = 0
                j+= 1
    
    return array

count = int(input())
primarys = get_primary_list(1000000)

for _ in range(count):
    n = int(input())
    gold_count = 0
    
    for num in range(2, n//2 + 1):
        if primarys[num] and primarys[n-num]:
            gold_count += 1
    
    print(gold_count)