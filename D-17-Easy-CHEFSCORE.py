# cook your dish here
T = int(input())
for _ in range(T):
    N, X, Y = map(int, input().split())
    if Y % X == 0:
        print("YES")
    else:
        print("NO")
