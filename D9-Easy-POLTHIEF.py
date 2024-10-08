# cook your dish here
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    d = abs(a - b)  # Use abs to get the absolute difference
    print(d)
