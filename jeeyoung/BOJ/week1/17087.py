# 17087
import itertools

def gcd(a,b):
    if (a < b):
        a, b = b, a # a가 더 큰 수
    
    while(b):  # b가 0이 될때까지
        a, b = b, a % b
        
    return a


bro, subin = list(map(int, input().split()))
bro_list = [abs(subin-int(i)) for i in input().split()]

result = bro_list[0]
for i in range(1, bro):
    result = gcd(result, bro_list[i])

print(result)