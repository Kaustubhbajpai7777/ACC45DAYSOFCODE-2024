def main():
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        temp = (b - 1) // a
        print(temp)

if __name__ == "__main__":
    main()
