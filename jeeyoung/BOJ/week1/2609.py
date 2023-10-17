# 2609 - 최대공약수와 최대공배수

n, m = map(int, input().split())

def gcd(n, m):
    for i in range(m, 0, -1):
        if (n % i == 0) and (m % i == 0):
            return i

result1 = gcd(n, m)
result2 = n*m // result1

print(result1)
print(result2)