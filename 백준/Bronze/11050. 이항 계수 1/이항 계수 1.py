import math

N, K = map(int, input().split())

answer = math.factorial(N) // (math.factorial(N-K)*math.factorial(K))
print(answer)