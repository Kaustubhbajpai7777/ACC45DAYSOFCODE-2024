# cook your dish here
def atm_withdrawal(test_cases):
    results = []
    
    for case in test_cases:
        N, K = case[0]
        A = case[1]
        
        result = []
        for amount in A:
            if K >= amount:
                result.append('1')
                K -= amount
            else:
                result.append('0')
        
        results.append(''.join(result))
    
    return results

# Input reading
T = int(input())
test_cases = []

for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    test_cases.append(((N, K), A))

# Processing
results = atm_withdrawal(test_cases)

# Output results
for res in results:
    print(res)
