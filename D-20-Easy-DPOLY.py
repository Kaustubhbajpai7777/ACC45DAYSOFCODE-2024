# cook your dish here
T = int(input())
for _ in range(T):
    N = int(input())
    coefficients = list(map(int, input().split()))
    
    # Find the highest index with a non-zero coefficient
    degree = next(i for i in range(N - 1, -1, -1) if coefficients[i] != 0)
    
    print(degree)
