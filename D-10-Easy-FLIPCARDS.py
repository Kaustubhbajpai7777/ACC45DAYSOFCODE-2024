# cook your dish here
t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    if x < (n - x):
        print(x)
    else:
        print(n - x)
