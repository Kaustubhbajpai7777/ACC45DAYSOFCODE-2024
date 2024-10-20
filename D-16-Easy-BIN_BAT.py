import sys
import math

def total_time_for_event(test_cases):
    results = []
    for N, A, B in test_cases:
        k = int(math.log2(N))  # Number of rounds
        total_time = k * A + (k - 1) * B
        results.append(total_time)
    return results

# Read input
input = sys.stdin.read
data = input().strip().splitlines()

T = int(data[0])  # Number of test cases
test_cases = [tuple(map(int, line.split())) for line in data[1:T + 1]]

# Calculate results
results = total_time_for_event(test_cases)

# Output results
for result in results:
    print(result)