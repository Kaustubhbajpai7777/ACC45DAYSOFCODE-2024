# cook your dish here
T = int(input())
for _ in range(T):
    decisions = list(map(int, input().split()))
    print("IN" if all(d == 0 for d in decisions) else "OUT")
