# cook your dish here
def election_results(test_cases):
    results = []
    for votes in test_cases:
        XA, XB, XC = votes
        if XA > 50:
            results.append("A")
        elif XB > 50:
            results.append("B")
        elif XC > 50:
            results.append("C")
        else:
            results.append("NOTA")
    return results

T = int(input())
test_cases = []

for _ in range(T):
    votes = list(map(int, input().split()))
    test_cases.append(votes)

results = election_results(test_cases)

for result in results:
    print(result)
