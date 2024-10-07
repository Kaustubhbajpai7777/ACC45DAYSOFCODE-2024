# cook your dish here
def main():
    t = int(input())
    for _ in range(t):
        a, b, c, d = map(int, input().split())
        
        if a in (b, c, d):
            print("YES")
        elif a in (b + c, b + d, c + d, b + c + d):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
