# https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem
def fibonacci(n):
    w = {}
    for i in range(n+1):
        if i in [0,1]:
            w[i] = i
        else:
            w[i] = w[i-1] + w[i-2]
    return w[n]
n = int(input())
print(fibonacci(n))
