# cook your dish here
def main():
    T = int(input(""))  
    results = []
    
    for _ in range(T):
        X, Y = map(int, input().split())  
        total_hours = (4 * X) + Y
        results.append(total_hours)
    
    for hours in results:
        print(hours)

if __name__ == "__main__":
    main()
