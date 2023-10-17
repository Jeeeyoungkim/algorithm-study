# 11653 - 소인수분해

num = int(input())

factor = []

while(num > 1):
    for i in range(2, num+1):
        if num % i == 0:
            print(i)
            num = num // i
            break
        