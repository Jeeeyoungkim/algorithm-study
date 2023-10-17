# 소수 구하기

x, y = map(int, input().split())
import math

def solution(x, y):    
    for i in range(x, y+1):
        if i == 1:
            continue
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                break # 소수가 아님
        else:
            print(i)
       
solution(x,y)