# cook your dish here
def min_wins_to_qualify(test_cases):
    results = []
    for X, Y in test_cases:
        min_wins = max(0, X - Y)
        results.append(min_wins)
    return results

T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

results = min_wins_to_qualify(test_cases)

for result in results:
    print(result)
