# cook your dish here
# Function to calculate the maximum tastiness
def max_tastiness(T, test_cases):
    results = []
    for case in test_cases:
        a, b, c, d = case
        # Calculate all possible tastiness combinations
        tastiness1 = a + c
        tastiness2 = a + d
        tastiness3 = b + c
        tastiness4 = b + d
        # Find the maximum tastiness
        max_tastiness_value = max(tastiness1, tastiness2, tastiness3, tastiness4)
        results.append(max_tastiness_value)
    return results

# Input handling
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Get the results
results = max_tastiness(T, test_cases)

# Output results
for result in results:
    print(result)
