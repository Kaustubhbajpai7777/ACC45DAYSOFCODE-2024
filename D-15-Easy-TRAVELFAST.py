# cook your dish here
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a > b:
        print("CAR")
    elif a == b:
        print("SAME")
    else:
        print("BIKE")
