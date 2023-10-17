# 9020
import math

def func_is_prime(n):
    is_prime = True
    
    for i in range(2, int(math.sqrt(n))+1):
        if (n % i) == 0:
            is_prime = False
            break;
    
    return is_prime
    
def get_prime_list(n):
    prime_list = []
    
    for i in range(2, n+1):
        if func_is_prime(i):
            prime_list.append(i)
    
    return prime_list


all_prime_list = get_prime_list(10000)

i = 0
count = int(input())

while i < count:
    n = int(input())
    num = n/2
    
    while num >= 0:
        if num in all_prime_list and n - num in all_prime_list:
            print(int(num), int(n-num))
            break
        else:
            num -= 1
    
    i += 1

    
