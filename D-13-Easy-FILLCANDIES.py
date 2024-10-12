# cook your dish here
t = int(input())
for _ in range(t):
    n, k, m = map(int, input().split())
    if n % (k * m) == 0:
        print(n // (k * m))
    else:
        print(n // (k * m) + 1)
