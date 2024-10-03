# cook your dish here
def max_people_in_room(test_cases):
    results = []
    for case in test_cases:
        N, X, A = case
        current_people = X
        max_people = X
        
        for change in A:
            current_people += change
            max_people = max(max_people, current_people)
        
        results.append(max_people)
    
    return results

T = int(input().strip())
test_cases = []
for _ in range(T):
    N, X = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    test_cases.append((N, X, A))

results = max_people_in_room(test_cases)
for result in results:
    print(result)
