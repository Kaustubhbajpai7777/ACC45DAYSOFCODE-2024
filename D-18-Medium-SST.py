# cook your dish here
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    
    valuation_first = A * 10 
    valuation_second = B * 5  
    
    if valuation_first > valuation_second:
        print("FIRST")
    elif valuation_second > valuation_first:
        print("SECOND")
    else:
        print("ANY")
