# cook your dish here
t = int(input())
for _ in range(t):
    __ = int(input())
    Array = sorted(list(map(int , input().split())))
    Array_set = sorted(list(set(Array)))
    for Num in Array_set:
        if Array.count(Num) % Num != 0:
            print("NO")
            break
    else:
        print("YES")